import requests
import json
from jsonpath_ng import jsonpath, parse

r = requests.get('https://world.openfoodfacts.org/api/v2/product/3017620429484.json')
foodjson = r.json()

searchstring = parse("$.product.ingredients_text")

ingredientsjson = searchstring.find(foodjson)

ingredients = ingredientsjson[0].value

print(ingredients)



l = ["candy"]

if any(word in ingredients for word in l):
    print(f"found a word in {l} in list of ingredients:\n{ingredients}")
else:
    print(f"Did not find word in {l} in list of ingredients:\n{ingredients}")
