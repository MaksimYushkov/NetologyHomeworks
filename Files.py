from pprint import pprint


def txt_to_dict(file_name):

    with open(file_name, encoding='utf-8') as file_rec:
        cook_book = {}
        dish_name = file_rec.readline().strip()

        for line in file_rec:
            quantity = int(line)
            lines = []
            for item in range(quantity):
                ingredients_dict = {}
                ingredients_list = file_rec.readline().split(' | ')
                ingredients_dict['ingredient name'] = ingredients_list[0]
                ingredients_dict['quantity'] = ingredients_list[1]
                ingredients_dict['measure'] = ingredients_list[2].strip()
                lines.append(ingredients_dict)

            if dish_name not in cook_book:
                cook_book[dish_name] = lines
            else:
                cook_book[dish_name] += lines
            file_rec.readline()
            dish_name = file_rec.readline().strip()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count=1):
    cook_book = txt_to_dict('recipes.txt')
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for ingredient in ingredients:
            ingredient_copy = ingredient.copy()
            ingredient_name = ingredient_copy['ingredient name']
            ingredient_copy.pop('ingredient name')
            if ingredient_name not in shop_list:
                ingredient_copy['quantity'] = int(ingredient_copy['quantity']) * person_count

            else:
                count = shop_list[ingredient_name]['quantity']
                ingredient_copy['quantity'] = int(ingredient_copy['quantity']) * person_count + count
            shop_list[ingredient_name] = ingredient_copy

    return shop_list


pprint(txt_to_dict('recipes.txt'))
print('----------------')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
pprint(get_shop_list_by_dishes(['Омлет'], 2))