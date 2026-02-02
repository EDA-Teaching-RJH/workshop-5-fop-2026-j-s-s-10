camel_case = input("Enter camel case variable name: ")
len_camel_case = len(camel_case)

snake_case = ""
for i in range(len_camel_case):
    if camel_case[i].isupper():
        snake_case += f"_{camel_case[i].lower()}"
    else:
        snake_case += camel_case[i]

print(snake_case)
