import re

with open ('./input.txt', 'r') as file:
    corrupted_memory = file.read()

def sum_enabled_mul_results(corrupted_memory):
    # Regex patterns for mul(), do(), and don't()
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    # Initialize state
    mul_enabled = True
    total_sum = 0

    # Scan through the memory sequentially
    instructions = re.finditer(f"{mul_pattern}|{do_pattern}|{dont_pattern}", corrupted_memory)
    for instruction in instructions:
        match = instruction.group()
        
        if re.fullmatch(do_pattern, match):
            mul_enabled = True
        elif re.fullmatch(dont_pattern, match):
            mul_enabled = False
        elif mul_enabled and re.fullmatch(mul_pattern, match):
            # Extract numbers and compute the product
            x, y = map(int, re.match(mul_pattern, match).groups())
            total_sum += x * y
    
    return total_sum
         
if __name__ == "__main__":
    result = sum_enabled_mul_results(corrupted_memory)
    print(f"Sum of enabled `mul` results: {result}")