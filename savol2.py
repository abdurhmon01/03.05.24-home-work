
def count_characters_frequency(input_str):
    char_frequency = {}
    for char in input_str:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

sample_string = "google.com"
result = count_characters_frequency(sample_string)
print(result) 

