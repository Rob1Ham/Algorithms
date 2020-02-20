#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #our kitchen is made up of keys of the ingridient field
  #if an item is in the recipe but not not ingridients, return 0.
  for ing in recipe.keys():
    if ing not in ingredients.keys():
      return 0
  #looping through each item in the ingriendents list
  batches = []
  for rec_item, rec_amount in recipe.items():
    quantity = ingredients[rec_item]//rec_amount
    batches.append(quantity)
  return(min(batches))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))