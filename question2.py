print("=== Resturant Menu ===")
print("1. pizza - $15.99")
print("2. burger - $12.99")
print("3. salad - $11.99")
print("4. pasta - $14.99")

choice = int(input("\nEnter your choice (1-4): "))
drink = input("would you like a drink? (+$2.50) (yes/no): ").lower()

#food price
if choice == 1:
    food = "pizza"
    price = 15.99
elif choice == 2:
    food = "burger"
    price = 12.99
elif choice == 3:
    food = "salad"
    price = 11.99
elif choice == 4:
    food = "pasta"
    price = 14.99
else:
    print("Invalide choice.")
    exit()
    
    #add drink
drink_price = 2.50 if drink == "yes" else 0.00
subtotal = price + drink_price
tax = subtotal * 0.08
total = subtotal +tax

#Display bill
print("\n=== Your order ===")
print(f"Food: {food} - ${price:.2f}")
print(f"Drink: {'Yes' if drink == 'Yes' else 'No'} - ${drink_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")    