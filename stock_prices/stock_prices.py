#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #initialize base cases
  current_min_price_so_far = float('inf')
  max_profit_so_far = float('-inf')
  
  #loop through all prices except for last day
  #(cant buy AND sell on last day)
  for i in range(0, len(prices)-1):
    #check if this value is the lowest price seen so far
    if prices[i] < current_min_price_so_far:
      #if its the lowest price seen so far, assign it
      #since max profit will never occur on lowest price
      #if this case is met we can go to next loop in logic
      current_min_price_so_far = prices[i]
      lowest_day_index = i
    for j in range(i+1,len(prices)):
      trade_profit = prices[j] - prices[i]
      if trade_profit > max_profit_so_far:
        max_profit_so_far = trade_profit
  return max_profit_so_far
    
    

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))