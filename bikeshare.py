import random


class BikeShare(object):
    """
    Bike Share Service Object

    """
    def __init__(self):
        """
        Init a list of Bikes and Stations
        """
        self.bikes = list()
        self.stations = list()

    def show_bikes(self):
        """
        Prints a list of all bikes in the bike share system
        :return:
        """
        print self.bikes

    def add_bike(self, bike):
        """
        Logic to add a bike into the system
        :param bike:
        :return:
        """
        if len(self.stations) < 1:
            raise Exception('Sorry! There are no stations for this new bike!')

        # We want to create a temporary variable to store all the stations in the system
        available_stations = self.stations
        # We select a random one to be a potential home station for our new bike
        selected_station = random.choice(available_stations)

        # In the chance that the selected station is already full on bike
        # We want to find another one by random to see if their slots are full
        # Thus, every station has an equal chance to be home to a bike
        while len(selected_station.bikes) >= selected_station.bike_slots:
            selected_station_index = available_stations.index(selected_station)
            del available_stations[selected_station_index]

            if len(available_stations) == 0:
                raise Exception('Sorry! All Stations are full!')

            selected_station = random.choice(available_stations)

        # Helper function to get the index of the station in the bike share system
        station_index = self.get_station_index_by_name(selected_station.name)
        # Set the home station for the bike
        bike.set_home_station(self.stations[station_index])
        # Add the bike to the station's bike list
        self.stations[station_index].add_bike(bike)
        # Add bike into system
        self.bikes.append(bike)

    def check_out_bike(self, bike, station):
        """
        Logic for checking out a bike from a station
        :param bike:
        :param station:
        :return:
        """
        # Validation for checking out a bike
        if bike.checked_out is True:
            raise Exception('Sorry! This bike is already checked out.')

        if station.bikes.index(bike) == -1:
            print "This station, does not contain the bike you are looking for, going to check other stations..."

            station = self.get_station_of_bike(bike)
            if station is None:
                raise Exception("This bike is either already checked out or no longer in our system.")

        # First, we remove the bike from the station, toggle the checked out variable of the bike
        # to true, and its current station to none
        station.remove_bike(bike)
        bike.checked_out = True
        bike.current_station = None

    def return_bike(self, bike, station):
        """
        Returning a bike to a station
        :param bike:
        :param station:
        :return:
        """
        # Validation for returning a bike to a station
        if bike.checked_out is False:
            raise Exception("How did you get this bike!? It wasn't even checked out!")

        # In case the station is full, we will manually look for another station that is not
        if len(station.bikes) >= station.bike_slots:
            print "Sorry this station is full, going to try another station..."

            # If all stations are full, we must throw an error
            # Things that could happen are if we check a bike out, but add another into the system
            # Without expanding the number of bike slots
            station = self.get_station_with_bike_slots()
            if station is None:
                raise Exception("Sorry, all stations are full")

        # Add the bike into the station, change marker for checked_out status, and set the
        # current station to the one passed
        # lastly, increment the trip counter
        station.add_bike(bike)
        bike.checked_out = False
        bike.current_station = station
        bike.trip_counter += 1

    def show_stations(self):
        """
        Prints a list of all stations
        :return:
        """
        for station in self.stations:
            print station.name

    def add_station(self, station):
        """
        Adds a station to the bike share system
        :param station:
        :return:
        """
        self.stations.append(station)

    """
    HELPER FUNCTIONS
    """
    def get_station_index_by_name(self, station_name):
        """
        Gets index of station by name
        :param station_name:
        :return:
        """
        for idx, station in enumerate(self.stations):
            if station.name == station_name:
                return idx

        return -1

    def get_station_of_bike(self, bike):
        """
        Given a bike, find the station it's at
        :param bike:
        :return:
        """
        for station in self.stations:
            if station.index(bike) > -1:
                return station

        return None

    def get_station_with_bike_slots(self):
        """
        Find a station with bike slots
        :return:
        """
        for station in self.stations:
            if len(station.bikes) < station.bike_slots:
                return station

        return None


class Bike(object):
    """
    Bike Object
    """
    def __init__(self):
        self.trip_counter = 0
        self.checked_out = False
        self.home_station = None
        self.current_station = None

    def set_home_station(self, station):
        """
        Sets home station for bike
        :param station:
        :return:
        """
        self.home_station = station

    def show_trips(self):
        """
        Prints the number of trips for a bike
        :return:
        """
        print self.trip_counter


class Station(object):
    """
    Station Object
    """
    def __init__(self, name, slots=random.choice([3, 5, 10])):
        self.sponsors = list()
        self.bike_slots = slots
        self.bikes = list()
        self.name = name

    def assign_sponsor(self, sponsor):
        """
        Assign the sponsor to this station
        :param sponsor:
        :return:
        """
        self.sponsors.append(sponsor)

    def add_bike(self, bike):
        """
        Adds a bike to this station
        :param bike:
        :return:
        """
        if len(self.bikes) >= self.bike_slots:
            raise Exception("Sorry, we have no more room for bikes here")

        self.bikes.append(bike)

    def remove_bike(self, bike):
        """
        Removes a bike from this station
        :param bike:
        :return:
        """
        if self.bikes.index(bike) == -1:
            raise Exception("Sorry, that bike does not exist in this station")

        del self.bikes[self.bikes.index(bike)]

    def show_sponsors(self):
        """
        Prints a nice list of all sponsors for this station
        :return:
        """
        for idx, sponsor in enumerate(self.sponsors):
            print "{}. {}".format(idx, sponsor.name)


class Sponsor(object):
    """
    Sponsor Object
    """
    def __init__(self, name):
        self.name = name
