names = ["Aman", "Riya", "Rahul", "Sneha", "Karan"]
marks = [45, 38, 72, 88, 55]    

Total=0
for mark in marks:
    Total= Total+mark 

Addends=len(marks)
average=Total/Addends

print("Class average :",average)

performance_average=average-10
at_risk_marks=[]

for i in marks:
    if i < performance_average:
        at_risk_marks.append(i)

at_risk_position=[]
for i in at_risk_marks:
    at_risk_position.append(marks.index(i))

print("Students at risk :")
    
for i in at_risk_position:
    print(names[i],"(",marks[i],")")
 
above_average=[]
below_average=[]
for i in marks:
    if i > performance_average:
        above_average.append(i)
    else:
        below_average.append(i)

percentage=40/100*5

below_average_student=0

for i in range(len(below_average)):
    below_average_student = below_average_student+1
    
if below_average_student < percentage:
    print("Class performance is poor")
else:
    print("Class performance is acceptable")
