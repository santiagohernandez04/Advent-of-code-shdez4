


def read_input_file(file_path):
    with open(file_path) as file:
        return file.read().strip().splitlines()

def parse_lines(lines):
    left_numbers = []
    right_numbers = []
    
    for line in lines:
        parts = line.split()
        if len(parts) == 2: # Verificar que la línea tenga dos partes
            left_numbers.append(int(parts[0]))
            right_numbers.append(int(parts[1]))
    
    return left_numbers, right_numbers

def calculate_total_distance(left_numbers, right_numbers):
    left_numbers.sort()
    right_numbers.sort()
    
    total_distance = 0
    for left_num, right_num in zip(left_numbers, right_numbers): #zip junta las listas en una sola
        total_distance += abs(left_num - right_num)
    
    return total_distance

def calculate_similarity_score(left_numbers, right_numbers):
    right_counts = {} # Diccionario para contar la cantidad de veces que aparece cada número en right_numbers
    for num in right_numbers:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    similarity_score = 0
    for num in left_numbers:
        if num in right_counts:
            similarity_score += num * right_counts[num]
    
    return similarity_score

def main():
    lines = read_input_file('input.txt')
    left_numbers, right_numbers = parse_lines(lines)
    
    total_distance = calculate_total_distance(left_numbers, right_numbers)
    similarity_score = calculate_similarity_score(left_numbers, right_numbers)
    
    print("Total Distance:", total_distance)
    print("Similarity Score:", similarity_score)



main()