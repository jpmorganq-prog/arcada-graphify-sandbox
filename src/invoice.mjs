/** Synthetic demo code only — no ARCADA application data. */
import { calculateSubtotal } from "./pricing.mjs";
import { calculateTax } from "./tax.mjs";

export function createInvoice(items, taxRate) {
  const subtotal = calculateSubtotal(items);
  const tax = calculateTax(subtotal, taxRate);
  return { itemCount: items.length, subtotal, tax, total: subtotal + tax };
}

export function describeInvoice(items, taxRate) {
  const invoice = createInvoice(items, taxRate);
  return `Invoice total: ${invoice.total.toFixed(2)}`;
}
