# the following lines read names from the input, do not modify it, please
name_1 = input()
name_2 = input()


def greeting(first_name, second_name):
    print("Hello,", first_name, "and", second_name)


greeting(name_1, name_2)
greeting(second_name=name_1, first_name=name_2)
