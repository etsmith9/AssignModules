import text_utils as tu

while True:
    choice = input("Type 1 if you would like to reverse your text, type 2 if you would like to capitolize your text, type 3 to exit:  ")
    if choice == '1':
        text_to_mod = input("Enter text you would like to reverse:  ")
        reversed_text = tu.reverse_string(text_to_mod)
        print(f" Your modified text is as follows:  {reversed_text}")
    if choice == '2':
        text_to_mod = input("Enter text you would like to capitolize:  ")
        capitalized_text = tu.capitalize_string(text_to_mod)
        print(f" Your modified text is as follows:  {capitalized_text}")
    if choice == '3':
        print("Exiting system. ")
        break