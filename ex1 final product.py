import sys

def playerMaker(): #FUNCTION THAT TAKES THE DATA FOR THE DOCUMENT AND STORES IT IN A LIST
    #set up variables for storing the data
    team = ''
    role = ''
    fName = ''
    lName = ''
    salary = ''
    listA = []

    for j in range(totLines):
        for k in input_file:
            c = 0
            for i in k:
                if i == ' ':
                    c += 1                
                if c == 0:
                    team += i
                elif c == 1:
                    role += i
                elif c == 2:
                    fName += i
                elif c == 3:
                    lName += i
                else:
                    salary += i
            data = (team.strip(), role.strip(), fName.strip(), lName.strip(), salary.strip()) #HERE I CREATE A TUPLE AND THE PROCESS IS QUITE LONG, I COULD HAVE CREATED A LIST INSTED USING .STRIP() BUT THE ASSIGNMENT SAID TO CREATE A TUPLE

            #resetting the variables for new entries
            team = ''
            role = ''
            fName = ''
            lName = ''
            salary = ''
            
            listA.append(data)
            data = ()
    return listA

def mainTable(): #FUNCTION THAT DISPLAYS THE LIST IN A TABLE FORMAT
    risultato = playerMaker()
    print('')
    print('{:15s} {:15s} {:15s} {:15s} {:15}'.format('Last Name', 'First Name', 'Salary', 'Position', 'Team'))
    print('---------------------------------------------------------------------------')
    for j in range(totLines):
            print('{:15s} {:15s} {:15s} {:15s} {:15}'.format(risultato[j][3], risultato[j][2], risultato[j][4], risultato[j][1], risultato[j][0]))
    print('---------------------------------------------------------------------------')
    print('')
    return risultato

def fileLen(): #FUNTION THAT COUNTS THE NUMBER OF LINES INSIDE THE DOCUMENT
        with open(file) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def salary(j): #FUNTION THAT TRANSFORMS THE SALARY FROM STRING WITH COMMAS TO INTEGER
    num = int(mainTable[j][4].replace(',',''))
    return num

def sortList(listB): #FUNTION THAT SORTS THE SALARY IN ASCENDEND ORDER
    listB.sort(key = lambda x: x[4]) 
    return listB

def checkFileName(): #FUNCTION THAT CHECKS IF THE NAME OF THE FILE PROVIDED CAN BE FOUND, IF NOT THE USER CHOOSES TO TRY AGAIN
    file = input('Please insert the name of the file: ')
    print('')
    if file[-4:] != '.txt':
        file += '.txt'
    try:
        input_file = open(file, 'r')
        return file, input_file
    except:
        print('The file name that you have provided cannot be found')
        if input('Do you want to try with a different file name? y = yes anything else = no ') == 'y':
            print('')
            file, input_file = checkFileName()
            return file, input_file
        else:
            print('Thanks')
            sys.exit()

def trueFalse (): #FUNCTION THAT ASKS THE USER TO INPUT Y AS YES OR N (IN REALITY ANYTHING BUT Y) AS NO AND IT RETURNS TRUE FOR Y AND FALSE FOR N (ANYTHING BUT Y)
    print('')
    if input('Do you want to try with different values? y = yes anything else = no ') == 'y':
        return True
    else:
        print('')
        print('Thanks')
        return False


#START OF THE PROGRAM

file, input_file = checkFileName()

totLines = fileLen() #TOTLINES IS A VARIABLE THAT STORES THE NUMBER OF LINES INSIDE OF THE FILE.TXT IT IS USED SEVERAL TIMES IN THE CODE INSIDE OF FOR LOOPS
mainTable = mainTable() #MAINTABLE IS THE NAME OF THE LIST THAT WILL BE CALLED SEVERAL TIMES IN THE CODE IN ORDER TO RETRIVE INFROMATION FROM THE LIST


for i in range(10):
    print('')
    print('l = Full details of a single player \ns = Players with a salary range between X - Y \nt = First an last name of players in the same team \nq = Quit')
    option = input('How would you like to sort your data? ')
    count = 0
    
    if option == 'l': #OPTION 1 (FULL DETAILS OF PLAYER)
        print('')
        inName = input('Please input the last name of the player that you are intreseted in: ').capitalize()
        print('')
        print('{:15s} {:15s} {:15s} {:15s} {:15}'.format('Last Name', 'First Name', 'Salary', 'Position', 'Team'))
        print('---------------------------------------------------------------------------')
        for j in range(totLines):
            if mainTable[j][3] == inName:                
                print('{:15s} {:15s} {:15s} {:15s} {:15}'.format(mainTable[j][3], mainTable[j][2], mainTable[j][4], mainTable[j][1], mainTable[j][0]))
                count += 1
        if count == 0:
            print('There is no data for the player with last name {}'.format(inName))
        print('---------------------------------------------------------------------------')

    elif option == 's': #OPTION 2 (SORT BY SALARY)
        print('')
        try:
            lowB = int(input('Please insert the minimun salary: '))
            highB = int(input('Please insert the maximum salary: '))
        except ValueError:
            print('That was an invalid input')
            continue
        print('')
        print('{:15s} {:15s} {:15s} {:15s} {:15}'.format('Last Name', 'First Name', 'Salary', 'Position', 'Team'))
        print('---------------------------------------------------------------------------')
        for j in range(totLines):
            if salary(j) in range(lowB, highB):
                print('{:15s} {:15s} {:15s} {:15s} {:15}'.format(mainTable[j][3], mainTable[j][2], mainTable[j][4], mainTable[j][1], mainTable[j][0]))
                count += 1
        if count == 0:
            print('There is no player with salary between {} and {}'.format(lowB, highB))
        print('---------------------------------------------------------------------------')

    elif option == 't': #OPTION 3 (SORT NAME OF PLAYERS BY TEAM)
        print('')
        teamName = input('Please insert the name of the team: ').capitalize()
        print('')
        print('{:15s} {:15s}'.format('Last Name', 'First Name'))
        print('---------------------------------------------------------------------------')
        for j in range(totLines):
            if mainTable[j][0] == teamName:
                print('{:15s} {:15s}'.format(mainTable[j][3], mainTable[j][2]))
                count += 1
        if count == 0:
            print('There is no team called {}'.format(teamName))
        print('---------------------------------------------------------------------------')

    elif option == 'q': #OPTION 4 (QUIT FOR LOOP)
        break

    else:
        print('')
        print('That was an invalid input')

for i in range(10):
    count = 0
    print('')
    print('Please now input the name of a team and the role of a player in that team')
    teamName = input('Team name: ').capitalize()
    position1 = input('Player position: ').capitalize()
    print('')
    print('Please now input the position of a player and lower and upper bound for the salary')
    position2 = input('Player position: ').capitalize()
    try:
        lowB = int(input('Minimun salary: '))
        highB = int(input('Maximum salary: '))
    except ValueError:
        print('')
        print('That was an invalid input')
        continue
    print('')
    print('{:15s} {:15s} {:15s} {:15s} {:15}'.format('Last Name', 'First Name', 'Salary', 'Position', 'Team'))
    print('---------------------------------------------------------------------------')
    
    for j in range(totLines): #CHECKING FOR FIRST CONDITION (TEAM AND POSITION)
        if mainTable[j][0] == teamName and mainTable[j][1] == position1:
            print('{:15s} {:15s} {:15s} {:15s} {:15}'.format(mainTable[j][3], mainTable[j][2], mainTable[j][4], mainTable[j][1], mainTable[j][0]))
            count += 1
    if count == 0:
        print('There is no {} playing in {}'.format(position1, teamName))
    print('---------------------------------------------------------------------------')
    print('')
    print('{:15s} {:15s} {:15s} {:15s} {:15}'.format('Last Name', 'First Name', 'Salary', 'Position', 'Team'))
    print('---------------------------------------------------------------------------')

    listB = []
    count = 0
    for j in range(totLines): #CHECKING FOR SECOND CONDITION (POSITION AND SALARY)       
        if salary(j) in range(lowB, highB) and mainTable[j][1] == position2:
            listB.append(mainTable[j])
            count += 1
    listB = sortList(listB)
    for j in range(count):
        print('{:15s} {:15s} {:15s} {:15s} {:15}'.format(listB[j][3], listB[j][2], listB[j][4], listB[j][1], listB[j][0]))
    if count == 0:
        print('There is no player with salary between {} and {} that plays as a {}'.format(lowB, highB, position2))
    print('---------------------------------------------------------------------------')

    if trueFalse() is True:
        continue
    else:
        break
    
input_file.close()
