class ParkingGarage():

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTicket = {
            'paid' : False,
            'ticket number': '',
            'spot' : ''
            }
        self.payment = ''

    def takeTicket(self):
        if self.tickets and self.parkingSpaces:
            self.currentTicket['ticket number'] = self.tickets.pop()
            self.currentTicket['spot'] = self.tickets.pop()
            print(f"There are {self.tickets(-1)} tickets remaining as well as {self.parkingSpaces(-1)} parking spaces availible")
        
        else:
            print("There are currently no spaces! Sorry for the inconvenience")
            quit


    def payForParking(self):
        self.payment = input("The machine demands 23 dollars. How much do you pay")
        if self.payment == '23':
            print("The machine is satisfied")
            self.currentTicket['paid'] = True
        else:
            print("This is not the correct amount. The machine demands 23 like Mike!")


    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("You may leave")
            self.tickets.append(self.currentTicket['ticket number'])
            self.currentTicket['ticket number'] = ''
            self.parkingSpaces.append(self.currentTicket['spot'])
            self.currentTicket['spot'] = ''

        else:
            while self.currentTicket['paid'] == False:
                self.payment = input("23 dollars. No more no less. Please put in the correct amount or the machine will be angry\n")
                if self.payment == '23':
                    print("\nThank you for paying. You may exit.")
                    self.currentTicket['paid'] = True
                    self.tickets.append(self.currentTicket['number'])
                    self.currentTicket['number'] = ''
                    self.parkingSpaces.append(self.currentTicket['parking spot'])
                    self.currentTicket['parking spot'] = ''
                else:
                    print("23 dollars. No more no less. Please put in the correct amount or the machine will be angry\n")


garage = ParkingGarage()
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()

