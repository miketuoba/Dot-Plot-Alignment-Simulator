def generateMatrix(seq1_size, seq2_size):
    matrix = []
    for i in range(0, seq2_size):
        matrix.append([])
        for j in range(0, seq1_size):
            matrix[i].append(" ")
    return matrix;

def printMatrix(matrix, seq1, seq2):
    print(" ", end = "")
    for k in range(len(seq1)):
        print("|", end="")
        print(seq1[k], end="")
    print("|")
    
    for i in range (len(matrix)):
        print(seq2[i], end = "")
        print("|", end="")
        for j in range (len(matrix[i])):
            print(matrix[i][j], end = "|")
        print()
        
def dot_plot(matrix, seq1, seq2):
    for i in range(len(seq2)):
        for j in range(len(seq1)):
            if seq2[i] == seq1[j]:
                matrix[i][j] = u"\u2022"
    return matrix

best_route = {}
coordinate = []
def scoring_matrix(matrix, sum, row, col):
    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        if matrix[row][col] == u"\u2022":
            coordinate.append((row, col))
            best_route[sum + 1] = coordinate
            return sum + 1
        else:
            coordinate.append((row, col))
            best_route[sum - 1] = coordinate
            return sum - 1
    elif row == len(matrix) - 1:
        if matrix[row][col] == u"\u2022":
            coordinate.append((row, col))
            return scoring_matrix(matrix, sum, row, col + 1)
        elif matrix[row][col] != u"\u2022":
            coordinate.append((row, col))
            return scoring_matrix(matrix, sum - 2, row, col + 1)
    elif col == len(matrix[0]) - 1:
        if matrix[row][col] == u"\u2022":
            coordinate.append((row, col))
            return scoring_matrix(matrix, sum, row + 1, col)
        elif matrix[row][col] != u"\u2022":
            coordinate.append((row, col))
            return scoring_matrix(matrix, sum - 2, row + 1, col)
    else:
        if matrix[row][col] == u"\u2022":
            coordinate.append((row, col))
            return max(scoring_matrix(matrix, sum, row + 1, col), scoring_matrix(matrix, sum, row, col + 1), scoring_matrix(matrix, sum + 1, row + 1, col + 1))
        elif matrix[row][col] != u"\u2022":
            coordinate.append((row, col))
            return max(scoring_matrix(matrix, sum - 2, row + 1, col), scoring_matrix(matrix, sum - 2, row, col + 1), scoring_matrix(matrix, sum - 1, row + 1, col + 1))

def scoring(matrix):
    return scoring_matrix(matrix, 0, 0, 0)
        
if __name__ == "__main__" :
    seq1 = "ATT"
    seq2 = "ATC"
    matrix = generateMatrix(len(seq1), len(seq2))
    dot_plot(matrix, seq1, seq2)
    print("The highest alignment score is", scoring(matrix))
    printMatrix(matrix, seq1, seq2)
    print(coordinate)
    print(best_route)
