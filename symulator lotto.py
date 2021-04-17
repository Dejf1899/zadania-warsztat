import random

def lotto_number():

    while True:
        try:
            result = int(input("Chose the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result

def lotto_numbers():

    result = set()
    while len(result) < 6:
        number = lotto_number()
        if 0 < number <= 49:
            result.add(number)

    return result

def print_numbers(numbers):

    print(", ".join(str(number) for number in sorted(numbers)))

def drawing_numbers():

    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return set(numbers[:6])

def lotto():

    user_numbers = lotto_numbers()
    print("Your numbers:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

    hits = 6 - len(random_numbers - user_numbers)

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()