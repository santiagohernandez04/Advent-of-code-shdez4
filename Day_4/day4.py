def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(line.strip()) for line in file]
    return matrix

def count_xmas_occurrences(matrix, word):

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    word_length = len(word)
    count = 0

    directions = [
        (1, 0),   # Vertical hacia abajo
        (0, 1),   # Horizontal hacia la derecha
        (1, 1),   # Diagonal hacia abajo y derecha
        (1, -1),  # Diagonal hacia abajo y izquierda
        (-1, 0),  # Vertical hacia arriba
        (0, -1),  # Horizontal hacia la izquierda
        (-1, 1), # Diagonal hacia arriba y derecha
        (-1, -1)  # Diagonal hacia arriba y izquierda
    ]
    def is_word_present(x, y, dx, dy):
        
        for i in range(1, word_length):
            x += dx
            y += dy
            if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] != word[i]: # Si se sale de los límites o no coincide la letra
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[0]: # Si la letra actual es la primera de la palabra
                for dx, dy in directions: # Verificar en todas las direcciones
                    if is_word_present(i, j, dx, dy):
                        count += 1
    return count



def count_xmas_occurrences2(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    count = 0

    # Definir las direcciones para formar una "X"
    directions = [
        (1, 1),   # Diagonal hacia abajo y derecha
        (1, -1),  # Diagonal hacia abajo y izquierda
        (-1, 1),  # Diagonal hacia arriba y derecha
        (-1, -1)  # Diagonal hacia arriba y izquierda
    ]

    def is_mas_or_sam(a, b, c):
        return (a == 'M' and b == 'A' and c == 'S') or (a == 'S' and b == 'A' and c == 'M')

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'A':  # El centro de la "X" debe ser 'A'
                valid = True
                for dx, dy in directions:
                    x1, y1 = i + dx, j + dy
                    x2, y2 = i - dx, j - dy
                    if (0 <= x1 < rows and 0 <= y1 < cols and
                        0 <= x2 < rows and 0 <= y2 < cols):
                        # Verificar si las letras forman "MAS" o "SAM"
                        if not is_mas_or_sam(matrix[x1][y1], matrix[i][j], matrix[x2][y2]):
                            valid = False
                            break
                    else:
                        valid = False
                        break
                if valid:
                    count += 1
    return count



def main():
    file_path = 'input4.txt'
    word = "XMAS"
    matrix = read_matrix(file_path)
    
    
    occurrences_xmas = count_xmas_occurrences(matrix, word)
    print(f"La palabra '{word}' aparece {occurrences_xmas} veces en la matriz.")

    occurrences_xmas = count_xmas_occurrences2(matrix)
    print(f"Parte 2 {occurrences_xmas} veces en la matriz.")


    

main()