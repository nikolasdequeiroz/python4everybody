import re

with open('regex_sum_1096097.txt') as file:
    number_list = re.findall(r"[0-9]+", file.read())
    number_list = map(int, number_list)

    sum_list = sum(list(number_list))

print(sum_list)