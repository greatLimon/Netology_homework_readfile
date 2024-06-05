
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

def main():
    print(readrecipes())

if __name__ == '__main__':
    main()