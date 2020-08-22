class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def calories(self):
        return (self.carbs * 4) + (self.protein * 4) + (self.fat * 9)


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(self):
        calories = 0
        for ingredient in self.ingredients:
            calories = calories + ingredient.calories()
        return calories

    def __str__(self):
        return self.name


recipes = [
    Recipe(
        "Milkshake",
        [Food("Milk", 10, 15, 20), Food("Ice Cream", 10, 15, 30),
         Food("Penaut Butter", 20, 25, 15)]
    ),
    Recipe(
        "Toast",
        [Food("Bread", 15, 15, 5), Food("Butter", 18, 10, 22)]
    )
]

for recipe in recipes:
    print("{} has {} calories".format(recipe, recipe.calories()))
