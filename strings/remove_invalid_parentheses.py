
from collections import deque
from typing import List

def removeInvalidParentheses(self, s: str) -> List[str]:

    # helper to check if the expression is valid
    def isValid(expr):
        count = 0
        for ch in expr:
            if ch not in '()':
                continue
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    if len(s) == 0:
        return [""]

    # queue holds expressions to evaluate
    queue = deque()
    # holds expressions that were evaluated
    visited = set()

    queue.append(s)
    visited.add(s)

    found = False   # all optimal solutions will be found on the same level
    output = []

    while queue:
        expr = queue.popleft()

        if isValid(expr):
            output.append(expr)
            found = True
        
        # no need to check by removing more, as we found on this level
        if found:
            continue

        for i in range(len(expr)):
            if expr[i] not in '()':
                continue

            candidate = expr[:i] + expr[i+1:]   #remove one parentheses
            if candidate not in visited:
                queue.append(candidate)
                visited.add(candidate)
    
    return output if output else [""]
