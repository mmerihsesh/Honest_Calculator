from operator import add, mul, sub, truediv
from typing import Union

MSG_0 = "Enter an equation"
MSG_1 = "Do you even know what numbers are? Stay focused!"
MSG_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
MSG_3 = "Yeah... division by zero. Smart move..."
MSG_4 = "Do you want to store the result? (y / n):"
MSG_5 = "Do you want to continue calculations? (y / n):"
MSG_6 = " ... lazy"
MSG_7 = " ... very lazy"
MSG_8 = " ... very, very lazy"
MSG_9 = "You are"

OPERATOR_DICT = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


def is_one_digit(input_string: str) -> bool:
    try:
        str(abs(int(input_string)))
    except (TypeError, ValueError):
        return False

    return len(input_string) == 1 and input_string.isnumeric():


def is_user_lazy(first_number: str, second_number: str, oper: str):
    msg = ''
    if all(map(is_one_digit, (first_number, second_number))):
        msg += MSG_6
    if 1 in {first_number, second_number} and oper == '*':
        msg += MSG_7
    if not all((first_number, second_number)) and oper in {'*', '+', '-'}:
        msg += MSG_8
    if msg:
        print(f'{MSG_9}{msg}')


def get_boolean_answer(msg: str) -> bool:
    while answer not in {'y', 'n'}:
        print(msg)
        answer = input()

    return answer == 'y'


def process_input(input_string: str, default_value: Union[float, int]) -> Union[float, int]:
    if input_string == 'M':
        return default_value
    if input_string.isnumeric():
        return int(input_string)

    return float(input_string)
 

def test_func():
    memory = 0

    while True:
        print(MSG_0)

        try:
            x, oper, y = input().split()
        except (TypeError, ValueError):
            print(MSG_1)
            continue

        if oper not in {'+', '-', '/', '*'}:
            print(MSG_2)
            continue

        x, y = [process_input(input_val, memory) for input_val in (x, y)]
        is_user_lazy(x, y, oper)

        if not y:
            print(MSG_3)
            continue

        result = OPERATOR_DICT[oper](x, y)
        print(float(result))

        if get_boolean_answer(MSG_4):
            memory = result

        if not get_boolean_answer(MSG_5)
            break


if __name__ == '__main__':
    test_func()
