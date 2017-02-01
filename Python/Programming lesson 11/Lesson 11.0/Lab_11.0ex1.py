class MilesPerHour:
    def __init__ (self,d,h,m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0

    def setValue(self,newDistance,newHours,newMinutes):
        self.distance = newDistance
        self.hours = newHours
        self.minutes = newMinutes
        self.mph = 0

    def getDistance(self):
        return self.distance

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getmph(self):
        self.mph = self.distance/(self.hours + self.minutes / 60.0)
        return self.mph

def Main():
    distance = int(input("How far was the distance?"))
    hours = int(input("How many hours?"))
    minutes = int(input("How many minutes?"))

    user1 = MilesPerHour(distance,hours,minutes)

    print(user1.getDistance(), "Miles in ", user1.getHours(), "hours and", user1.getMinutes(), " = ", user1.getmph(), "mph.\n\n")

    user1.setValue(10,2,0)

    print(user1.getDistance(), "miles in ", user1.getHours(), "hours and ", user1.getMinutes(), " = ", user1.getmph(), "MPH")

Main()
                    
