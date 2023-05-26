def winnie_the_pooh_rhythm(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

str = input("Введите вашу рифму: ")
if winnie_the_pooh_rhythm(str):
    print('Парам пам-пам')
else:
    print('Пам парам')