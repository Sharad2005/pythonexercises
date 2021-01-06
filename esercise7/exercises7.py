data_valid=False

while data_valid==False:
    grade1= input("Please enter garde of your first exam:")
    try:
        grade1=float(grade1)
    except:
        print("The number is invalid")
        continue
    if grade1<0 or grade1>10:
        print("Grade should be b/w 0 and 10")
        continue
    else:
        data_valid=True


data_valid=False

while data_valid==False:
    grade2=input("Please enter garde of your second exam:")
    try:
        grade2=float(grade2)
    except:
        print("The number is invalid")
        continue
    if grade2<0 or grade2>10:
        print("Grade should be b/w 0 and 10")
        continue
    else:
        data_valid=True


data_valid=False

while data_valid==False:
    total_classes=input("Please enter the number of classes you have atended:")
    try:
        total_classes=int(total_classes)
    except:
        print("The number is invalid")
        continue
    if total_classes<=0:
        print("you can't enter number less than zero")
        continue
    else:
        data_valid=True
        
        
                
data_valid=False

while data_valid==False:
    absences=input("Please enter the number of classes you have abesnces:")
    try:
        absences=int(absences)
    except:
        print("The number is invalid")
        continue
    if absences < 0 or absences > total_classes:
        print("the number of absences  is invalid")
        continue
    else:
        data_valid=True


avg_grade=(grade1+grade2) /2
attentendence=(total_classes-absences) / total_classes        
print("average garde:",round(avg_grade,2))
print("attendace rate:",str(round((attentendence * 100),2))+'%')
