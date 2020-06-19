def up(word):
    return word[0].upper() + word[1:]


def list_up(words):
    word_up = []
    for i in words:
        i = i[0].upper() + i[1:]
        word_up.append(i)
    return word_up


a = 'hello'
print(up(a))

user_inp = input('введите слова, разделенные пробелами ').split(' ')
print(list_up(user_inp))