with open ('./input.txt', 'r') as file:
    content = file.read()
    
def parseInput(input):
    reports = input.strip().split('\n')
    parsed_reports = []
    
    for report in reports:
        parsed_report = report.split()
        numbers = []
        for i in range(len(parsed_report)):
            numbers.append(int(parsed_report[i]))
        parsed_reports.append(numbers)
        
    return parsed_reports

def is_report_safe(report):
    # Calculate difference between consecutive levels
    differences = []
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i + 1])
        differences.append(difference)
        
    # Check if all differences are in the range [1, 3]
    for diff in differences:
        if diff < 1 or diff > 3:
            return False
        
    # Check if the levels are strictly increasing
    increasing = True
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            increasing = False
            break 
        
    # Check if the levels are strictly decreasing
    decreasing = True
    for i in range(len(report) - 1):
        if report[i] <= report[i + 1]:
            decreasing = False
            break
        
    return increasing or decreasing

def count_safe_reports(reports):
    safe_report_count = 0
    for report in reports:
        if is_report_safe(report):
            safe_report_count += 1
    return safe_report_count

def solution(input):
    parsed_reports = parseInput(input)
    print(parsed_reports)
    safe_reports_count = count_safe_reports(parsed_reports)
    print("The count of safe reports are: ", safe_reports_count)
         


if __name__ == "__main__":
    solution(content)