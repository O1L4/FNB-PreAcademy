#cost_calculator.py

print("cost calculator")
km = float(input("Kilometers: "))
price = float(input("petrol price per liter: R"))

litre = km / 10 
total = liters * price

print(f"Total cost: R{round(total, 2)}")