def culinary_dictionary(recipes):
    cook_book = {}
    with open(recipes, encoding='utf-8') as f:
        elements = f.readlines()
        for line in elements:
            if (not line.strip().isdigit() and ' | ' not in line
                and line != '\n'):
                dish = line.strip()
                cook_book[dish] = []
            elif '|' in line:
                ingredients_list = line.rstrip().split(' | ')
                ingredients_dict = {'ingredient_name': ingredients_list[0],
                                    'quantity': int(ingredients_list[1]),
                                    'measure': ingredients_list[2]}
                cook_book[dish].append(ingredients_dict)
    return cook_book

cook_book = culinary_dictionary('recipes.txt')         
print(cook_book, end='\n\n')

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in ingredients:
                    ingredients[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count}
                else:
                    ingredients[ingredient['ingredient_name']]['quantity'] += \
                    ingredient['quantity'] * person_count
    return ingredients

print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 
                               'Картофель фри'], 2))

def connect(*files):
    lines = {}
    for file in files:
        with open(file, encoding='utf-8') as f:
            quantity_lines = len(f.readlines())
            lines[file] = quantity_lines
    
    sorting_lines = dict(sorted(lines.items(), key=lambda x: x[1]))
    result = 'file_result.txt'
    clear_result = open(result, 'w')
    clear_result.close()

    for text, line in sorting_lines.items():
        with open(text, encoding='utf-8') as f2:
            text_read = f2.read()
        with open(result, 'a', encoding='utf-8') as f1:
            f1.write(f'{text}\n{line}\n{text_read}\n')

connect('1.txt', '2.txt', '3.txt')