price = 25000
quantity = 2
discount = 5000

subtotal = price * quantity
final_total = subtotal - discount

print(f"Mahsulot narxi: {price} so'm")
print(f"Soni: {quantity} ta")
print(f"Chegirmasiz jami: {subtotal} so'm")
print(f"Chegirma: {discount} so'm")
print(f"To'lanadigan summa: {final_total} so'm")

print("-----")

product = "Non"
price = 4000
quantity = 5

total = price * quantity
print(f"{product}: {quantity} ta x {price} so'm = {total} so'm")

print("-----")

total_bill = 100000
customers = 3

each_person = total_bill / customers # kasrli bo'lish
each_person_int = total_bill // customers # butun bo'lish
remainder = total_bill % customers # qoldiq

print(f"Umumiy hisob: {total_bill} so'm")
print(f"Odamlar soni: {customers}")
print(f"Har bir odam to'laydi: {each_person} so'm")
print(f"Butun bo'lib to'lash: {each_person_int} so'm")
print(f"Qoldiq: {remainder} so'm")

print("-----")

number = 5
square = number ** 2
print(f"{number} ning kvadrati: {square}")

base = 2    
power = 4
result = base ** power

print (f"{base} ning {power}-darajasi: {result}")



