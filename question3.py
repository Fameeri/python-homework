#Pet age calculator

pet_type = input("Enter pet type (dog/cat/bird/hamster): ").lower()
human_age = int(input("Enter your pet's age in human years: "))

pet_age = 0

if pet_type in ["dog", "cat"]:
    if human_age == 1:
        pet_age = 12
    elif human_age == 2:
        pet_age = 24
    elif human_age > 2:
        pet_age = 24 + (human_age - 2) * 4
    elif pet_type == "bird":
        pet_age = human_age * 9
    elif pet_type == "hamster":
        pet_age = human_age * 25
    else:
        print("Unsupported pet type.")
        exit()
        
    #Result
    
    print("\n=== Pet Age Conversation ===")
    print(f"Pet Type: {pet_type.capitalize()}")
    print(f"Human Age: {human_age} years")
    print(f"Pet Age: {pet_age} pet years")
    print(f"\nFun Fact: Your {pet_type} is like a {pet_age}-year-old human!")