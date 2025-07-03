item_prices = [100, 200, 50]      
quantities = [2, 1, 4]            
discount_rate = 0.10              
tax_rate = 0.08                  
subtotal = sum(p * q for p, q in zip(item_prices, quantities))
discount = subtotal * discount_rate
taxable_amount = subtotal - discount
tax = taxable_amount * tax_rate
total_cost = taxable_amount + tax
print("Subtotal: ₹", round(subtotal, 2))
print("Discount: ₹", round(discount, 2))
print("Tax: ₹", round(tax, 2))
print("Total Cost to Customer: ₹", round(total_cost, 2))
