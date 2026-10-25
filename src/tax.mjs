/** Synthetic demo code only — no ARCADA application data. */
export function calculateTax(subtotal, rate) {
  if (!Number.isFinite(rate) || rate < 0) throw new RangeError("invalid tax rate");
  return Math.round(subtotal * rate * 100) / 100;
}
