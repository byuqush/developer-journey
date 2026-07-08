print("Receipt Review App")
print("------")

customer_name = " Javlonbek "
product_name = " non "

price = 4000
quantity = 5
discount = 3000
delivery = 7000

clean_customer_name = customer_name.strip() # stript so'z boshi va oxiridagi bo'shlikni oladi
clean_product_name = product_name.strip().title() #title birinchi harfni katta qiladi

subtotal = price * quantity
final_total = subtotal - discount + delivery

print(f"Customer: {clean_customer_name}")
print(f"Product: {clean_product_name}")
print(f"Price: {price} so'm")
print(f"Quantity: {quantity} ta")
print(f"Subtotal: {subtotal} so'm")
print(f"Discount: {discount} so'm")
print(f"Delivery: {delivery} so'm")
print(f"Final total: {final_total} so'm")

print("------")
print("Type checks")

print(type(clean_customer_name)) # type bu qiymatlarni emas ularning turini chiqaradi
print(type(price))
print(type(quantity))
print(type(final_total))

print("------")
print("Operator priority")

result_1 = price * quantity + delivery
result_2 = price * (quantity + delivery)

print(f"price * quantity + delivery = {result_1}")
print(f"price * (quantity + delivery) = {result_2}")

