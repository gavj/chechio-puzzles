def count_neighbours(grid, row, col):
    countVal = 0

    if row-1>=0 and col-1>=0 and grid[row-1][col-1] :
        countVal += 1; ###print countVal,'A'
    if row-1>=0 and grid[row-1][col] == 1:
        countVal += 1; ##print countVal,'B'
    if row-1>=0  and col+1<len(grid[0]) and grid[row-1][col+1] == 1 :
        countVal += 1; ##print countVal,'C'
    if col-1>=0 and grid[row][col-1] == 1:
        countVal += 1; ##print countVal,'D'
    if col+1<len(grid[0]) and grid[row][col+1] == 1   :
        countVal += 1; ##print countVal,'E'
    if row+1<len(grid) and col-1>=0 and grid[row+1][col-1] == 1  :
        countVal += 1; ##print countVal,'F'
    if row+1<len(grid) and grid[row+1][col] == 1 :
        countVal += 1; ##print countVal,'G'
    if row+1<len(grid)    and col+1<len(grid[0]) and grid[row+1][col+1] == 1  :
        countVal += 1; ##print countVal,'H'
        
    return countVal
