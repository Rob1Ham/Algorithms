#!/usr/bin/python

import sys
import functools

#@functools.lru_cache(maxsize=128)
def making_change(amount, denominations):
  #if the amount is negative or 0, return 1
  if amount <=0:
    return 1
  #need to create a reference for all possible ways to make change
  #done at length of amount+1 since range indexes at 0 to start
  possibilities = [0 for x in range(amount+1)]
  #there is 1 way to make change of 0, which is once.
  possibilities[0] = 1
  #then, a loop is done across all possible denomination types
  for i in range(0, len(denominations)):
    #within each denomination, a loop is done between that denomination's value and the total amount of change
      for j in range(denominations[i], amount+1):
        #for each value that falls within the possibilities table
        #it is incrimented by the possibilities at that cell, minus the value of that denominated currency.
        #this looks recursively backwards to how much is solveable for a given amount of coins, but to an amount previously computed
        #of the total amount - removing that denomination of coins.
        possibilities[j] += possibilities[j-denominations[i]]
  return possibilities[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")