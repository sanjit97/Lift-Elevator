#Assumptions
# There are total 10 floors and maximum number of people that can enter in the lift is 8
# 0 stands for ground floor and 10 stands for 10th floor
# Every time there is a prompt asking user to call the lift or not. If he/she types yes, the lift would be called and if he/she types no, the lift won't be called(the program will stop there)
# Once the user types yes, the current position,direction and status will be shown to the user
# The floor number of the user will be taken as input and based on that the lift will be processed to that floor.
# The program assumes that the persons entering from a floor are travelling to the same destination via the lift
# There will be a time delay of 60s when the lift is in the same floor as the user and a time delay of 10s while travelling from source floor to destination floor.

import time

#floors=[0,1,2,3,4,5,6,7,8,9,10]
total_persons=8
lift_currentfloor=0
lift_currentdirection="up"
lift_currentstatus="closed"

def choice():
    call_lift=input("Call Elevator/Lift  (yes/no) \n")
    return call_lift

returned_choice=choice()
while(returned_choice=='yes'):
    print(" Current position of Lift is {}".format(lift_currentfloor))
    print(" Current direction of Lift is {}".format(lift_currentdirection))
    print(" Current status of Lift is {}".format(lift_currentstatus))

    floornumber=int(input("\n Hello! Which floor are you in?"))
    if(floornumber>10):
        print("\n This floor doesnt exist ! ")
    else:
        if (floornumber == lift_currentfloor):
            lift_currentstatus="open"
            print("\n The lift is in your floor! ")
            no_of_persons=int(input(" How many persons to enter? "))
            if(no_of_persons>8):
                print("\n Overload !")
            
            else:
                print(" Great! The lift is open for 1 minute. Pl get in !")
                time.sleep(60)
                total_persons-=no_of_persons
                print("\n The lift is now closed! ")
                lift_currentstatus="closed"
                target_floor_number=int(input("\n Which floor to go?"))
                if (target_floor_number > floornumber):
                    lift_currentdirection="up"
                    print("\n Moving in the Upward direction to Floor Number {0}".format(target_floor_number))
                    time.sleep(10)
                    print("\n Destination reached !")
                    print("\n Lift is now open! Have a great day! \n")
                    total_persons+=no_of_persons
                    lift_currentfloor=target_floor_number
                    lift_currentstatus="open"
                else:
                    lift_currentdirection="down"
                    print("\n Moving in the Downward direction to Floor Number {0}".format(target_floor_number))
                    time.sleep(10)
                    print("\n Destination reached !")
                    print("\n Lift is now open! Have a great day! \n")
                    lift_currentstatus="open"
                    lift_currentfloor=target_floor_number
                    total_persons+=1
        elif (floornumber > lift_currentfloor):
            print("\n Pl wait! The lift is coming to your floor from floor number {0} in the Upward direction".format(lift_currentfloor))
            time.sleep(10)
            print("\n The lift is in your floor! Opening lift ! ")
            no_of_persons=int(input(" How many persons to enter? "))
            if(no_of_persons>8):
                print("\n Overload !")
            
            else:
                print("Great!  The lift is open for 1 minute. Pl get in !")
                time.sleep(60)
                total_persons-=no_of_persons
                print("\n The lift is now closed! ")
                lift_currentstatus="closed"
                target_floor_number=int(input("\n Which floor to go?"))
                if (target_floor_number > floornumber):
                    lift_currentdirection="up"
                    print("\n Moving in the Upward  direction to Floor Number {0}".format(target_floor_number))
                    time.sleep(10)
                    print("\n Destination reached !")
                    print("\n Lift is now open! Have a great day! \n")
                    lift_currentstatus="open"
                    lift_currentfloor=target_floor_number
                    total_persons+=no_of_persons
                else:
                    lift_currentdirection="down"
                    print("\n Moving in the Downward direction to Floor Number {0}".format(target_floor_number))
                    time.sleep(10)
                    print("\n Destination reached !")
                    print("\n Lift is now open! Have a great day! \n")
                    lift_currentstatus="open"
                    lift_currentfloor=target_floor_number
                    total_persons+=no_of_persons
        else:
            lift_currentdirection="down"
            print("\n Pl wait! The lift is coming to your floor from floor number {0} in the Downward direction".format(lift_currentfloor))
            time.sleep(10)
            print("\n The lift is in your floor! Opening lift ! Pl get in !")
            no_of_persons=int(input(" How many persons to enter? "))
            if(no_of_persons>8):
                print("\n Overload !")
           
            else:
                print(" Great! The lift is open for 1 minute. Pl get in !")
                time.sleep(60)
                total_persons-=no_of_persons
                print("\n The lift is now closed! ")
                lift_currentstatus="closed"
                target_floor_number=int(input("\n Which floor to go?"))
                if (target_floor_number > floornumber):
                    lift_currentdirection="up"
                    print("\n Moving in the Upward direction to Floor Number {0}".format(target_floor_number))
                    time.sleep(10)
                    print("\n Destination reached !")
                    print("\n Lift is now open! Have a great day! \n")
                    lift_currentstatus="open"
                    lift_currentfloor=target_floor_number
                    total_persons+=no_of_persons
                else:
                    lift_currentdirection="down"
                    print("\n Moving in the Downward direction to Floor Number {0}".format(target_floor_number))
                    time.sleep(10)
                    print("\n Destination reached !")
                    print("\n Lift is now open! Have a great day! \n")
                    lift_currentstatus="open"
                    lift_currentfloor=target_floor_number
                    total_persons+=no_of_persons
    returned_choice=choice()
