
#read input csv.file content
data = []
with open('uni_students.csv') as f:
    lines = f.readlines()
    
#process data from 2nd line onwards
for line in lines[1:]:
    y = line.split(',')
    data = data + [[y[0],                           #student ID
                   y[1],                            #level
                   int(y[2]),                       #credit
                   float(y[3]),                     #GPA
                   y[4].strip().replace(' ', '')]]  #department

#student with academic probation
def probation_students(data):
    probation_num = 0
    for x in data:
        if x[3] < 2.0:
            probation_num += 1
    print('\nProbation Students (Total: %d students)' %(probation_num))
    for z in data:
        if z[3] < 2.0:
            print('- %s : GPA %s' %(z[0],z[3]))  
    return

#avaerage gpa for each department
def avg_dep(data):
    print('\nStudent Performance per Department:')
    cs_num = 0.0
    cs_gpa = 0.0
    ee_num = 0.0
    ee_gpa = 0.0
    me_gpa = 0.0
    me_num = 0.0
    ce_gpa = 0.0
    ce_num = 0.0
    ba_gpa = 0.0
    ba_num = 0.0
    for x in data:
        if x[4] == 'ComputerScience':
            cs_num += 1.0
            cs_gpa = cs_gpa + x[3]
        if x[4] == 'ElectricalEngineering':
            ee_num += 1.0
            ee_gpa = ee_gpa + x[3]
        if x[4] == 'MechanicalEngineering':
            me_num += 1.0
            me_gpa = me_gpa + x[3]   
        if x[4] == 'CivilEngineering':
            ce_num += 1.0
            ce_gpa = ce_gpa + x[3]   
        if x[4] == 'BusinessAdministration':
            ba_num += 1.0
            ba_gpa = ba_gpa + x[3]   
    print ('- Computer Science: Average GPA %f (%d students)' %(cs_gpa / cs_num, cs_num))
    print ('- Electrical Engineering: Average GPA %f (%d students)' %(ee_gpa / ee_num, ee_num))
    print ('- Mechanical Engineering: Average GPA %f (%d students)' %(me_gpa / me_num, me_num))
    print ('- Civil Engineering: Average GPA %f (%d students)' %(ce_gpa / ce_num, ce_num))
    print ('- Business Administration: Average GPA %f (%d students)' %(ba_gpa / ba_num, ba_num))
    return

probation_students(data)
avg_dep(data)