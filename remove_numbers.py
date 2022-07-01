def remove_numbers(string):
    stack = []
    for item in string:
        if item.isdigit():
            pass
        else:
            stack.append(item)
    s = ''
    return s.join(stack)



print()
print()
string = input("Type a stirng of letters and numbers. Hit enter to remove all numbers:")
print()
print(remove_numbers(string))