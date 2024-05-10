with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)

author = input('Кто автор этой цитаты?')
with open('quotes.txt', 'a', encoding='UTF-8') as file:
    text = '('+author+')\n'
    file.write(text)

while True:
    answer = input('Хотите добавить ещё одну цитату? (да/нет)').lower()
    if answer == 'да':
        quote = input('Введите цитату')
        author = input('Введите автора')
        with open('quotes.txt', 'a', encoding='UTF-8') as file:
            text = quote + '\n(' + author + ')\n'
            file.write(text)
    else:
        break

with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)