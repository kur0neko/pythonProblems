def cacti_number(plot):
    #r= rows, c=colums
    r = len(plot)
    c = len(plot[0])
    count = 0
    
    #nested loop check reach r=rows
    for i in range(r):
         #nested loop check reach colums
        for j in range(c):
            #if matrice[row][column] is zero, it is empty
            if plot[i][j] == 0:
                adjacent_empty = True
                #if matrice[row][column] is not zero, it is not empty
                if i > 0 and plot[i-1][j] == 1:
                    adjacent_empty = False
                if j > 0 and plot[i][j-1] == 1:
                    adjacent_empty = False
                if i < r-1 and plot[i+1][j] == 1:
                    adjacent_empty = False
                if j < c-1 and plot[i][j+1] == 1:
                    adjacent_empty = False
                if i > 0 and j > 0 and plot[i-1][j-1] == 1:
                    adjacent_empty = False
                if i > 0 and j < c-1 and plot[i-1][j+1] == 1:
                    adjacent_empty = False
                if i < r-1 and j > 0 and plot[i+1][j-1] == 1:
                    adjacent_empty = False
                if i < c-1 and j < c-1 and plot[i+1][j+1] == 1:
                    adjacent_empty = False
                
                if adjacent_empty:
                    count += 1   
    return count

