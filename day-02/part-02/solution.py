with open('./input.txt', "r") as file:
    content = file.read()
    
def parseInput(input):
    lines = input.strip().split('\n')
    a, b = [], []

    for line in lines:
        left, right = line.split()
        a.append(left)
        b.append(right)

    return a, b

def calculate_similarity(input):
  a, b = parseInput(input)
  similarity_count = 0

  for i in range(len(a)):
    duplicate_count = 0
    for j in range(len(b)):
      if a[i] == b[j]:
        duplicate_count += 1
    similarity_count += int(a[i]) * duplicate_count

  return similarity_count

if __name__ == "__main__":
    result = calculate_similarity(content)
    print(result)