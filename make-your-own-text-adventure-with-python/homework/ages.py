age_input = input("Please enter your age: ")
age = int(age_input)

if age < 10:
    if age <= 4:
        print("You are a toddler")
    else:
        print("You are a child")

    print("You are a minor")
    if age >= 7:
        print("You are in school")
elif age < 18:
    print("You are a teenager")
    print("You are an adolesent")
    print("You are a minor")
    print("You are still in school")
elif age >= 18:
    if age <= 35:
        print("You are a young adult")
    elif age > 35 and age <= 55:
        print("You are an adult")
    elif age > 55:
        print("You are an older adult")
    print("You are allowed to vote")
    print("You are allowed to buy alcohol")
else:
    print("That is wierd age to be")
