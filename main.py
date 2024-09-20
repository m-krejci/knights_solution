# Returns the number of lonely knights on a square chessboard. 
# A knight is lonely if no square within a knight's move is occupied by another knight.
def lonely_knights(self, m: list[list[int]]) -> int:
    # TODO: Implement the solution
    lonely = 0
    occ = 0
    row_len = len(m[lonely])
    col_len = len(m)
    for row in range(row_len):
        for col in range(col_len):
            if m[row][col] == 0:
                continue
            else:
                lonely += 1
                # 1
                if (row-2 >= 0 and row-2 <= row_len-1) and (col-1 >= 0 and col-1 <= col_len-1):
                    if m[row-2][col-1] == 1:
                        occ += 1
                        continue
                # 2
                if (row-2 >= 0 and row-2 <= row_len-1) and (col+1 >= 0 and col+1 <= col_len-1):
                    if m[row-2][col+1] == 1:
                        occ += 1
                        continue
                # 3
                if (row-1 >= 0 and row-1 <= row_len-1) and (col-2 >= 0 and col-2 <= col_len-1):
                    if m[row-1][col-2] == 1:
                        occ += 1
                        continue
                # 4
                if (row-1 >= 0 and row-1 <= row_len-1) and (col+2 >= 0 and col+2 <= col_len-1):
                    if m[row-1][col+2] == 1:
                        occ += 1
                        continue
                # 5
                if (row+1 >= 0 and row+1 <= row_len-1) and (col-2 >= 0 and col-2 <= col_len-1):
                    if m[row+1][col-2] == 1:
                        occ += 1
                        continue
                # 6
                if (row+1 >= 0 and row+1 <= row_len-1) and (col+2 >= 0 and col+2 <= col_len-1):
                    if m[row+1][col+2] == 1:
                        occ += 1
                        continue
                # 7
                if (row+2 >= 0 and row+2 <= row_len-1) and (col-1 >= 0 and col-1 <= col_len-1):
                    if m[row+2][col-1] == 1:
                        occ += 1
                        continue
                # 8
                if (row+2 >= 0 and row+2 <= row_len-1) and (col+1 >= 0 and col+1 <= col_len-1):
                    if m[row+2][col+1] == 1:
                        occ += 1
                        continue
    return lonely-occ
