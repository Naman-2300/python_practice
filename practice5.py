R = int(input("Enter the rows: "))
C = int(input("Enter the columns: "))
 
sudoku = []
print("Enter the entries: ")
for i in range(R):         
    a =[]
    for j in range(C):     
         a.append(int(input()))
    sudoku.append(a)

for i in range(R):
    for j in range(C):
        print(sudoku[i][j], end = " ")
    print()