def is_safe(levels):
    
    #Verifica si los niveles son seguros, es decir, si son estrictamente crecientes o decrecientes,
    # y si las diferencias entre niveles adyacentes están entre 1 y 3.
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    # Si no es ni creciente ni decreciente, no es seguro
    if not (is_increasing or is_decreasing):
        return False
    
    # Verificar que las diferencias entre niveles adyacentes estén entre 1 y 3
    for i in range(len(levels) - 1):
        difference = abs(levels[i] - levels[i + 1])
        if difference < 1 or difference > 3:
            return False
    
    # REtorna si es seguro
    return True

def is_safe_with_dampener(levels):
    #Verifica si los niveles pueden volverse seguros eliminando un solo nivel.

    if is_safe(levels):
        return True
    
    # Intentar eliminar un nivel y verificar si se vuelve seguro
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    
    # No es seguro
    return False

def read_input_file(file_path):
    
    with open(file_path) as file:
        return [list(map(int, line.split())) for line in file.read().strip().splitlines()]

def main():
  
    reports = read_input_file('input2.txt')
    
    safe_count_part_1 = 0
    safe_count_part_2 = 0
    
    for report in reports:
        if is_safe(report):
            safe_count_part_1 += 1
        if is_safe_with_dampener(report):
            safe_count_part_2 += 1
    
    print(f"Parte 1: El número de informes seguros es: {safe_count_part_1}")
    print(f"Parte 2: El número de informes seguros es: {safe_count_part_2}")


main()