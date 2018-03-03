

class Queue:


    def __init__(self):
        self._qList = list()




    def enqueue(self, item):
        self._qList.append(item)



    def dequeue(self):
        return self._qList.pop(0)




    
    def isEmpty(self):
        return len(self) == 0




    def isFull(self):
        return len(self) == 10




    def __len__(self):
        return len(self._qList)



    




    
        




def current_status(garage,garageList,waiting,waitingList,moves):


    if command.lower()=="check-g":



        if garage.isEmpty():
            print("There are no cars in the garage now.\n")


        else:
           
            print("#####  GARAGE QUEUE  #####")
            


            for i in range(0,len(garage)):
                print(i+1,":",garageList[i],":",moves[i],"move(s)")


            if len(garage)==1:
                print("There is 1 car in the garage now.\n")


            else:
                print("There are",len(garage),"cars in the garage now.\n")                


    elif command.lower()=="check-w":        
        

        if waiting.isEmpty():
            print("There are no cars in the waiting queue now.\n")



        else:
           
            print("Waiting")
            



            for i in range(0,len(waiting)):
                print(i+1,":",waitingList[i])



            if len(waiting)==1:
                print("There is 1 car in the waiting queue now.\n")



            else:
                print("There are",len(waiting),"cars in the waiting queue now.\n")



def commandCheck(command,garage,garageList,waiting,waitingList,moves):


    if command=="check-g" or command=="check-w":
        current_status(garage,garageList,waiting,waitingList,moves)


    elif command[0:2].lower()=="a " and command[2:4].isalpha() and command[4:].isdigit():


        if command[2:] in garageList:
            print(command[2:],"number car is already in garage.\n")


        elif command[2:] in waitingList:
            print(command[2:],"number car is already in waiting queue. \n")



        else:
            space_check(command[2:].upper(),garage,garageList,waiting,waitingList,moves)


    elif command[0:2].lower()=="d " and command[2:4].isalpha() and command[4:].isdigit():
        presence_check(command[2:].upper(),garage,garageList,waiting,waitingList,moves)



    else:
        print("Incorrect Command.\n")


def space_check(number,garage,garageList,waiting,waitingList,moves):



    if not garage.isFull():
        print("There is room for the car.")
        garage.enqueue(number)
        garageList.append(number)
        moves.append(0)
        print(number,"has been parked.\n")



    else:
        print("No Space for the car.")
        waiting.enqueue(number)
        waitingList.append(number)
        print(number,"number car has been added to the waiting queue.\n")





def presence_check(number,garage,garageList,waiting,waitingList,moves):



    if number in garageList:
        print(number,"number car is in the garage.")
        loop_garage(number,garage,moves)        
        parking_waiting(garage,garageList,waiting,waitingList,moves)



    elif number in waitingList:
        print(number,"number car is in waiting queue.")
        loop_waiting(number,waiting)        



    else:
        print("Car  is not here.\n")





def loop_garage(number,garage,moves):



    for i in range (0,len(garage)):
        top=garage.dequeue()


        if top==number:
            print(number,"number car has been departed.\nIt moved",moves.pop(i)+1,"time(s) within the garage")
            print("THANK YOU.\n")


        else:


            garage.enqueue(top)
    garageList.remove(number)



    for i in range(0,len(moves)):
        moves[i]=moves[i]+1










        
def parking_waiting(garage,garageList,waiting,waitingList,moves):



    if not waiting.isEmpty():
        print("There is space for a car.")
        garage.enqueue(waiting.dequeue())
        garageList.append(waitingList.pop(0))
        moves.append(0)
        print(garageList[-1],"number car has been parked at garage from waiting queue\n")

def loop_waiting(number,waiting):



    for i in range (0,len(waiting)):
        top=waiting.dequeue()



        if top==number:
            print(number,"number car has been departed.\nIt moved 0 time(s) within the garage\nTHANK YOU. COME AGAIN\n")



        else:
            waiting.enqueue(top)
    waitingList.remove(number)



garage=Queue()
garageList=list()
waiting=Queue()
waitingList=list()
moves=list()




print("*****************************************************************")



print("####################***  LAUGHS PARKING *****####################")


print("#**********##*************************##************************#\n")







print("Example : 'a AB1234'")



print("check-w : To check the current status of the waiting")
print("check-g : To check the status")






print("done")





while True:
    command=input("command : ")
    if command.lower()=="done":
        break                
    else:
        commandCheck(command,garage,garageList,waiting,waitingList,moves)
