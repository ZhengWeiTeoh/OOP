#Name: Teoh Zheng Wei
#Student ID: 2400782
#Program: 3E

#Name: Wei Hanqi
#Student ID: 2402165
#Program: 3E


#read the content of the file
data = []
with open('employee_performance.csv') as f:
    lines = f.readlines()
    
#split the content into a list
for line in lines[1:]:
    y = line.split(',')
    data = data + [[y[0],                               #employee ID
                   y[1],                                #name
                   y[2].strip().replace(' ', ''),       #department
                   int(y[3])]]                          #sales

#employee performance rating
def performance_rating(data):
    Excellent = 0 
    Good = 0
    Average = 0
    Poor = 0

    for x in data:
        if x[3] > 100000:
            Excellent += 1
        if 80000 <= x[3] < 100000:
            Good += 1
        if 60000 <= x[3] < 80000:
            Average += 1
        if x[3] < 60000:
            Poor += 1

    print(f'\nExcellent: {Excellent} employees')
    print(f'Good: {Good} employees')
    print(f'Average: {Average} employees')
    print(f'Poor: {Poor} employees')

    return

#top performers by department
def top_performance(data):
    top_performer_by_department = {}

    print('\nTop Performers by Department:')

    for x in data:
            sales = int(x[3])
            department = x[2]
            name = x[1]
            
            if department not in top_performer_by_department or sales > top_performer_by_department[department][1]:
                top_performer_by_department[department] = (name, sales)
    
    for dept, (name, sales) in top_performer_by_department.items():
        print(f"- {dept}: {name} (RM {sales} sales)")

    return

performance_rating(data)
top_performance(data)