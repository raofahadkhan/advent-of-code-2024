import re
    
with open ('./input.txt', 'r') as file:
    corrupted_memory = file.read()

def sum_mul_results(corrupted_memory: str) -> int:
    # Define a regex pattern for valid `mul(X,Y)` instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate the sum of all valid multiplication results
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

if __name__ == "__main__":
    # Calculate the result
    result = sum_mul_results(corrupted_memory)
    print(f"Sum of all valid `mul` results: {result}")  