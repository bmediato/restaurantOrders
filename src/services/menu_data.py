import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self._read_menu(source_path)
        self.dishes = set()

        with open(source_path, mode='r') as pratos:
            reader = csv.reader(pratos)
            for row in reader:
                dish = row[0]
                price = float(row[1])
                ingredient = row[2]
                recipe_amount = int(row[3])

                dish = self._get_or_create_dish(dish, price)
                ingredient = Ingredient(ingredient)
                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish
