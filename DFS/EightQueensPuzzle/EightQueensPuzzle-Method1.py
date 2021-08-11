class Solution:
    """
    Backtracking solution
    """

    def solveNQueens(self, n: int) -> list[list[str]]:
        def convert(col_idx, n):
            return "." * col_idx + "Q" + "." * (n - col_idx - 1)

        def dfs(i):
            """
            find positions of queen in i th index row
            """
            if i == n:
                # just gone through a valid scenario
                # add current board to the result set
                output.append(list(board))

            row_idx = i
            for col_idx in range(n):
                if (col_idx not in cols and 
                    row_idx + col_idx not in sums and 
                    row_idx - col_idx not in diffs):
                    print('tender %d' %(row_idx - col_idx))
                    cols.add(col_idx)
                    sums.add(row_idx + col_idx)
                    diffs.add(row_idx - col_idx)

                    # this might be the next valid board. Not confirmed yet.
                    board.append(convert(col_idx, n))

                    # recurse to next row
                    dfs(i + 1)

                    # if current scenario with col_idx is not valid,
                    # then backtrack
                    board.pop()
                    cols.remove(col_idx)
                    sums.remove(row_idx + col_idx)
                    diffs.remove(row_idx - col_idx)

        output = []
        board = []
        cols = set()
        sums = set()
        diffs = set()

        dfs(0)
        return output

solution = Solution
result = solution.solveNQueens(solution, 4)
print('total answer is %d' %len(result))
for answers in result:
    print(answers)