

student={}
 
student['malak']='05567894','malak@hotmail.com','st5567'
student['afaf']='0435667','afaf@gmail.com','st3224'
student['sara']='05334789','sara@hotmail.com','st678'
student['maha']='05338889','maha@gmail.com','st9678'
student['noha']='05308889','noha@hotmail.com','st2178'
    


option=True
while option:
    print('"Welcome to the student dictionary"')
    print("What would you like to do? ")
    print("1. print the student dictionary ")
    print("2. Search Student")
    print("3. print Count of Students ")
    print("4. Remove Student")
    print("5. Exist")

    
    option = input(">> ")
    if option =="1":
        print('\nthe student dectionry :\n',student)
    elif option == "2":
        student.keys()
        serch=input('enter the name :')
        print('information student :',student.get(serch))
        
    elif option == "3":
        print('count of students :',len(student))
    elif option == "4":
         remove=input('enter student name :')
         del(student[remove])
    else:
        print('\n"Thans for your time"\n')
        