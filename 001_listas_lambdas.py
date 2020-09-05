from helper_functions import double_number

numbers_list = [
    8,
    10,
    23,
    38,
    126,
    128,
    18,
    19,
    22,
    9,
]


# ----------------------------------------------------------------
# Compute of double of number function with static number
number=2500
number_double=double_number(number) # double_number(2500)
print('--------------------------------')
print(f'Calculando el doble de {number} = {number_double}\n\n')
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# Apply double_number to all list
print('--------------------------------')
for n in numbers_list:
    r = double_number(n) # double_number(position_n)
    print(f'Calculando el doble de {n} = {r}')
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# Apply double_number using map
print('\n\n--------------------------------')
numbers_list_double = list(map(double_number, numbers_list))
print(numbers_list)
print(numbers_list_double)
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# Apply double_number using lambda
print('\n\n--------------------------------')
double = lambda value: value * 2
print(double(45))
# ----------------------------------------------------------------
