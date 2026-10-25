/** Synthetic demo code only — no ARCADA application data. */
export function calculateSubtotal(items) {
  if (!Array.isArray(items)) throw new TypeError("items must be an array");
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}
