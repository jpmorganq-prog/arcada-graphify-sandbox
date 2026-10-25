#!/usr/bin/env node
// Codex App Server discovery test. Does not start a model turn or use credentials.
import { spawn } from "node:child_process";
import { createInterface } from "node:readline";
import process from "node:process";
import path from "node:path";
import assert from "node:assert/strict";

const required = ["experimental-design", "statistical-analysis", "uncertainty-and-units"];
const cwd = process.cwd();
const child = spawn("codex", ["app-server"], {
  cwd, env: process.env, stdio: ["pipe", "pipe", "pipe"]
});
const reader = createInterface({ input: child.stdout });
let stderr = "";
let complete = false;
const timer = setTimeout(() => finish(new Error("codex skills/list timed out")), 60000);
child.stderr.on("data", chunk => { stderr = (stderr + String(chunk)).slice(-3000); });
child.on("error", err => finish(err));
child.on("exit", (code) => {
  if (!complete) finish(new Error("codex exited early with code " + code + "\n" + stderr));
});
function send(msg) { child.stdin.write(JSON.stringify(msg) + "\n"); }
function finish(error) {
  if (complete) return;
  complete = true;
  clearTimeout(timer);
  reader.close();
  child.kill();
  if (error) { console.error("FAIL CODEX DISCOVERY:", error.message); process.exitCode = 1; }
}
reader.on("line", line => {
  let obj;
  try { obj = JSON.parse(line); } catch { return finish(new Error("invalid JSONL: " + line.slice(0,200))); }
  if (obj.id === 0) {
    if (obj.error) return finish(new Error("initialize: " + JSON.stringify(obj.error)));
    console.log("CODEX_APP_SERVER_INITIALIZED", obj.result?.userAgent || "unknown-version");
    send({ method: "initialized", params: {} });
    send({ id: 1, method: "skills/list", params: { cwds: [cwd], forceReload: true } });
  } else if (obj.id === 1) {
    if (obj.error) return finish(new Error("skills/list: " + JSON.stringify(obj.error)));
    try {
      const records = obj.result?.data || [];
      assert.equal(records.length, 1, "one directory result expected");
      assert.deepEqual(records[0].errors || [], [], "no skill scanning errors");
      const skills = records[0].skills || [];
      for (const name of required) {
        const matches = skills.filter(skill => skill.name === name);
        assert.equal(matches.length, 1, "skill missing or duplicated: " + name);
        const rawPath = matches[0].path || matches[0].location || "";
        const normalized = String(rawPath).replaceAll("\\", "/");
        assert.ok(normalized.includes("/.agents/skills/" + name + "/SKILL.md"), "wrong skill path for " + name + ": " + normalized);
        console.log("PASS CODEX SKILL", name, matches[0].scope || "scope-unknown", normalized.replace(cwd, "<repo>"));
      }
      console.log("ALL 3 CODEX SKILLS DISCOVERED WITHOUT MODEL AUTH");
      finish();
    } catch (err) { finish(err); }
  }
});
send({ id: 0, method: "initialize", params: {
  clientInfo: { name: "arcada_science_ci", title: "ARCADA isolated science tests", version: "1.0.0" }
}});
