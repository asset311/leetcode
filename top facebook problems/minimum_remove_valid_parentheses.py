

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