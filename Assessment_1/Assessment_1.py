# Function to read CSV file
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = [v.strip() for v in line.strip().split(',')]
            data.append(dict(zip(headers, values)))
    return data

# Function to categorize employee performance
def categorize_performance(employees):
    performance_counts = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Poor': 0}
    
    for record in employees:
        try:
            sales = float(record['Sales'])
            if sales >= 100000:
                performance_counts['Excellent'] += 1
            elif sales >= 80000:
                performance_counts['Good'] += 1
            elif sales >= 60000:
                performance_counts['Average'] += 1
            else:
                performance_counts['Poor'] += 1
        except ValueError:
            continue
    
    return performance_counts

# Function to find top performer in each department
def top_performers(employees):
    top_performer_by_dept = {}
    
    for record in employees:
        try:
            sales = float(record['Sales'])
            department = record['Department']
            name = record['Name']
            
            if department not in top_performer_by_dept or sales > top_performer_by_dept[department][1]:
                top_performer_by_dept[department] = (name, sales)
        except ValueError:
            continue
    
    return top_performer_by_dept

# Main execution
input_file = 'employee_performance.csv'
data = read_csv(input_file)

# Get performance summary
performance_summary = categorize_performance(data)
print("Performance Rating Summary:")
for rating, count in performance_summary.items():
    print(f"- {rating}: {count} employees")

# Get top performers per department
top_performers_by_dept = top_performers(data)
print("\nTop Performers by Department:")
for dept, (name, sales) in top_performers_by_dept.items():
    print(f"- {dept}: {name} (RM {sales} sales)")
