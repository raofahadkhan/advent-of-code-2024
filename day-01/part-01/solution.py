with open ('./input.txt', 'r') as file:
    content = file.read()

def parseInput(input):
    lines = input.strip().split('\n')
    a, b = [], []

    for line in lines:
        left, right = line.split()
        a.append(left)
        b.append(right)

    return a, b

def sort(arr):
    if len(arr) <= 1:
        return [int(arr[0])]

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = sort(left_half)
    right_sorted = sort(right_half)

    sorted_arr = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            sorted_arr.append(left_sorted[i])
            i += 1
        else:
            sorted_arr.append(right_sorted[j])
            j += 1

    while i < len(left_sorted):
        sorted_arr.append(left_sorted[i])
        i += 1

    while j < len(right_sorted):
        sorted_arr.append(right_sorted[j])
        j += 1

    return sorted_arr


def calculate_difference(a, b):
    i = 0
    sum_diff = 0
    while i < len(a):
        sum_diff += abs(a[i] - b[i])
        i += 1
    return sum_diff

def solution(input_str):
    left, right  = parseInput(input_str)
    sorted_left = sort(left)
    sorted_right = sort(right)
    return calculate_difference(sorted_left, sorted_right)

res = solution(content)
print(res)
    