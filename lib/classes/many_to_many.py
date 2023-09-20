import statistics
from statistics import mode

class NationalPark:

    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
           raise Exception("Cannot change name of national park")
        elif isinstance(name, str) and len(name) >=3:
            self._name = name
        else:
            raise Exception("Name must be a string and at least 3 characters long")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        park_trips = self.trips()
        if len(park_trips) == 0:
            return None
        else:
            most_visits = 0
            best_vis = []
            for trip in park_trips:
                curr_vis = trip.visitor
                total_vis = len([trip for trip in park_trips if trip.visitor == curr_vis])
                if total_vis > most_visits:
                    most_visits = total_vis
                    best_vis.clear()
                    best_vis.append(curr_vis)
            return best_vis[0]
    @classmethod
    def most_visited(cls):
        return mode([trip.national_park for trip in Trip.all])





class Trip:
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        # start_date = start_date.capitalize()
        # date_Check = start_date.split()
        # if isinstance(start_date, str) and len(start_date) >= 7 and date_Check[0] in Trip.months:
        #     self._start_date = start_date
        # else:
        #     print("Date should be a string and start with the month")
        if isinstance(start_date, str) and len(start_date) >=7:
            self._start_date = start_date
        else:
            raise Exception("Date should be a string and greater than 6 characters")

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        # end_date = end_date.capitalize()
        # date_Check = end_date.split()
        # if isinstance(end_date, str) and len(end_date) >= 7 and date_Check[0] in Trip.months:
        #     self._end_date = end_date
        # else:
        #     print("Date should be a string and start with the month")
        if isinstance(end_date, str) and len(end_date) >=7:
            self._end_date = end_date
        else:
            raise Exception("Date should be a string and greater than 6 characters")
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("visitor must be of class Visitor")
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("park must be of class NationalPark")

        


class Visitor:

    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=15:
            self._name = name
        else:
            raise Exception("name must be a String and between 1 and 15 characters")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])