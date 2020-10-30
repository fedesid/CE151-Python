import sys
import math

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
        if input('Do you want to try with a different file name? y = yes n = no ') == 'y':
            print('')
            file, input_file = checkFileName()
            return file, input_file
        else:
            print('Thanks')
            sys.exit()

def fileLen(): #FUNTION THAT COUNTS THE NUMBER OF LINES INSIDE THE DOCUMENT
        with open(file) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def cityMaker(): #FUNCTION THAT CREATES A LIST WITH ALL THE INFORMATION ABOUT THE CITIES
        city = ''
        lat = ''
        lon = ''
        pop = ''
        finalList = []
        for item in input_file:
            c = 0
            for i in item:
                if i == ' ':
                    c += 1
                if c == 0:
                    city += i
                elif c == 1:
                    lat += i
                elif c == 2:
                    lon += i
                else:
                    pop += i
            cityInfo = (city.strip(), lat.strip(), lon.strip(), pop.strip()) #HERE I CREATE A TUPLE AND THE PROCESS IS QUITE LONG, I COULD HAVE CREATED A LIST INSTED USING .STRIP() BUT THE ASSIGNMENT SAID TO CREATE A TUPLE

            city = ''
            lat = ''
            lon = ''
            pop = ''
                
            finalList.append(cityInfo)
            cityInfo = []
        return finalList

def mainTable(): #FUNTION THAT DISPLAYS ALL THE INFORMATION ABOUT THE CITIES IN A TABLE FORMAT
    print('')
    print('{:15s} {:10s} {:10s} {:8s}'.format('City', 'Latitude', 'Longitude', 'Population'))
    print('---------------------------------------------------------------------------')
    for j in range(totLines):
            print('{:15s} {:10s} {:10s} {:8s}'.format(risultato[j][0], risultato[j][1], risultato[j][2], risultato[j][3]))
    print('---------------------------------------------------------------------------')
    print('')
    return risultato

def popTable(): #FUNCTION THAT DISPLAYS CITY AND POPULATION THE LIST IN A TABLE FORMAT
    
    print('')
    print('---------------------------------------------------------------------------')
    for j in range(totLines):
            print('{:15s} n. citizens {:8s}'.format(risultato[j][0], popComma(j)))
    print('---------------------------------------------------------------------------')
    print('')
    return risultato

def popComma(j): #ADDS COMMAS TO THE POPULATION NUMBER
        pop = int(risultato[j][3])
        pop = f"{pop:,d}"
        return pop

def latInt(j): #FUNTION THAT TRANSFROMS THE STRING OF LATITUDE INTO AN INTEGER NUMBER
    lat = int(risultato[j][1])
    return lat

def lonInt(j): #FUNTION THAT TRANSFROMS THE STRING OF LONGITUDE INTO AN INTEGER NUMBER
    lon = int(risultato[j][2])
    return lon

def popInt(j): #FUNTION THAT TRANSFROMS THE STRING OF POPULATION INTO AN INTEGER NUMBER
    pop = int(risultato[j][3])
    return pop

def pyth(a,b): #FUNTION THAT USES PYTHAGORAS THEOREM USED TO CALCULATE THE DISTANCE BETWEEN TWO CITIES
    value = math.sqrt(a*a + b*b)
    return value

def trueFalse (): #FUNCTION THAT ASKS THE USER TO INPUT Y AS YES OR N (IN REALITY ANYTHING BUT Y) AS NO AND IT RETURNS TRUE FOR Y AND FALSE FOR N (ANYTHING BUT Y) IT IS USED IN THE PORGRAM TO ALLOW THE USER TO TAKE CHOICES
    if input('Do you want to try with different values? y = yes n = no ') == 'y':
        return True
    else:
        print('')
        print('Thanks')
        return False
        


#START OF PROGRAM

file, input_file = checkFileName()
totLines = fileLen() #TOTLINES IS A VARIABLE THAT STORES THE NUMBER OF LINES INSIDE OF THE FILE.TXT IT IS USED SEVERAL TIMES IN THE CODE INSIDE OF FOR LOOPS
risultato = cityMaker() #RISULTATO IS THE NAME OF THE LIST THAT WILL BE CALLED SEVERAL TIMES IN THE CODE IN ORDER TO RETRIVE INFROMATION FROM THE LIST

popTable()
mainTable()

for i in range(10): #START OF MAIN LOOP
    print('')
    option = input('How would you like to sort your data? \n   c = Full detalis of a city \n   p = Details of cities with a range op population X - Y \n   r = Cities near specific cordinates (up to 10km radius) \n   q = Quit \n   Option chosen: ')
    c = 0
    
    if option == 'c': #FIRST OPTION (GATHERING DATA OF ONLY ONE CITY BY THE NAME PROVIDED BY THE USER)
        print('')
        cityName = input('Please insert the name of a city: ').capitalize()
        print('')
        print('{:15s} {:10s} {:10s} {:8s}'.format('City', 'Latitude', 'Longitude', 'Population'))
        print('---------------------------------------------------------------------------')
        for j in range(totLines):            
            if risultato[j][0] == cityName:
                print('{:15s} {:10s} {:10s} {:8s}'.format(risultato[j][0], risultato[j][1], risultato[j][1], risultato[j][3]))
                c += 1
        if c == 0:
            print('No city with name {} was found'.format(cityName))
        print('---------------------------------------------------------------------------')
        print('')

    elif option == 'p': #SECOND OPTION (FILTRING THE DATA BY THE RANGE OF POPULATION PROVIDED BY THE USER
        print('')
        try:
            popMin = int(input('Please insert minimum population: '))
            popMax = int(input('Please insert maximum population: '))
        except ValueError:
            print('That was an invalid input')
            continue
        print('')
        print('{:15s} {:10s} {:10s} {:10s}'.format('City', 'Latitude', 'Longitude', 'Population'))
        print('---------------------------------------------------------------------------')
        for j in range(totLines):
            if popInt(j) in range(popMin, popMax):
                print('{:15s} {:10s} {:10s} {:10s}'.format(risultato[j][0], risultato[j][1], risultato[j][1], risultato[j][3]))
                c += 1
        if c == 0:
            print('There is no city with population between {} and {}'.format(popMin, popMax))
        print('---------------------------------------------------------------------------')
        print('')

    elif option == 'r': #THIRD OPTION (FILTRING THE DATA BY THE COORDINATES PROVIDED BY THE USER
        print('')
        try:
            latIn = int(input('Please insert a latitude value: '))
            lonIn = int(input('Please insert a longitude value: '))
        except ValueError:
            print('That was an invalid input')
            continue
        print('')
        print('{:15s} {:10s} {:10s} {:10s} {:25s}'.format('City', 'Latitude', 'Longitude', 'Population', 'Distance (km)'))
        print('---------------------------------------------------------------------------')
        for j in range(totLines):
            latDif = abs(latInt(j) - latIn)
            lonDif = abs(lonInt(j) - lonIn)
            radius = float(format(math.sqrt((latDif*latDif) + (lonDif*lonDif)), '.3f'))
            if radius < 10:
                print('{:15s} {:10s} {:10s} {:10s} {}'.format(risultato[j][0], risultato[j][1], risultato[j][1], risultato[j][3], radius))
                c += 1
        if c == 0:
            print('There is no city in a radius of 10km from the given coordinates')
        print('---------------------------------------------------------------------------')
        print('')

    elif option == 'q': #FOURTH OPTION (QUIT)
        break

    else: #IN CASE THE USER INPUTS AN INVALID VALUE
        print('')
        print('That was an invalid input')

for i in range(10): #START OF SECOND LOOP (CALCULATE DISTANCE BETWEEN TWO CITIES)
    c = 0
    print('')
    try:
        city1, city2 = input('Enter two cities name, ex. Rome Berlin: ').split()
    except ValueError:
        print('Please insert two cities separated by a space')
        continue
    city1 = city1.capitalize()
    city2 = city2.capitalize()
    for j in range(totLines):
        if city1 == risultato[j][0]:
            c += 1
            city1Pos = j
        if city2 == risultato[j][0]:
            city2Pos = j
            c += 2
    if c == 0:
        print('None of the cities that you have provided were found')
        print('')
        if trueFalse() is True:
            continue
        else:
            break
    elif c == 1:
        print('The secod city that you have provided was not found')
        print('')
        if trueFalse() is True:
            continue
        else:
            break
    elif c == 2:
        print('The first city that you have provided was not found')
        print('')
        if trueFalse() is True:
            continue
        else:
            break
    distanceLat = abs((latInt(city1Pos) - latInt(city2Pos)))
    distanceLon = abs((lonInt(city1Pos) - lonInt(city2Pos)))
    distance = format(pyth(distanceLat, distanceLon), '.2f')
    print('')
    print('The distance between {} and {} is {}km'.format(city1, city2, distance))
    print('')

    if trueFalse() is True:
        continue
    else:
        break

input_file.close()
