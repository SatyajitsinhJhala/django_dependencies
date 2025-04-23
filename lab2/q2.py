def student_details():
    num=int(input("Enter number of students: "))
    student=[]
    for i in range (num):
        name=input("Enter student name:")
        addr=input("Enter address ")
        rollno=input("Enter rollno")
        dept=input("Enter department")
        mark1=int(input("Enter marks 1"))
        mark2=int(input("Enter marks 2"))
        mark3=int(input("Enter marks 3"))
        total=mark1+mark2+mark3
        percentage=total/150*100
        student.append([name,addr,rollno,dept,total,percentage])
    for s in student:
        print("Name:",s[0])
        print("total:",s[4])

    max_marks=max(student,key=lambda s:s[4])
    min_marks=min(student,key=lambda s:s[4])
    s_failed=[]
    for s in student:
        if(s[4]<40):
            s_failed.append(s[0])
    
student_details()