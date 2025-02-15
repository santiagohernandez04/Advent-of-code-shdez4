def read_input_file(file_path):
    with open(file_path) as file:
        return file.read().strip().splitlines()

def parse_equation(line):
    # Separar el target y los números
    target_str, numbers_str = line.split(":")
    target = int(target_str.strip())
    numbers = [int(num) for num in numbers_str.strip().split()]
    return target, numbers

def can_evaluate_equation(target, numbers):
    
    if not numbers:
        return False

    def evaluate_recursive(index, current_value):
        if index == len(numbers): 
            return current_value == target 
        next_number = numbers[index] 
        # Probar con suma
        if evaluate_recursive(index + 1, current_value + next_number): 
            return True
        # Probar con multiplicación
        if evaluate_recursive(index + 1, current_value * next_number):
            return True
        return False

    
    return evaluate_recursive(1, numbers[0]) 

def main():
    lines = read_input_file('input7.txt')
    calibration_sum = 0  

    for line in lines:
        target, numbers = parse_equation(line)
        if can_evaluate_equation(target, numbers):
            calibration_sum += target

    print("Resultado de la calibracion:", calibration_sum) 


main()