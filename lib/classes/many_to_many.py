class NationalPark:

    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            print("Cannot change name of national park")
        elif isinstance(name, str) and len(name) >=3:
            self._name = name
        else:
            print("Name must be a string and at least 2 characters")
    
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(visitors, key = visitors.count)
    @classmethod
    def most_visited(cls):
        national_parks = [trip.national_park for trip in Trip.all]
        if len(national_parks) == 0:
            return None
        else:
            return max(national_parks, key = national_parks.count)


class Trip:
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
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            print("Start date must be a string and at least 7 characters long")
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            print("End date must be a string and at least 7 characters long")
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            print("visitor must be of class Visitor")
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else: 
            print("national park must be of class NationalPark")


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
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])