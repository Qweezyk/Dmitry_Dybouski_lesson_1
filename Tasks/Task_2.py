list = []
i = 0
variable_one = 0
variable_one_analog = 0
variable_two = 0
variable_two_analog = 0
result_one = 0
result_one_analog = 0
while i <= 1000:
    if i % 2:
        variable_one = (i ** 3)
        list.append(i ** 3)
        another = variable_one
        variable_one_analog = variable_one
        if variable_one > 0:
            while variable_one > 0:
                result_one += variable_one % 10
                variable_one = variable_one // 10
            if result_one % 7 == 0:
                variable_two+= another
            result_one = 0
        if variable_one_analog > 0:
            variable_one_analog += 17
            while variable_one_analog > 0:
                result_one_analog += variable_one_analog % 10
                variable_one_analog = variable_one_analog // 10
            if result_one_analog % 7 == 0:
                variable_two_analog += another + 17
            result_one_analog = 0
    i += 1
print('Список из кубов нечётных чисел от 1 до 1000: ', list)
print('Сумма цифр которых делится нацело на 7:', variable_two)
print('Повтороное вычисленния суммы после преобразования и проверки:', variable_two_analog)