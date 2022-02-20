# PROJECT MODULE 1 -- PURWADHIKA JCDS VL
# Code Written by: AZHAR ADITYA RAHMAN (JCDSVL-005-011)
# ASSIGNMENT: ACADEMIC SCORES (Student Score Data Program)

def dataNotFound():
    print('!!! ALERT: Option/data not available !!!\n')
def updated():
    print('SUCCESS: Data has been updated!\n')
def cancel():
    print('CANCEL: Last action to update has been cancelled!\n')

stud = [{'ID': 100, 'Name': 'Andi', 'Sex': 'M', 'Origin': 'Bandung', 'Grade': 'A'},
{'ID': 101, 'Name': 'Bella', 'Sex': 'F', 'Origin': 'Jakarta', 'Grade': 'B+'},
{'ID': 102, 'Name': 'Ciko', 'Sex': 'M', 'Origin': 'Jakarta', 'Grade': 'C+'}]

def prog():
    while True:
        main = input('''
==========ACADEMIC SCORES==========
====STUDENTS SCORE DATA PROGRAM====

MAIN MENU
1. REPORT Student Data
2. ADD Student Data
3. EDIT Student Data
4. DELETE Student Data
5. EXIT Program

Please Input Your Choice Here [1-5]:''')

        while (main == '1'):
            print ('\n-----REPORT STUDENT DATA-----')
            sub1 = int(input('''
    1. Report All Student Data
    2. Report A Student Data
    3. Return to Main Menu
    
    Please Input Your Choice Here [1-3]:'''))

            if (sub1==1):
                if (len(stud)==0):
                    dataNotFound()
                else:
                    print ('~~~~STUDENT DATA~~~~')
                    print('ID\t\t| Name\t\t| Sex\t\t| Origin\t\t| Grade')
                    for j, i in enumerate(stud):
                        print(f"{i['ID']}\t\t| {i['Name']}\t\t| {i['Sex']}\t\t| {i['Origin']}\t\t| {i['Grade']}")

            elif (sub1==2):
                if (len(stud)==0):
                    dataNotFound()
                else:
                    while True:
                        studID = int(input('Please Input Student ID: '))
                        for j, i in enumerate(stud):
                            if studID == i['ID']:
                                print (f'~~~~STUDENT DATA FOR ID {studID}~~~~')
                                print('ID\t\t| Name\t\t| Sex\t\t| Origin\t\t| Grade')
                                print(f"{i['ID']}\t\t| {i['Name']}\t\t| {i['Sex']}\t\t| {i['Origin']}\t\t| {i['Grade']}")
                                break
                        else:
                            dataNotFound()
                        break      

            elif (sub1==3):
                break
            
            else:
                dataNotFound()
        
        while (main=='2'):
            print ('-----ADD STUDENT DATA-----')
            sub2 = int(input('''
    1. Add Student Data
    2. Return to Main Menu
    
    Please Input Your Choice Here [1-2]:'''))

            if (sub2==1):
                print ('~~~~ADD STUDENT DATA~~~~')
                while True:
                    idNew = int(input('Please Input Student ID: '))
                    for j, i in enumerate(stud):
                        if idNew == i['ID']:
                            print('ALERT! Student ID already taken!\n')
                            break
                    else:
                        nameNew = input ('Please input student name  : ')
                        sexNew = input  ('Please input student sex   : ')
                        oriNew = input  ('Please input student origin: ')
                        gradeNew = input  ('Please input student grade  : ')
                        newStud = {'ID': idNew, 'Name': nameNew, 'Sex': sexNew, 'Origin': oriNew, 'Grade': gradeNew}
                        while True:
                            decision=input('Are you sure you want to update the data [Y/N]: ')
                            if (decision == 'Y'):
                                stud.append(newStud)
                                updated()
                                break
                            elif (decision == 'N'):
                                cancel()
                                break
                            else:
                                dataNotFound()
                    break

            elif (sub2==2):
                break

            else:
                dataNotFound()
        
        while (main=='3'):
            print ('-----EDIT STUDENT DATA-----')
            sub3 = int(input('''
    1. Edit Student Data
    2. Return to Main Menu
    
    Please Input Your Choice Here [1-2]:'''))

            if (sub3==1):
                print ('~~~~EDIT STUDENT DATA~~~~')
                while True:
                    idEdit = int(input('Please Input Student ID: '))
                    for j, i in enumerate(stud):
                        if idEdit == i['ID']:
                            print ('~~~~STUDENT DATA FOR EDITING~~~~')
                            print('ID\t\t| Name\t\t| Sex\t\t| Origin\t\t| Grade')
                            print(f"{i['ID']}\t\t| {i['Name']}\t\t| {i['Sex']}\t\t| {i['Origin']}\t\t| {i['Grade']}")
                            while True:
                                decision=input('Are you sure you want to update the data [Y/N]: ')
                                if (decision == 'Y'):
                                    keyEdit = input('Please Input the Parameter You Want to Change: ')
                                    valEdit = input(f'Please input the new {keyEdit} value for ID {idEdit}: ')
                                    dicEDIT = {keyEdit: valEdit}
                                    while True:
                                        decision=input('Are you sure you want to update the data [Y/N]: ')
                                        if (decision == 'Y'):
                                            i.update(dicEDIT)
                                            updated()
                                            break
                                        elif (decision == 'N'):
                                            cancel()
                                            break
                                        else:
                                            dataNotFound()
                                    break
                                elif (decision == 'N'):
                                    cancel()
                                    break
                                else:
                                    dataNotFound()
                            break
                    else:
                        dataNotFound()                     
                    break   
                
            elif (sub3==2):
                break

            else:
                dataNotFound()
        
        while (main=='4'):
            print ('-----DELETE STUDENT DATA-----')
            sub4 = int(input('''
    1. Delete Student Data
    2. Return to Main Menu
    
    Please Input Your Choice Here [1-2]:'''))

            if (sub4==1):
                print ('~~~~DELETE STUDENT DATA~~~~')
                while True:
                    idDel = int(input('Please Input Student ID: '))
                    for j, i in enumerate(stud):
                        if idDel == i['ID']:
                            while True:
                                decision=input('Are you sure you want to update the data [Y/N]: ')
                                if (decision == 'Y'):
                                    del stud[j]
                                    updated()
                                    break
                                elif (decision == 'N'):
                                    cancel()
                                    break
                                else:
                                    dataNotFound()
                            break
                    else:
                        dataNotFound ()
                    break

            elif (sub4==2):
                break
            
            else:
                dataNotFound()
            
        if (main=='5'):
            print ('Program will now close.\nThank you for using ACADEMIC SCORES. See you next time!\n ========================')
            break

        else:
            dataNotFound()

prog()