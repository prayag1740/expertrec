


def myplexer_print_data(input_string):
    input_string = input_string.lower()
    if input_string == "hi":
        return "Nice Work"
    elif input_string[0:7] == "sayhito":
        return f"Hi , {input_string[8:]}"
    elif input_string[0:5] == "count":
        count_elements = input_string[6:]
        count_elements_list = count_elements.split(" ")
        return len(count_elements_list)
    elif input_string == "exit":
        return "Exit"   
    else:
        return "Invalid command"