"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""

def int_func():
    wrd = input("Введите слово из маленьких латинских букв: ")
    return wrd.title()

print(int_func())

def my_func():
    res = []
    wrds = input("Введите слова через пробел: ").split(' ')
    for i in wrds:
        el = str(i)
        first_letter = el[:1].upper()
        wrd = first_letter + el[1:]
        res.append(wrd)
    return res
print(my_func())