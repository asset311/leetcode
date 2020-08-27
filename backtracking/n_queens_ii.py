
'''

Pseudocode:

def backtrack(row=0, count=0):
    for col in range(n):
        # iterate through all columns on the current row
        if is_not_under_attack(row, col):
            # choose this placement candidate, and mark out attacking zones
            place_queen(row, col)
            if row + 1 == n:
                # we reached the bottom, found the solution
                count += 1
            else:
                # move the next row
                backtrack(row+1, count)
            # backtrack, i.e. remove the queen and the attacking zone
            remove_queen(row, col)
    return count

'''

# There can be only one queen on a row and only one queen in a column
# So we iterate over columns

# main algorithm
class Solution:
    def totalNQueens(self, n):
        def is_not_under_attack(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col])
        
        def place_queen(row, col):
            rows[col] = 1
            hills[row - col] = 1  # "hill" diagonals
            dales[row + col] = 1  # "dale" diagonals
        
        def remove_queen(row, col):
            rows[col] = 0
            hills[row - col] = 0  # "hill" diagonals
            dales[row + col] = 0  # "dale" diagonals
        
        def backtrack(row = 0, count = 0):
            if row == n:
                count += 1
                return count

            for col in range(n):
                # iterate through all columns on the current row
                if is_not_under_attack(row, col):
                    # choose this placement candidate, and mark out attacking zones
                    place_queen(row, col)
                    #if row + 1 == n:
                    #    count += 1
                    #else:
                    count = backtrack(row + 1, count)
                    # backtrack, i.e. remove the queen and the attacking zone
                    remove_queen(row, col)
            return count
        
        rows = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        return backtrack()