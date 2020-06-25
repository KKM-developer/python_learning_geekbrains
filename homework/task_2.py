"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('task_2.txt', 'r', encoding='UTF-8') as file:
    line = file.readlines()
    line = [l.rstrip() for l in line]
    line_count = len(line)
    print('Всего строк ', line_count)
    word_count = 1
    for i in line:
        words = i.split(' ')
        words = [word.replace(',', '').replace('.', '') for word in words]
        for w in words:
            if w.isalnum() == False:
                words.remove(w)
        print(f'В строке {word_count}, {len(words)} слов')
        word_count += 1
        #print(words)
