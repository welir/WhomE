__author__ = 'Voronin Denis'

import sl4a
import time
import types


droid = sl4a.Android()
Marks = types.SimpleNamespace()
Marks.name = ''
Marks.shirota = 0.0
Marks.dolgota = 0.0
Marks.coordinate = ''
class Mark:


    def get_coordinate(self):
        self.droid.startLocating()
        time.sleep(15)
        loc = self.droid.readLocation().result
        if loc == {}:
          loc == self.droid.getLastKnownLocation().result
        if loc != {}:
          try:
            n = loc['gps']
          except KeyError:
            n = loc['network']
          la = n['latitude']
          lo = n['longitude']
          address = self.droid.geocode(la, lo).result
          self.droid.stopLocating()
          print(address)
          return  address

    def set_coordinate(self):
        global Marks
        Marks.name = 'hh'
        Marks.shirota = 1.1
        Marks.dolgota = 1.1
        Marks.coordinate = self.get_coordinate()
        print(Marks)


chel = Mark()


chel.set_coordinate()