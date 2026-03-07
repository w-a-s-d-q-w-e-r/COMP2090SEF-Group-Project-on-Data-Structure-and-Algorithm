def create_matrix():
    rows = int(input("Enter number of rows: "))         # user input for number of rows
    col = int(input("Enter number of columns: "))       # user input for number of columns

    matrix = []                                         # creating an empty matrix
    print("Entries row-wise:")                          # tell user the matrix is in row-wise

    number = 1                                          # initial number to be added in the matrix

    for i in range(rows):                               # loop for rows
        row = []                                        # creating a new row
        for j in range(col):
            row.append(number)                          # input number to the row
            number = number + 1              
        matrix.append(row)                              # adding rows to the matrix

    print("\n2D matrix is:")

    for i in range(rows):
        for j in range(col):
            print(matrix[i][j], end=" ")                # print the matrix in 2D format
        print()     
        
    return matrix


def return_matrix(matrix):
    print("\n2D matrix is:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")                # print the matrix in 2D format


def change_matrix_value(matrix,row,col,value):
    if row >= len(matrix) or col >= len(matrix[0]):
        print("Invalid row or column index.")
        print("No value in matrix is changed")
        pass
    else:
        matrix[row][col] = value
        print("\n2D matrix after update is:")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")            # print the matrix in 2D format
            print()
    return matrix
