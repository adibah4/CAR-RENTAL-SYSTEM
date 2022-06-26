import calculator  #import our own module calculator

import turtle               #turtle library
wn = turtle.Screen()        #create a playground
wn.bgcolor("black")
wn.title("Car Rental System")

#todo : appear name of our system
turtle.color("white")
style = ("courier", 18, "bold")
turtle.write("CAR RENTAL SYSTEM", font = style, align = 'center')
turtle.hideturtle()

#todo : appear "Loading" word
turtle.color("grey")
turtle.penup()
turtle.setpos(0,-100)
turtle.pendown()
style = ("verdana", 12, "normal")
turtle.write("loading", font = style, align = 'center')
turtle.hideturtle()

#todo : appear "please click anywhere after loading done " word
turtle.color("grey")
turtle.penup()
turtle.setpos(0,-150)
turtle.pendown()
style = ("verdana", 12, "normal")
turtle.write("Please click anywhere after loading done", font = style, align = 'center')
turtle.hideturtle()

#create turtle assign to cr (todo: draw)
cr = turtle.Turtle()
cr.color("white")
cr.pensize(3)
cr.shape("square")
cr.speed(2)

cr.penup()
cr.setpos(-220,-20)
cr.pendown()

for i in range(6):
    cr.pendown()

    cr.forward(30)
    cr.right(90)
    cr.forward(30)
    cr.right(90)
    cr.forward(30)
    cr.right(90)
    cr.forward(30)
    cr.right(90)
    cr.forward(30)

    cr.penup()
    cr.forward(50)
turtle.exitonclick()
wn.mainloop()                                               #close window

def maketuple(*args):                                       #*ARGS arguments function
    k=args
    return k                                                #return in tuple
def deletecar(x):                                           #delete the car from text after selected to rent
    if x == 1:
        myvidelete = open("CAR.txt", "r")                   # reading the file
        data = myvidelete.read()
        ifmyvi = data.split("\n")                           #replacing end splitting the text when newline ('\n') is seen.
        myvidelete.close()
        ifmyvi.remove('Myvi')                               #remove bezza from the list
        with open("CAR.txt", "w") as fp:
            for item in ifmyvi:
                fp.write("%s\n" %item)                      #write back list into text
    elif x==2:
        bezzadelete = open("CAR.txt", "r")                  # reading the file
        data = bezzadelete.read()
        ifbezza = data.split("\n")                          #replacing end splitting the text when newline ('\n') is seen.
        bezzadelete.close()
        ifbezza.remove('Bezza')                             #remove bezza from the list
        with open("CAR.txt", "w") as fp:
            for item in ifbezza:
                fp.write("%s\n" %item)                      #write back list into text
    elif x==3:
        alzadelete = open("CAR.txt", "r")                   # reading the file
        data = alzadelete.read()
        ifalza = data.split("\n")                           # replacing end splitting the text when newline ('\n') is seen.
        alzadelete.close()
        ifalza.remove('Alza')                               #remove bezza from the list
        with open("CAR.txt", "w") as fp:
            for item in ifalza:
                fp.write("%s\n" %item)                      #write back list into text

#admin interface
class admin():
    def __init__(self,Car,User):
        self.Car = Car
        self.User=User

    def upd_cars(Car):
            ans = str(input("Do you want to update Rent per hour?: y-Yes, n-No \t"))     #ask input if the staff want to update(JUST IN CASE)
            if ans == "y" or ans == "Y":                                                 #IF YES
                new_rent = int(input("The new rental rate per hour(RM): "))
                Car.update([('Rental_rate',new_rent)])
            elif ans == "n"or ans == "N" :                                               #IF NO
                print("No update for rent per hour")
            else:
                print("Invalid answer")                                                  #INVALID

class user(admin):                                          #Subclass
    def __init__(self,name,ic,hours):
        self.name = name
        self.ic = ic
        self.hours = hours
        admin.__init__(self)                                #invoking the __init__ from the parent class

    def sel_cars(Car):
        for x in Car:
            print(x,":",Car[x])
        hours = int(input("Duration of rental(in hours): "))
        User.update([('Rental duration',hours)])            #update receipt for hours
        name = input("Insert your name: ")
        User.update([('Name',name)])                        #update receipt for name
        ic = input("Insert your IC Number: ")
        User.update([('No IC',ic)])                         #update receipt for IC number
        rate = Car.get('Rental_rate')
        price = calculator.pricetotal(rate,hours)
        User.update([('Price(in RM)',price)])               #update receipt for total price
        pass

#Dictionary that contain the car information
User = {'Name':'a','No IC':0,'Rental duration':0, 'Price(in RM)':0}     #User dictionary for receipt
Myvi = {'Brand':"Myvi",'Seat':4, 'Rental_rate':100}                     #Myvi dictionary that stores Myvi information for rent
Bezza = {'Brand':"Bezza",'Seat':4, 'Rental_rate':9}                     #Bezza dictionary that stores Bezza information for rent
Alza = {'Brand':"Alza",'Seat':6, 'Rental_rate':20}                      #Myvi dictionary that stores Myvi information for rent
##
###Main Menu
while(True):
    opt_adm = int(input("\n1-Update rent per hour \n2-Car Availability \n3-Delete booking \n4-User Interface \n5-Exit \t"))  #Print menu and choose input
    if opt_adm == 1:
        car = int(input("Choose the car: \n1-Myvi \n2-Bezza \n3-Alza \n4-Back \t"))  #Choose car
        if car == 1:
            Adm = admin.upd_cars(Myvi)                      #update key(Rental_rate) in Myvi dictionary
        elif car == 2:
            Adm = admin.upd_cars(Bezza)                     #update key(Rental_rate) in Bezza dictionary
        elif car == 3:
            Adm = admin.upd_cars(Alza)                      #update key(Rental_rate) in Alza dictionary
        elif car==4:
            pass                                            #back
        else:
            print("Wrong input. Please enter valid value")  #wrong input
    elif opt_adm ==2:
        layout = "{0:<6}{1}"                                #string formatting for menu
        f="ITEMS"
        x="code"
        #Print menu
        print(layout.format(x,f))                           #Menu formatting
        print("--------------")

        items=["Car list", "check car availability","Back"]
        fn=1
        for fl in items:
            print(layout.format(fn,fl))                     #Menu and item list formating
            fn+=1
        print("--------------")
        codei=int(input("Choose code: "))                   #choose code for menu

        if codei ==1:
            x="Code"
            b="Car"
            print(layout.format(x,b))
            print("--------------")
            carlist=maketuple("Myvi", "Bezza", "Alza")      #pass argument to function maketuple to create tuple from the given items
            a=1
            #Print menu
            for i in carlist:
                print(layout.format(a,i))                   #Menu and item list formating
                a+=1
            print("--------------")
        elif codei==2:
            car_file=open("CAR.txt","r")                    #open file
            while True:
                theline=car_file.readline()                 #read line by line
                if len(theline)==0:
                    break                                   #stop if there is no more string at current line
                print(theline, end="")                      #print each string from each line
            car_file.close()                                #Close file
#DONE BOOKING or CANCEL BOOKING
    elif opt_adm ==3:
        card = int(input("Choose option: \n1-Cancel booking \n2-Done renting \n3-Back\t"))          #Print menu and select item
        #CANCEL BOOKING
        if card ==1:
            carc = int(input("Choose the car you booked: \n1-Myvi \n2-Bezza \n3-Alza \n4-Back\t"))  #Print menu and select item
            if carc ==1:
                #MYVI
                carmyvican='Myvi'                           #define string
                carlistmyvican=open("CAR.txt","r")          #opening the file in read mode
                flagmyvican=0                               #define flag and index as 0
                indexmyvican=0
                for line in carlistmyvican:                 #check car
                    indexmyvican+=1
                    if carmyvican in line:
                        flagmyvican = 1                     #if car is available,set flag 1
                        break                               #stop the loop after the string is available or no more line available
                if flagmyvican ==1:
                    print("\nCar is already in the data")   #if the car is already available, dont modify
                else:
                    myvican = open("CAR.txt", "r")          # opening the file in read mode
                    datamyvi = myvican.read()               # reading the file
                    listmyvi = datamyvi.split("\n")         # replacing end splitting the text when newline ('\n') is seen.
                    myvican.close()
                    listmyvi.append('Myvi')                 #add myvi to the list
                    with open("CAR.txt", "w") as fpm:
                        for item in listmyvi:
                            fpm.write("%s\n" %item)         #write back list into text
            elif carc ==2:
                #Bezza
                carbezzacan='Bezza'                         #define string
                carlistbezzacan=open("CAR.txt","r")         #opening the file in read mode
                flagbezzacan=0                              #define flag and index as 0
                indexbezzacan=0
                for line in carlistbezzacan:                #check car
                    indexbezzacan+=1
                    if carbezzacan in line:
                        flagbezzacan = 1                    #if car is available,set flag 1
                        break                               #stop the loop after the string is available or no more line available
                if flagbezzacan ==1:
                    print("\nCar is already in the data")   #if the car is already available, dont modify
                else:
                    bezzacan = open("CAR.txt", "r")         # opening the file in read mode
                    databezza = bezzacan.read()             # reading the file
                    listbezza = databezza.split("\n")       # replacing end splitting the text when newline ('\n') is seen.
                    bezzacan.close()
                    listbezza.append('Bezza')               #add bezza to the list
                    with open("CAR.txt", "w") as fpb:
                        for item in listbezza:
                            fpb.write("%s\n" %item)         #write back list into text
            elif carc ==3:
                #Alza
                caralzacan='Alza'                           #define string
                carlistalzacan=open("CAR.txt","r")          #opening the file in read mode
                flagalzacan=0                               #define flag and index as 0
                indexalzacan=0
                for line in carlistalzacan:                 #check car
                    indexalzacan+=1
                    if caralzacan in line:
                        flagalzacan = 1                     #if car is available,set flag 1
                        break                               #stop the loop after the string is available or no more line available
                if flagalzacan ==1:
                    print("\nCar is already in the data")   #if the car is already available, dont modify
                else:
                    alzacan = open("CAR.txt", "r")          # opening the file in read mode
                    dataalza = alzacan.read()               # reading the file
                    listalza = dataalza.split("\n")         # replacing end splitting the text when newline ('\n') is seen.
                    alzacan.close()
                    listalza.append('Alza')                 #add alza to the list
                    with open("CAR.txt", "w") as fpa:
                        for item in listalza:
                            fpa.write("%s\n" %item)         #write back list into text
            elif carc==4:
                pass                                        #BACK
            else:
                print("Wrong input. Please enter valid input")
        elif card ==2:
            cardone = int(input("Choose the car you booked: \n1-Myvi \n2-Bezza \n3-Alza \n4-Back\t"))  #Print menu
            if cardone ==1:
                #MYVI
                carmyvi='Myvi'                              #define string
                carlistmyvi=open("CAR.txt","r")             #opening the file in read mode
                flagmyvi=0                                  #define flag and index as 0
                indexmyvi=0
                for line in carlistmyvi:                    #check car
                    indexmyvi+=1
                    if carmyvi in line:
                        flagmyvi = 1                        #set flag to 1 if the string is available
                        break                               #stop the loop after the string is available or no more line available
                if flagmyvi ==1:
                    print("\nCar is already in the data")   #if the car is already available, dont modify
                else:
                    my_file = open("CAR.txt", "r")          # opening the file in read mode
                    data = my_file.read()                   # reading the file
                    data_into_list = data.split("\n")       # replacing end splitting the text when newline ('\n') is seen.
                    my_file.close()
                    data_into_list.append('Myvi')           #add Myvi to the list
                    with open("CAR.txt", "w") as fp:
                        for item in data_into_list:
                            fp.write("%s\n" %item)          #write back list into text
            elif cardone ==2:
                #Bezza
                carbezza='Bezza'                            #define string
                carlistbezza=open("CAR.txt","r")            # opening the file in read mode
                flagbezza=0                                 #set flag and index to 0
                indexbezza=0
                for line in carlistbezza:                   #check car
                    indexbezza+=1
                    if carbezza in line:
                        flagbezza = 1                       #set flag to 1 if the string is available
                        break                               #stop the loop after the string is available or no more line available
                if flagbezza ==1:
                    print("\nCar is already in the data")   #if the car is already available, dont modify
                else:
                    my_file = open("CAR.txt", "r")          # opening the file in read mode
                    data = my_file.read()                   # reading the file
                    data_into_list = data.split("\n")       # replacing end splitting the text when newline ('\n') is seen.
                    my_file.close()
                    data_into_list.append('Bezza')          #add Bezza to the list
                    with open("CAR.txt", "w") as fp:
                        for item in data_into_list:
                            fp.write("%s\n" %item)          #Write the list into text file
            elif cardone ==3:
                #Alza
                caralza='Alza'                              #define string
                carlistalza=open("CAR.txt","r")             # opening the file in read mode
                flagalza=0                                  #set flag and index to 0
                indexalza=0
                for line in carlistalza:                    #check car
                    indexalza+=1
                    if caralza in line:
                        flagalza = 1                        #set flag to 1 if the string is available
                        break                               #stop the loop after the string is available or no more line available
                if flagalza ==1:
                    print("\nCar is already in the data")   #if the car is already available, dont modify
                else:
                    my_file = open("CAR.txt", "r")          # opening the file in read mode
                    data = my_file.read()                   # reading the file
                    data_into_list = data.split("\n")       # replacing end splitting the text when newline ('\n') is seen.
                    my_file.close()
                    data_into_list.append('Alza')           #add alza to the list
                    with open("CAR.txt", "w") as fp:
                        for item in data_into_list:
                            fp.write("%s\n" %item)          #write list back into the text file
            elif cardone ==4:
                pass                                        #BACK
            else:
                print("Wrong input. Please enter valid input")  #invalid input
        elif card==3:
            pass                                            #BACK
        else:
            print("Wront input. Please enter valid input")  #invalid input


    elif opt_adm == 4:
        opt_user = int(input("\nWelcome to Car booking menu \nChoose the option: \n1-Register User \n2-back \t"))  #Print menu and select option
        if opt_user == 1:
            sel_car= int(input("Choose your car \n1-Myvi \n2-Bezza \n3-Alza \n4-back\t"))  #Print menu and select option
            if sel_car == 1:
                car1='Myvi'                                 #define string
                carlista=open("CAR.txt","r")                # opening the file in read mode
                flagm=0                                     #set flag and index to 0
                indexm=0
                for line in carlista:                       #check car
                    indexm+=1
                    if car1 in line:
                        flagm = 1                           #set flag to 1 if the string is available
                        break                               #stop the loop after the string is available or no more line available
                if flagm == 0:
                    print("\nCar not available. Please select other car")  #if the car is not available, dont modify
                else:
                    selectedcar=Myvi
                    admin(Myvi,User)                        #pass arguments to class
                    user.sel_cars(selectedcar)              #to edit user dictionary
                    deletecar(sel_car)                      #delete myvi from text file
                    for x in User:
                        print(x,":",User[x])                #print user dictionary as receipt
            elif sel_car == 2:
                car3='Bezza'                                #define string
                carlistb=open("CAR.txt","r")                # opening the file in read mode
                flagb=0                                     #set flag and index to 0
                indexb=0
                for line in carlistb:                       #check car
                    indexb+=1
                    if car3 in line:
                        flagb = 1                           #set flag to 1 if the string is available
                        break                               #stop the loop after the string is available or no more line available
                if flagb ==0:
                    print("\nCar not available. Please select other car")  #if the car is not available, dont modify
                else:
                    selectedcar=Bezza
                    admin(Bezza,User)                       #pass arguments to class
                    user.sel_cars(selectedcar)              #to edit user dictionary
                    deletecar(sel_car)                      #delete bezza from text file
                    for x in User:
                        print(x,":",User[x])                #print user dictionary as receipt
            elif sel_car == 3:
                car3='Alza'                                 #define string
                carlistc=open("CAR.txt","r")                # opening the file in read mode
                flaga=0                                     #set flag and index to 0
                indexa=0
                for line in carlistc:                       #check car
                    indexa+=1
                    if car3 in line:
                        flaga = 1                           #set flag to 1 if the string is available
                        break                               #stop the loop after the string is available or no more line available
                if flaga ==0:
                    print("\nCar not available.Please select other car")  #if the car is not available, dont modify
                else:
                    selectedcar=Alza
                    admin(Alza,User)                        #pass arguments to class
                    user.sel_cars(selectedcar)              #to edit user dictionary
                    deletecar(sel_car)                      #delete alza from text file
                    for x in User:
                        print(x,":",User[x])                #print user dictionary as receipt
            elif sel_car ==4:
                pass                                        #BACK
            else:
                print("Invalid input. Please try again")    #invalid input
        if opt_user == 2:
            pass                                            #BACK
    elif opt_adm == 5:
        exit()                                              #exit
    else:
       print("Invalid Number. Please try again")            #invalid input