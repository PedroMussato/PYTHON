import csv

def validateCpf(number):
    # Convert the digits of the number into a list of integers
    cpf = [int(digit) for digit in number if digit.isdigit()]

    if len(cpf) != 11:
        return False

    # Calculate the first verification digit
    sum_ = sum((cpf[i] * (10 - i) for i in range(9)))
    first_digit = 11 - (sum_ % 11)
    first_digit = first_digit if first_digit < 10 else 0

    # Calculate the second verification digit
    sum_ = sum((cpf[i] * (11 - i) for i in range(10)))
    second_digit = 11 - (sum_ % 11)
    second_digit = second_digit if second_digit < 10 else 0

    # Check if the last two digits of the CPF match the calculated verification digits
    return cpf[-2:] == [first_digit, second_digit]


def validateCnpj(number):
    # Convert the digits of the number into a list of integers
    cnpj = [int(digit) for digit in number if digit.isdigit()]

    if len(cnpj) != 14:
        return False

    def calculateDigit(digits, multipliers):
        # Calculate a single verification digit for the given digits and multipliers
        sum_ = sum((digits[i] * multipliers[i] for i in range(len(digits))))
        remainder = sum_ % 11
        return 0 if remainder < 2 else 11 - remainder

    # Calculate the first and second verification digits for CNPJ
    first_digit = calculateDigit(cnpj[:12], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    second_digit = calculateDigit(cnpj[:13], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

    # Check if the last two digits of the CNPJ match the calculated verification digits
    return cnpj[-2:] == [first_digit, second_digit]

# Open the CSV file for reading
with open('CPFsCNPJs.csv', 'r') as file:
    # Create a CSV reader object
    data = csv.reader(file)
    for line in data:
        if line[0] == 'cnpj':
            # If the line represents a CNPJ number, validate it using the validateCnpj function
            if not validateCnpj(line[1]):
                print('Error')
        if line[0] == 'cpf':
            # If the line represents a CPF number, validate it using the validateCpf function
            if not validateCpf(line[1]):
                print('Error')
