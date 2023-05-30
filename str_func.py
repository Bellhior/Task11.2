def upper(words):
    """Заглавные буквы во всей строке"""
    upper_words = words.upper()
    return upper_words


def title(words):
    """Заглавные буквы каждого слова строки"""
    titled_words = words.title()
    return titled_words


"""Добавление интерфейса ввода для пользователя"""
a = input("Введите строку")
print(upper(a))

b = input("Введите строку")
print(title(b))
