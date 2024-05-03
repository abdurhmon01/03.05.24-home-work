
def remove_repeated_chars(input_str):
    result = ""
    for i in range(len(input_str)):
        if i == 0 or input_str[i] != input_str[i-1]:
            result += input_str[i]
    return result

print(remove_repeated_chars("Red Green White"))  
print(remove_repeated_chars("aabbbcdefff")) 
print(remove_repeated_chars("Yellowwooddoor")) 
