def foo():
    with open('tx.txt') as f:
        cook_book = {}
        for line_d in f:
            name_dish = line_d.strip()  # 1 строчка
            amount = f.readline().strip()  # 2 строчка
            ingredients = []
            x = int(amount)
            for line in range(x):
                ingredient = f.readline().strip().split('|')  # 3 строчка
                ingredient_d = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                ingredients.append(ingredient_d)
                a = {name_dish: ingredients}
                cook_book.update(a)
            f.readline().strip()  # пустая строчка
    f.close()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    c_book = foo()
    grocery_dict = {}
    for dish_search in dishes:
        for dish, ingredients in c_book.items():
            if dish == dish_search:
                for i in ingredients:
                    ingredient = i['ingredient_name']
                    a = int(i['quantity'])
                    b = i['measure']
                    quanity = {'quantity': a * person_count, 'measure': b}
                    temp_dict = {ingredient: quanity}
                    grocery_dict.update(temp_dict)
    return grocery_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
