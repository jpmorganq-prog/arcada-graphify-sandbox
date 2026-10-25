import test from "node:test";
import assert from "node:assert/strict";
import { createInvoice, describeInvoice } from "../src/invoice.mjs";

test("synthetic invoice dependencies", () => {
  const items = [{ price: 12, quantity: 2 }, { price: 5, quantity: 1 }];
  assert.deepEqual(createInvoice(items, 0.1), {
    itemCount: 2, subtotal: 29, tax: 2.9, total: 31.9
  });
  assert.equal(describeInvoice(items, 0.1), "Invoice total: 31.90");
});
