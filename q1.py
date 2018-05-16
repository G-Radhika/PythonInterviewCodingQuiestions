"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True.
Your function definition should look like: question1(s, t) and return a boolean True or False.
""" 
"""
Time complexity:

Space complexity:
"""

import itertools

def question1(s, t):
    # 1. check if t is not empty
    if len(t) == 0:
        return False
    elif len(t) == 1: # t has only one letter, so cannot make any combinations!
        return False
    elif len(t) > len(s):
        return False
    else:
        return compare(s, t)

def compare(s, t):
    # Make a set of every permutation of s and t
    t_list =  list(map("".join, itertools.permutations(t))) #t_list contains all anagrams of t
    t_set = set(t_list)
    s_list =  list(map("".join, itertools.permutations(s, len(t)))) #t_list contains all anagrams of t
    s_set = set(s_list)
    for t in t_set:
        if t in s_set:
            return True
        else:
            return False


# Simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test_anagram(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
   
# main() 
# using test_anagram() to check if each result is correct or not.
def main():
  print 'question2'
  # Each line calls donuts, compares its result to the expected for that call.
  test_anagram(question1("udacity", ''), False)     # Empty t
  test_anagram(question1("udacity", 'u'), False)    # Only one letter in t
  test_anagram(question1("udacity", 'uda'), True)  # combination is present  
  test_anagram(question1("udacity", 'uda'), True)   # combination is present
  test_anagram(question1("udacity", 'cadi'), True)   # combination is present
  test_anagram(question1("udacity", 'abc'), False)  # combination is NOT present
  test_anagram(question1("udacity", 'abcdefgh'), False)  # length of t>s

if __name__ == '__main__':
    main()