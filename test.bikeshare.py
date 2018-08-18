from bikeshare import *
import unittest


class BikeShareCreationTest(object):
    """
    Create bike share test
    """
    def __init__(self):
        self.bike_share = BikeShare()

    def test_creating_stations(self):
        print "============================================="
        print "TEST: Creating Stations"
        print "============================================="

        station_1 = Station('North')
        station_2 = Station('South')

        self.bike_share.add_station(station_1)
        self.bike_share.add_station(station_2)

        print "Expected Stations in our bike share system: {}, actual: {}".format(2, len(self.bike_share.stations))
        print ""
        print "Did this test pass? {}".format(len(self.bike_share.stations) == 2)
        print ''

    def test_creating_bikes(self):
        print "============================================="
        print "TEST: Creating Bikes"
        print "============================================="

        bike_1 = Bike()
        bike_2 = Bike()

        self.bike_share.add_bike(bike_1)
        self.bike_share.add_bike(bike_2)

        print "Bike 1's home station is: {}".format(bike_1.home_station.name)
        print "Bike 2's home station is: {}".format(bike_2.home_station.name)
        print ""
        print "Total bikes in system: {}".format(len(self.bike_share.bikes))
        print "Total bikes in all stations: {}".format(self.get_all_bikes_in_all_stations())
        print ""
        print "Did this test pass? {}".format(
            2 == len(self.bike_share.bikes) == self.get_all_bikes_in_all_stations())
        print ''

    def test_creating_sponsors(self):
        print "============================================="
        print "TEST: Creating Sponsors"
        print "============================================="

        sponsor_list = [
            Sponsor('Pizza Hut'),
            Sponsor('Round Table'),
            Sponsor('Taco Bell'),
            Sponsor('Burger King')
        ]

        for i in range(4):
            selected_sponsor = random.choice(self.bike_share.stations)
            selected_sponsor.assign_sponsor(sponsor_list[i])

        print "Total Sponsors: {}".format(len(sponsor_list))
        print "Total Sponsors in all stations: {}".format(self.get_all_sponsors_in_all_stations())
        print ''
        print "Did this test pass? {}".format(len(sponsor_list) == self.get_all_sponsors_in_all_stations())
        print ''

    def get_all_bikes_in_all_stations(self):
        return sum(len(station.bikes) for station in self.bike_share.stations)

    def get_all_sponsors_in_all_stations(self):
        return sum(len(station.sponsors) for station in self.bike_share.stations)


class BikeShareBikeTest(object):
    """
    Create Bike for Bike Share test
    """
    def __init__(self):
        self.bike_share = BikeShare()

    def test_bike_checkout(self):
        print "============================================="
        print "TEST: Creating Bike Checkout"
        print "============================================="
        station_1 = Station('North')

        self.bike_share.add_station(station_1)

        bike_1 = Bike()
        bike_2 = Bike()
        bike_3 = Bike()

        self.bike_share.add_bike(bike_1)
        self.bike_share.add_bike(bike_2)
        self.bike_share.add_bike(bike_3)

        print "Expected Bikes in Station 1: {}, Actual Bikes in Station 1: {}".format(3, len(self.bike_share.stations[0].bikes))
        print 'Checked out Bike 1...'

        self.bike_share.check_out_bike(bike_1, station_1)

        print "Expected Bikes in Station 1: {}, Actual Bikes in Station 1: {}".format(2, len(self.bike_share.stations[0].bikes))
        print 'Expected Bike Checked out Status: {}, Actual Bike checked out Status: {}'.format(True, bike_1.checked_out)
        print ''

    def test_bike_return(self):
        print "============================================="
        print "TEST: Creating Bike Returns"
        print "============================================="
        station_1 = Station('North')

        self.bike_share.add_station(station_1)

        bike_1 = Bike()
        bike_2 = Bike()
        bike_3 = Bike()

        self.bike_share.add_bike(bike_1)
        self.bike_share.add_bike(bike_2)
        self.bike_share.add_bike(bike_3)

        self.bike_share.check_out_bike(bike_1, station_1)
        self.bike_share.return_bike(bike_1, station_1)
        self.bike_share.check_out_bike(bike_1, station_1)
        self.bike_share.return_bike(bike_1, station_1)
        self.bike_share.check_out_bike(bike_1, station_1)
        self.bike_share.return_bike(bike_1, station_1)

        self.bike_share.check_out_bike(bike_2, station_1)
        self.bike_share.return_bike(bike_2, station_1)
        self.bike_share.check_out_bike(bike_2, station_1)
        self.bike_share.return_bike(bike_2, station_1)

        self.bike_share.check_out_bike(bike_3, station_1)

        print "Expected Bikes in Station 1: {}, Actual {}".format(2, len(station_1.bikes))
        print "Expected Trips for Bike 1: {}, Actual: {}".format(3, bike_1.trip_counter)
        print "Expected Trips for Bike 2: {}, Actual: {}".format(2, bike_2.trip_counter)
        print "Expected Trips for Bike 3: {}, Actual: {}".format(0, bike_3.trip_counter)


class BikeShareStationTest(unittest.TestCase):
    """
    Station Tests
    """
    def __init__(self):
        self.bike_share = BikeShare()

    def test_full_station(self):
        print "============================================="
        print "TEST: Creating Bike For Full Station"
        print "============================================="

        station_1 = Station('North', 3)

        self.bike_share.add_station(station_1)

        bike_1 = Bike()
        bike_2 = Bike()
        bike_3 = Bike()
        bike_4 = Bike()

        self.bike_share.add_bike(bike_1)
        self.bike_share.add_bike(bike_2)
        self.bike_share.add_bike(bike_3)

        with self.assertRaises(Exception): self.bike_share.add_bike(bike_4)
        print "Error was thrown: {}".format(True)
        print ""


if __name__ == '__main__':
    sf_bike_share_creation_test = BikeShareCreationTest()
    sf_bike_share_creation_test.test_creating_stations()
    sf_bike_share_creation_test.test_creating_bikes()
    sf_bike_share_creation_test.test_creating_sponsors()

    sf_bike_share_bike_checkout_test = BikeShareBikeTest()
    sf_bike_share_bike_checkout_test.test_bike_checkout()

    sf_bike_share_bike_return_test = BikeShareBikeTest()
    sf_bike_share_bike_return_test.test_bike_return()

    sf_bike_share_station_test = BikeShareStationTest()
    sf_bike_share_station_test.test_full_station()

