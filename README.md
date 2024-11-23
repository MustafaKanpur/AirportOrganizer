# AirportOrganizer
Organizes info from a formatted CSV file in regards to airports, their cities and countries. Can create flights between airports, determining if connecting flights are necessary. 

Loads in data from a CSV file containing info on airports, location of said airports, outgoing and incoming flights from these airports. Organizes the airports into a list and the flights into a dictionary. The key for the flight dictionary is the airport code, and the value is a list of flight objects that depart from that airport. 

Data is loaded in from the CSV file, and cleaned up so that it can be easily formatted into a list. It is then organized into flight objects, and the previously stated data structures are created. The program can find aiirports by their code, all flights that come in our out of a city or a country, the flights between two airports, including connecting flights if necessary, and can also determine return flights. 

This program uses object oriented programming, efficient handling of data for search and storage purposes, and effective error handling.
