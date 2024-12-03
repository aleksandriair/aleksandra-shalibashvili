import json
import itertools


def load_dict_from_json(input_file):
    with open(input_file, "r") as f:
        result = json.load(f)
    return result


def find_ingredients(recipes, markets, dish):
    ingredients_needed = set(recipes[dish]["ingredients"])

    available_ingredients = set()
    valid_shops = {}
    for shop, items in markets.items():
        covered = ingredients_needed.intersection(items)
        if covered:
            valid_shops[shop] = covered
            available_ingredients.update(covered)

    unavailable = ingredients_needed - available_ingredients
    if unavailable:
        print(f"\nWarning: These ingredients are not available in any store: {', '.join(unavailable)}")

    for r in range(1, len(valid_shops) + 1):
        for shops_combo in itertools.combinations(valid_shops.keys(), r):
            covered_ingredients = set()
            shopping_list = {}

            for shop in shops_combo:
                remaining_ingredients = available_ingredients - covered_ingredients
                shop_ingredients = remaining_ingredients.intersection(markets[shop])
                if shop_ingredients:
                    shopping_list[shop] = list(shop_ingredients)
                    covered_ingredients.update(shop_ingredients)

            if covered_ingredients == available_ingredients:
                return shopping_list

    return {}


def print_pretty_dict(dictionary):
    pretty_dict = ""
    for k, v in dictionary.items():
        pretty_dict += f"\n{k}:\n"
        for value in v:
            pretty_dict += f"    {value}\n"
    return pretty_dict


def main():
    recipes = load_dict_from_json("recipes.json")
    markets = load_dict_from_json("markets.json")
    dishes = list(recipes.keys())

    print("\nWelcome to our meal planning app!")
    print("\nPlease select a dish from these options:")

    for i in range(len(dishes)):
        print(str(i + 1) + ". " + dishes[i])

    dish = input("\nEnter dish name: ")

    shopping_list = find_ingredients(recipes, markets, dish)
    print(f"\nWe suggest that you go to these grocery stores:\n{print_pretty_dict(shopping_list)}")


if __name__ == "__main__":
    main()
