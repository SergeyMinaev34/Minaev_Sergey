# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    result = text.split()
    result = ''.join(result)
    result = list(result)
    my_list = []
    for i in range(len(result)):
        if result[i].isalpha():
            my_list.append(result[i])
    result = ''.join(my_list)
    letter_dict = {}
    for i in result:
        letter_dict[i] = result.count(i)
    return letter_dict
# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict):
    summary = 0
    for score in letter_dict.values():
        summary = summary + score
    frequency = {}
    for score in letter_dict.values():
        frequency[score] = round(score / summary, 2)
    sum_dict = dict()
    for score, letter in letter_dict.items():
        sum_dict[score] = frequency[letter]
    return sum_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
# TODO Распечатайте в столбик букву и её частоту в тексте
frequency = calculate_frequency(count_letters(main_str))
for key, value in frequency.items():
    print(f"{key}: {value:.2f}")

