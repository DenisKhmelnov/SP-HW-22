# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def read():
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data

def sort(data):
    return sorted(data, key=lambda x: int(x['age']))

def filter(data):
    return [x for x in data if int(x['age']) > 10]


def get_users_list():
    # Чтение данных из строки
    data = read()

    # Сортировка по возрасту по возрастанию
    data = sort(data)
    # Фильтрация
    return filter(data)


if __name__ == '__main__':
    print(get_users_list())
