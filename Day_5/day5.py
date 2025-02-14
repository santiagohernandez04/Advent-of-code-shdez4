def read_input(file_path):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    rules = []
    updates = []
    is_rules_section = True

    for line in lines:
        line = line.strip()
        if line == "":
            is_rules_section = False
            continue
        if is_rules_section:
            rules.append(line)
        else:
            updates.append(line.split(','))

    return rules, updates

def is_update_valid(update, rules):
    update_set = set(update)

    # Verificar cada regla
    for rule in rules:
        x, y = rule.split('|')
        if x in update_set and y in update_set:
            # Verificar si x está antes que y en la actualización
            if update.index(x) > update.index(y):
                return False
    return True

def get_middle_page(update):
    middle_index = len(update) // 2 #Obtener el índice del número de página del medio
    return int(update[middle_index]) 

def main():
    file_path = 'input5.txt'  
    rules, updates = read_input(file_path)

    total = 0

    # Verificar cada actualización
    for update in updates:
        if is_update_valid(update, rules):
            middle_page = get_middle_page(update)
            total += middle_page

    print(f"La suma de los números de página del medio es: {total}")


main()