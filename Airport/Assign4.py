from Flight import *
from Airport import *

allAirports = []
allFlights = {}

# Gets the info from the text files and stores them in the appropriate containers
def loadData(airportFile, flightFile):
    try:
        with open(airportFile) as file:
            for line in file:
                # Gets rid of the extra spaces and characters in the text file
                lineList = line.strip("\n").split(",")
                lineList = cleanUpLine(lineList, line)
                # Initializes an airport object from each line of the text file
                newAirport = Airport(lineList[0], lineList[2], lineList[1])
                allAirports.append(newAirport)
            print(allAirports)

        for i in range(len(allAirports)):
            file = open(flightFile, "r")
            currentFlightList = []
            for line in file:
                # Sets the current key/code for the dictionary, based on the airport codes from the airport list
                currentCode = allAirports[i].getCode()
                # Cleans up the line
                lineList = line.strip("\n").split(",")
                lineList = cleanUpLine(lineList, line)
                # Checks if the flight is departing from the same airport as the current airport code
                if lineList[1] == currentCode:
                    # If it is, creates a flight object from the line, and adds it to a list
                    flight = createFlightObject(lineList[0], lineList[1], lineList[2])
                    currentFlightList.append(flight)
                else:
                    continue
            file.close()
            # Creates the dictionary entry with the key as the airport code and the value as the list of flights corresponding to that code
            allFlights[currentCode] = currentFlightList

    # Exceptions for if the text file doesn't properly initialize
    except IOError:
        print("File not found")
        return False

    except ValueError:
        print("File contents invalid")
        print(len(allAirports))
        return False

    return True

# Method to remove all the extra characters from each word in al ine
def cleanUpLine(lineList, line):
    for i in range(len(lineList)):
        lineList[i] = lineList[i].strip(" ").strip("\t")
    return lineList

# Method that creates airport objects and uses them to create a flight object
def createFlightObject(flightNumber, originCode, destinationCode):
    origin = getAirportByCode(originCode)
    destination = getAirportByCode(destinationCode)
    newFlight = Flight(flightNumber, origin, destination)
    return newFlight


# Returns an airport object from a given airport code
def getAirportByCode(code):
    # Goes through the allAirports list
    for i in range(0, len(allAirports)):
        # Checks if the current element of the list has the same code as the given code
        if code == allAirports[i].getCode():
            returnValue = allAirports[i]
            break
        else:
            returnValue = -1
    return returnValue


# Returns a list of all of the flight objects that involve the given city
def findAllCityFlights(city):
    flightsToFromCity = []
    # Goes through the flight dictionary and parses through each of the lists in the values
    for value in allFlights.values():
        for i in range(len(value)):
            originCity = value[i].getOrigin().getCity()
            destinationCity = value[i].getDestination().getCity()
            # Checks if the flight object involves the city as either the origin or destination
            if destinationCity == city or originCity == city:
                flightsToFromCity.append(value[i])
    return flightsToFromCity

# Returns a list of all the flight objects that involve a given country
# Uses the same method as findAllCityFlights except it checks the countries of the flight objects
def findAllCountryFlights(country):
    flightsToFromCountry = []
    for value in allFlights.values():
        for i in range(len(value)):
            originCity = value[i].getOrigin().getCountry()
            destinationCity = value[i].getDestination().getCountry()
            if destinationCity == country or originCity == country:
                flightsToFromCountry.append(value[i])
    return flightsToFromCountry

# Finds a flight object between two airports,finds a connecting flight if there isn't a direct one
def findFlightBetween(origAirport, destAirport):
    allFlightsCopy = dict(allFlights)
    connectingFlightSet = set()
    origAirportCode = origAirport.getCode()
    destAirportCode = destAirport.getCode()
    # Looks for a direct flight in the allFlights dictionary
    for value in allFlights.values():
        # Goes through each list in the dictionary, and checks if the objects origin and destination are the same as the given parameters
        for i in range(len(value)):
            currentOrigCode = value[i].getOrigin().getCode()
            currentDestCode = value[i].getDestination().getCode()
            # If it matches, it returns a string and exits the method
            if currentOrigCode == origAirportCode and currentDestCode == destAirportCode:
                return "Direct Flight: " + currentOrigCode + " to " + currentDestCode

    # Only goes to this block of code if there's not a direct flight
    # Looks for a connecting flight
    for value in allFlights.values():
        for i in range(len(value)):
            currentOrigCode = value[i].getOrigin().getCode()
            currentDestCode = value[i].getDestination().getCode()
            # Goes through the dictionary and the values, checks if the origin airport is the same
            if currentOrigCode == origAirportCode:
                # Then parses through a duplicate dictionary
                for value2 in allFlightsCopy.values():
                    for j in range(len(value2)):
                        # Looks for a flight object who's origin airport, is the same as the destination airport of the first flight object
                        currentOrigCode2 = value2[j].getOrigin().getCode()
                        if currentOrigCode2 == currentDestCode:
                            currentDestCode2 = value2[j].getDestination().getCode()
                            # Checks if the destination of the second flight object (the one who's origin is the same as the destination of the previous)
                            # is the same as the given destination
                            if currentDestCode2 == destAirportCode:
                                # Adds the connecting airport (the origin of the second flight object) to a set
                                connectingFlightSet.add(currentOrigCode2)
    # Checks if the set is empty, which determines whether there were any connecting flights or not
    if len(connectingFlightSet) == 0:
        return -1
    else:
        return connectingFlightSet


# Finds a return flight for the given flight object
def findReturnFlight(firstFlight):
    returnValue = None
    originalOrig = firstFlight.getOrigin().getCode()
    originalDest = firstFlight.getDestination().getCode()
    # Sets the origin to firstFlight's destination and vice versa
    reversedOrig = originalDest
    reversedDest = originalOrig

    # Goes through the allFlights dictionary
    for value in allFlights.values():
        # Checks each flight object to see if the origin and destination are the same as the reversed origin and destination
        for i in range(len(value)):
            currentOrig = value[i].getOrigin().getCode()
            currentDest = value[i].getDestination().getCode()
            if currentOrig == reversedOrig and currentDest == reversedDest:
                return value[i]
            else:
                returnValue = -1
    return returnValue




