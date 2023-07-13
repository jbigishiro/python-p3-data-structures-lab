spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]



def get_names(spicy_foods):
    names=[]
    for food in spicy_foods:
        names.append(food["name"])
    return names
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level']>5 ]
print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}") for food in spicy_foods]
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_food={}
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            matching_food=food
    return matching_food
print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
 for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_indicator = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_indicator}")
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat
print(get_average_heat_level(spicy_foods))


spicy_food={
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
      }

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food (spicy_foods, spicy_food))
