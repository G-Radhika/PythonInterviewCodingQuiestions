"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""
"""
Algorithm:
1. Check if the string is not empty. If empty return.
2. check length of the string passed
3. take three temp variables longest, left and right. and initialize them to 0.
4. For the whole string subdivide the string and check f it palindrom.
5. find the longest string that is a palindrome. It'll have highest value for the variable longest.

This O(n^2)
"""


# @param {string} s input string
# @return {bool} if string is palindrome or not
def isPalindrome(s):
    if not s:
        return False
    # reverse compare
    return s == s[::-1]

# @param {string} s input string
# @return {string} the longest palindromic substring
def question2(s):
    if not s:
        return ""

    n = len(s)
    longest, left, right = 0, 0, 0
    for i in xrange(0, n):
        for j in xrange(i + 1, n + 1):
            substr = s[i:j]
            if isPalindrome(substr) and len(substr) > longest:
                longest = len(substr)
                left, right = i, j
    # construct longest substr
    result = s[left:right]
    return result
#
# Test Cases
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'question2'
  # Each line calls donuts, compares its result to the expected for that call.
  test(question2("AABCCBAC"), 'ABCCBA')
  test(question2("ABCDDCBA"), 'ABCDDCBA')
  test(question2("ABACCARA"), 'ACCA')
  test(question2("ABATC"), 'ABA')
#


if __name__ == '__main__':
    main()