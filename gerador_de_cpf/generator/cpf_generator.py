from random import randint

def cpf_generator(cpf):
    
    i = 0
    while i < cpf:

        new_cpf = ""

        number = 0

        while number < 9:
            new_cpf += str(randint(0, 9))
            number += 1
        
        new_cpf = first_digit(new_cpf)
        new_cpf = second_number(new_cpf)

        print(new_cpf)

        i += 1


def first_digit(new_cpf):
    
    cpf_number_sum = 0

    multiplied = 10

    for number in new_cpf:
        number = int(number)

        cpf_number_sum += (number * multiplied)

        multiplied -= 1
    
    cpf_number_sum = (cpf_number_sum * 10) % 11

    if cpf_number_sum == 10:
        cpf_number_sum = 0

    new_cpf += str(cpf_number_sum)

    return new_cpf
    
def second_number(new_cpf):

    cpf_number_sum = 0

    multiplied = 11

    for number in new_cpf:
        number = int(number)

        cpf_number_sum += (number * multiplied)

        multiplied -= 1
    
    cpf_number_sum = (cpf_number_sum * 10) % 11

    if cpf_number_sum == 10:
        cpf_number_sum = 0


    new_cpf += str(cpf_number_sum)

    return new_cpf