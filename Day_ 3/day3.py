import re 

def find_multiplications_part_1(corrupted_memory):
    
    # Expresión regular para encontrar instrucciones mul(X,Y) válidas
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Buscar todas las coincidencias en la cadena de memoria corrupta
    matches = re.findall(pattern, corrupted_memory)
    
    # Calcular la suma de los resultados de las multiplicaciones
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

def find_multiplications_part_2(corrupted_memory):
    
    #Encuentra todas las instrucciones en la memoria corrupta, considerando las instrucciones do() y don't()
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Buscar todas las coincidencias en la cadena de memoria corrupta
    mul_matches = re.findall(mul_pattern, corrupted_memory)
    do_matches = re.finditer(do_pattern, corrupted_memory)
    dont_matches = re.finditer(dont_pattern, corrupted_memory)
    
    
    multiplications_enabled = True
    total_sum = 0
    mul_index = 0
    
    
    for i in range(len(corrupted_memory)):
        # Verificar si hay una instrucción do() o don't() en la posición actual
        if re.match(do_pattern, corrupted_memory[i:]):
            multiplications_enabled = True
        elif re.match(dont_pattern, corrupted_memory[i:]):
            multiplications_enabled = False
        
        # Verificar si hay una instrucción mul(X,Y) en la posición actual
        if re.match(mul_pattern, corrupted_memory[i:]):
            x, y = mul_matches[mul_index]
            if multiplications_enabled:
                total_sum += int(x) * int(y)
            mul_index += 1
    
    return total_sum

def read_input_file(file_path):
   
    with open(file_path) as file:
        return file.read().strip()

def main():
    corrupted_memory = read_input_file('input3.txt')
    
    result_part_1 = find_multiplications_part_1(corrupted_memory)
    result_part_2 = find_multiplications_part_2(corrupted_memory)
    
    print(f"Parte 1: La suma de los resultados de las multiplicaciones es: {result_part_1}")
    print(f"Parte 2: La suma de los resultados de las multiplicaciones habilitadas es: {result_part_2}")


main()