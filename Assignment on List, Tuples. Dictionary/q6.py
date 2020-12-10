EmployeeData = {'emp1': {'Name': 'Rick', 'job': 'Sales Manager' , 'JoiningDate':'17-11-2012' , 'Salary':'30000'},
     'emp2': {'Name': 'Mayank', 'job': 'Developer' , 'JoiningDate':'01-07-2020' , 'Salary':'10000'},
     'emp3': {'Name': 'Rita', 'job': 'Network Management' , 'JoiningDate':'09-01-2008' ,'Salary':'90000'},
     'emp4': {'Name': 'Rohit', 'job': 'Marketing' , 'JoiningDate':'21-07-2017' ,'Salary':'75000'},
     'emp5': {'Name': 'Kabir', 'job': 'System Analyst' , 'JoiningDate':'06-07-2020' , 'Salary':'20000'},
     'emp6': {'Name': 'Kate', 'job': 'Manager', 'JoiningDate': '16-09-2013' , 'Salary':'35000'}}


while True:
    print('Enter employee ID: ')
    print('or Exit')

    ch=input(('Enter your choice: ')).split()

    choice= ch[0].strip().lower()

    if choice=='exit':
        break
    else:
        options=input("Type 1 if you want to see all the information of the employee. Type 2 if you want to see a particular field ").split()
        option = options[0].strip().lower()
        if option=='1':
            print(EmployeeData[choice])
        elif option=='2':
            field=input("Enter the field which you want to see  -> Name , job , JoiningDate , Salary  ").split()
            ans=field[0].strip().lower()

            print(EmployeeData[choice].get(ans))