#!/usr/bin/python

import sys
import functools

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

@functools.lru_cache(maxsize=128)
def eating_cookies(n):
  if n < 0:
    #can't eat neative cookies
    return 0
  if n == 0:
    #if there are no cookies
    #you can only not eat them one way.
    return 1
  if n == 1:
    #1
    return 1
  elif n == 2:
    #1, 1
    #2
    return 2
  elif n == 3:
    #1, 1, 1,
    #1, 2
    #2, 1
    #3
    return 4
  else:
    return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')