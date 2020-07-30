
'''
This presents a general template for approaching backtracking problems.
As an exposition we choose to solve the following problem:
Palidrome Partitioning (https://leetcode.com/problems/palindrome-partitioning/)

All backtracking problems are composed by three steps: choose, explore, unchoose.
For each problem you need to know:
1. Choose what? 
    - choose each substring
2. How to explore?
    - do the same thing for the remaining string
3. Unchoose
    - do the opposite of operation of choose.

In this example.
1. Define helper(): Usually we need a helper function to accept more parameters.
2. Parameters: Usually we need the following parameters.
    - The object you are working on. For this problem it is a string 's'.
    - A start index or end index, to indicate which part you are working on. For this problem we choose substring to indicate the start index.
    - A step result to remember the current 'choose' and then do 'unchoose': For this problem we choose List[str] step.
    - A final result, to store the final result: usually we just add to that result (could be a list, could be a set)

3. Base case:
    - indicates when to add step into the result, and when to return
4. Iteration, for-loop:
    - usually we need a loop to iterate over the input to 'choose', so that we can choose all options.
5. Choose:
    - in this problem, if the substring of 's' is a palindrome, we add it into the step, which means we choose this substring.
    - we usually define a separate function to test the choice, in this case we test for palindrome.
6. Explore:
    - in this problem, we want to do the same thing to the remaining substring. So we recursively call our function.
7. Unchoose:
    - we draw back, remove the chosen substring, in order to try other options.
'''

from typing import List
def partition(s: str) -> List[List[str]]:
    # edge case
    if not s:
        return []
    
    # initial call to backtraking, using a helper
    result = [] 
    step = []
    helper(s, step, result)
    return result


def helper(s:str, step:List[str], result: List[List[str]]) -> None:
    # base case
    if len(s) == 0:
        print(f'adding to result: {step}')
        result.append(step[:])  # need to create a new list, as this will be backtracked
        return
    
    # start a loop to choose a step
    for i in range(1,len(s)+1):
        substring = s[:i]
        #print(f'next substring:{substring}')
        
        if isPalindrome(substring):
            print(f'next candidate:{substring}')
            step.append(substring)   # choose
            helper(s[i:], step, result) # explore via recursive call
            print(f'backtracking from {substring}')
            step.pop()          # unchoose
    return


# standard function to check if a string is a palindrome
def isPalindrome(s:str) -> bool:
    left, right = 0, len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
