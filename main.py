
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

def merge_files_with_sort_by_len()->None:
    f1 = open('files/1.txt', 'r', encoding='utf-8')
    f2 = open('files/2.txt', 'r', encoding='utf-8')
    f3 = open('files/3.txt', 'r', encoding='utf-8')

    data_list = [(f1.readlines(), "1"), (f2.readlines(), "2"), (f3.readlines(), "3")]
    
    f1.close()
    f2.close()
    f3.close()

    data_list.sort(key = lambda data : len(data[0]))
    with open('files/result.txt', 'w', encoding='utf-8') as res_file:
        for data in data_list:
            for ids, line in enumerate(data[0]):
                res_file.write(line)
                print(f'{line.rstrip()}\nСтрока номер {ids+1}, Файл номер {data[1]}')
            res_file.write('\n')
            print('\n')

        ...



def main():
    merge_files_with_sort_by_len()

if __name__ == '__main__':
    main()