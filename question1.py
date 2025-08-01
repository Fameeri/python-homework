name = input("Enter your name: ")

#Validation

while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

quantity = int(input("How many tickets do you want? "))

#ticket and type with price
if age < 13:
    ticket_type = "child"
    ticket_price = 8.00
elif 13 <= age <= 64:
    ticket_type = "Adult"
    ticket_price = 12.00
else:
    ticket_type = "senior"
    ticket_price = 9.00
    
    total_cost = ticket_price * quantity
    
    # Receipt Display
print("\n=== Movie Ticket Receiept ===")
print(f"Customer: {name}")
print(f"Ticket type: {ticket_type} (${ticket_price:.2f} each)")
print(f"Quantity: {quantity}")
print(f"Total cost: ${total_cost:.2f}")
print("Thank you for your purchase!")


