
def add_ing_or_ly(input_str):
    if len(input_str) < 3:
        return input_str
    elif input_str[-3:] == 'ing':
        return input_str + 'ly'
    else:
        return input_str + 'ing'

sample_str1 = 'abc'
sample_str2 = 'string'
result1 = add_ing_or_ly(sample_str1)
result2 = add_ing_or_ly(sample_str2)
print(result1)  
print(result2)  

