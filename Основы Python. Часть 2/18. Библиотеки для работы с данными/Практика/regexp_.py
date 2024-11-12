import re


if __name__ == '__main__':
    s = "AUE - Hello world 2024 against"

    # Любой символ кроме пропуска строки
    r = re.findall(r'.', s)
    print(r)

    # Любую букву или цифру
    r = re.findall(r'\w', s)
    print(r)

    # Целые слова
    r = re.findall(r'\w+', s)
    print(r)

    # Все подстроки начинающиеся на гласные (aeiouAEIOU)
    r = re.findall(r'[aeiouAEIOU]\w+', s)
    print(r)

    # Все слова начинающиеся на гласные (aeiouAEIOU)
    r = re.findall(r'\b[aeiouAEIOU]\w+', s)
    print(r)


