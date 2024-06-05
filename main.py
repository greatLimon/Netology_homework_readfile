
def readrecipes()->dict:
    with open('recipes.txt', encoding='utf-8') as f:
        recipes = f.readlines()
    cook_book = {}
    food_name = ''
    ing_count = 0
    count = 0
    ing = []
    for line in recipes:
        if food_name == '':
            food_name = line.rstrip()
        elif food_name != '' and ing_count == 0 and count == 0:
            ing_count = int(line.rstrip())
        elif food_name != '' and ing_count != 0 and count != ing_count:
            temp_line = line.rstrip().split(' | ')
            ing.append({
                'ingredient_name': temp_line[0], 
                'quantity': int(temp_line[1]), 
                'measure': temp_line[2]
            })
            count += 1
        elif count == ing_count:
            cook_book[food_name] = ing
            food_name = ''
            ing_count = 0
            count = 0
            ing = []
    cook_book[food_name] = ing
    return cook_book

def get_shop_list_by_dishes(dishes:list, person:int)->dict:
    if type(dishes) == list and len(dishes) == 0:
        return {}
    book = readrecipes()
    ingridients = {}
    for dish in dishes:
        for ing_book in book[dish]:
            if ing_book['ingredient_name'] in ingridients:
                ingridients[ing_book['ingredient_name']]['quantity'] += ing_book['quantity'] * person
            else:
                ingridients[ing_book['ingredient_name']] = {
                    'quantity': ing_book['quantity'] * person,
                    'measure' : ing_book['measure']
                }
    return ingridients

def main():
    print(get_shop_list_by_dishes(['Омлет', "Фахитос"], 3))

if __name__ == '__main__':
    main()