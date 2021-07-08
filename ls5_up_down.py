def list_lower (my_list):
    return my_list.lower()
print(list_lower('Hello World'))
b = list_lower('Hello World')

def list_upper (my_list1):
    return my_list1.upper()
print(list_upper('Hello World'))
a= list_upper('Hello World')

list_lowered = list(map(list_lower,a))
list_uppered = list(map(list_upper,b))

print(list_lowered, list_uppered)

