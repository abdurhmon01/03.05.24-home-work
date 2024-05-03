def remove_nth_char(input_str, n):
    if n < 0 or n >= len(input_str):
        return "Invalid index"
    return input_str[:n] + input_str[n+1:]

sample_str = "Python"
n = 2
result = remove_nth_char(sample_str, n)
print(result) 