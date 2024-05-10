with open('pupils_txt.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()
    fives = []
    mark_sum = 0
    for p in text:
        pupil = p.split()
        mark = pupil[2]
        name = pupil[0]
        text = name + ' - ' + mark
        print(text)
        mark_sum += int(mark)
        if mark == '5':
            fives.append(name)
    average = mark_sum/len(text)
    print('\nСредний балл:', round(average, 2))
    print('\nСписок отличников:')
    for p in fives:
        print(p)