from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):
                self._flightNo = flightNo
                self._origin = origin
                self._destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")


    def __repr__(self):
        originCity = self._origin.getCity()
        destinationCity = self._destination.getCity()
        if self.isDomesticFlight():
            flightStatus = " {domestic}"
        else:
            flightStatus = " {international}"
        return "Flight: " + self._flightNo + " from " + originCity + " to " + destinationCity + flightStatus

    def __eq__(self, other):
        if self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination():
            return True
        elif not isinstance(other, Flight):
            return False
        else:
            return False

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        originCountry = self._origin.getCountry()
        destinationCountry = self._destination.getCountry()
        if originCountry == destinationCountry:
            return True
        else:
            return False


    def setOrigin(self,origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination



