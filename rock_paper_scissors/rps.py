#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  #defining possible terms
  moves = ['rock', 'paper', 'scissors']
  #blank list that will host answer
  output = []
  #if 0, return blank nested
  if n == 0:
    return [[]]
  #if 1, return rock, paper, scissors
  if n== 1:
    return [[m] for m in moves]
  #otherwise, dedcrease by 1, and apply each of the 3 available options to the subset
  #of possibilities with recursion.
  else:
    #note!! this is recursively adding rock, paper, or scisior to a lower
    #complexity space N. Since we cover our bases and add all 3 potential
    #moves at our disposal, we are covering all possible outcomes in the
    #branching possibilities
    for x in rock_paper_scissors(n-1):
      output.append((x + [moves[0]]))
      output.append((x + [moves[1]]))
      output.append((x + [moves[2]]))
    return output

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')