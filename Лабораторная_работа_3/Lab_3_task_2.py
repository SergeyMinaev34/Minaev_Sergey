# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, n = ','):
    first = first.split(n)
    second = second.split(n)
    first = set(first)
    summary = first.intersection(second)
    summary = list(summary)
    summary.sort()
    return summary
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
