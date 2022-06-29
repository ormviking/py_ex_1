import ipaddress
import math
from itertools import combinations

"""
Задача 01. Написать метод domain_name, который вернет домен из url адреса:
url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"
"""


def url_lower_1(new_url):
    url_lower = new_url.lower()
    return url_lower


def http_cleared(url):
    url_lower = url_lower_1(url)
    if url_lower[0:7] == "http://" or url_lower[0:8] == "https://":
        url_split = url_lower.split('//')
        http_clear_url = url_split[1]
    else:
        http_clear_url = url_lower
    return http_clear_url


def domain_name(new_url):
    clead_url = http_cleared(new_url)
    url_split = clead_url.split('.')
    if url_split[0] == "www":
        return url_split[1]
    else:
        return url_split[0]


"""
Задача 02. Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:
"""


def int32_to_ip(int32):
    return ipaddress.ip_address(int32)


"""
Задача 03 Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
"""


def zeros(n):
    number = int(n)  # ну мало ли кто float решит высчитать:)
    z = math.factorial(number)
    string = str(z)
    count = 0
    for symbol in string[::-1]:
        if symbol == '0':
            count = count + 1
        else:
            break
    return count


# второй вариант, без строк, но первый мне нравится больше

def zeros(n):
    if n < 5:
        return 0
    return n // 5 + zeros(n // 5)


"""
Задача 04. Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.
(Используйте - для обозначения зачеркнутой буквы)
"""


def bananas(s):
    word = 'banana'
    result = set()
    for combination in combinations(range(len(s)), len(s) - len(word)):
        list_one = list(s)
        for index in combination:
            list_one[index] = '-'
        variant = ''.join(list_one)
        if variant.replace('-', '') == word:
            result.add(variant)
    return result


"""
Задача 05. Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.
"""


def count_find_num(primes_l, limit):
    numbers_all = []
    total = math.prod(primes_l)
    numbers_all.append(total)
    if total > limit:
        return []
    for num in primes_l:
        for total in numbers_all:
            number = num * total
            if number <= limit and number not in numbers_all:
                numbers_all.append(number)
    return [len(numbers_all), max(numbers_all)]
