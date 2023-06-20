from csv import DictReader
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        dishes_map = {}

        with open(source_path, mode="r") as doc:
            for row in DictReader(doc):
                dish_name = row["dish"]
                if dish_name in dishes_map:
                    dish = dishes_map[dish_name]
                else:
                    dish = Dish(dish_name, float(row["price"]))
                    dishes_map[dish_name] = dish
                    self.dishes.add(dish)
                ingredient = Ingredient(row["ingredient"])
                recipe_amount = int(row["recipe_amount"])
                dish.add_ingredient_dependency(ingredient, recipe_amount)
