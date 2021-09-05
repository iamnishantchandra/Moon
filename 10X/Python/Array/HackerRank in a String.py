'''
HackerRank in a String!
 link- https://www.hackerrank.com/contests/10x-01-09-2021/challenges/hackerrank-in-a-string/problem
We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. Remeber that a subsequence maintains the order of characters selected from a sequence.

More formally, let  be the respective indices of h, a, c, k, e, r, r, a, n, k in string . If  is true, then  contains hackerrank.

For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.

Example

This contains a subsequence of all of the characters in the proper order. Answer YES


This is missing the second 'r'. Answer NO.


There is no 'c' after the first occurrence of an 'a', so answer NO.

Function Description

Complete the hackerrankInString function in the editor below.

hackerrankInString has the following parameter(s):

string s: a string
Returns

string: YES or NO
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a single query string .

Constraints

Sample Input 0

2
hereiamstackerrank
hackerworld
Sample Output 0

YES
NO
Explanation 0

We perform the following  queries:


The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we return YES.
 does not contain the last three characters of hackerrank, so we return NO.
Sample Input 1

2
hhaacckkekraraannk
rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt
Sample Output 1

YES
NO
'''


import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s):
    # Write your code here
    s=s
    st="hackerrank"
    stri=""
    j=0
    i=0 
    while(j<(len(st)) and i<len(s)):  
        if st[j]==s[i]:
            j=j+1
            stri+=s[i]
        i=i+1
    if stri==st:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
    '''
    
    import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s):
    # Write your code here
    st="hackerrank"
    stri=""
    
    j=1
    for i in range(len(s)):
        
        if st[j-1]==s[i] and j<len(st):
            j+=1
            stri+=s[i-1]
        else:
            pass
    if stri==st:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
    '''