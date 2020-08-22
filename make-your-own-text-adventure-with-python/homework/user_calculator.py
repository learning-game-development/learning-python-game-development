def add(value_one, value_two):
    return value_one + value_two


def make_number(value):
    try:
        return int(value)
    except ValueError:
        print('"{}" is not a number.'.format(value))
        return None


while True:  # WARNING: Infinate loop!
    print("Which 2 numbers do you want to add?")
    input_value_one = input("First number: ")
    input_value_two = input("Second number: ")

    value_one = make_number(input_value_one)
    value_two = make_number(input_value_two)

    if value_one != None and value_two != None:
        print(
            "The values {} plus {} is equal to {}.".format(
                input_value_one,
                input_value_two,
                add(value_one, value_two)
            )
        )
