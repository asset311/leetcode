

# Approach 1: Two-pass solution 
# When traversing left to right, number of open parentheses has to be greater or equal to close parentheses
# When traversing right to left, vice versa
def minRemoveToMakeValid(s: str) -> str:
    open_counter = 0
    close_counter = 0
    res = []

    for c in s:
        if c == '(':
            res.append(c)
            open_counter += 1
        elif c == ')':
            if close_counter+1 > open_counter:
                continue
            else:
                close_counter += 1
                res.append(c)
        else:
            res.append(c)

    open_counter = 0
    close_counter = 0
    res2 = []

    for i in range(len(res)-1, -1, -1):
        c = res[i]
        if c == ')':
            res2.append(c)
            close_counter += 1
        elif c == '(':
            if open_counter + 1 > close_counter:
                continue
            else:
                open_counter += 1
                res2.append(c)
        else:
            res2.append(c)

    return ''.join(res2[::-1])

    # Approach 2: One pass with string builder
    # Based on a principle of balanced parentheses
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack: #stack empty, no corresponding opening bracket
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack)) # we maintain a set, because it is O(1) lookup
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)