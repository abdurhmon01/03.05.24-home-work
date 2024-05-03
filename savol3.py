
def swap_first_two_chars(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " + new_str2

sample_str1 = 'abc'
sample_str2 = 'xyz'
result = swap_first_two_chars(sample_str1, sample_str2)
print(result)  

