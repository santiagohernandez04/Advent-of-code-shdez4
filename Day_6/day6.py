def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def find_guard_position(map_data):

    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] in ['^', 'v', '<', '>']:
                direction = map_data[i][j]
                return (i, j), direction
    return None, None

def move_guard(map_data):
    
    # Encontrar la posición y dirección inicial del guardia
    (row, col), direction = find_guard_position(map_data)
    if direction is None:
        return 0

    # Definir las direcciones: arriba, derecha, abajo, izquierda
    directions = ['^', '>', 'v', '<']
    moves = {
        '^': (-1, 0),  # Arriba
        '>': (0, 1),   # Derecha
        'v': (1, 0),   # Abajo
        '<': (0, -1)   # Izquierda
    }

    # Inicializar el conjunto de posiciones visitadas
    visited = set()
    visited.add((row, col))

    while True:
        # Obtener el movimiento actual
        dr, dc = moves[direction]

        # Calcular la nueva posición
        new_row, new_col = row + dr, col + dc

        # Verificar si la nueva posición está fuera del mapa
        if new_row < 0 or new_row >= len(map_data) or new_col < 0 or new_col >= len(map_data[0]):
            break

        # Verificar si hay un obstáculo en la nueva posición
        if map_data[new_row][new_col] == '#':
            # Girar 90 grados a la derecha
            current_index = directions.index(direction)
            direction = directions[(current_index + 1) % 4] 
        else:
            # Mover al guardia
            row, col = new_row, new_col
            visited.add((row, col))

    return len(visited)

def main():
    file_path = 'input6.txt'
    map_data = read_map(file_path)
    distinct_positions = move_guard(map_data)
    print(f"El guardia visita {distinct_positions} posiciones distintas antes de salir del área.")


main()