# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import logging as log

# Mobility trace for the city of São Paulo
# URL: http://interscity.org/open_data/
# ZIP FILE: https://www.dropbox.com/s/hatzbujfspte12i/car-bus-simulation.zip?dl=0#

# CSV DATASET from InterSCimulator
TRACE_DATA = './datasets/car-bus-simulation/output/events_lat_long.csv'
COLUMNS = ['time', 'action', 'vid', 'lat', 'lon']

'''
Geo data manipulation of the interscity simulator
'''
class GeoData():
    def __init__(self):
        self.dataset = None
        self.scheme = {"id": 'vid'}

    # load the simulation trace
    def read_csv(self, file, nrows=None, delimiter=';', columns=None):
        print("file: %s" % file)
        print("nrows: %s" % nrows)
        print("delimiter: %s" % delimiter)
        print("columns: %s" % colunms)
        if not columns:
            log.warning("No column names was specified, first raw will be used instead")
        df = pd.read_csv(file, names=columns, delimiter=delimiter, nrows=nrows)
        self.dataset = df
        return self.dataset

    # return the list of attributes in the given dataset
    def attributes(self):
        if self.dataset.empty:
            return list(self.dataset)
        else:
            log.error("Cannot list attributes of empty dataset.")

    # All data points from a given vehicle id
    def filter_by_id(self, id):
        df = self.dataset.loc[self.dataset['vid'] == id]
        return df

    # The first time a vehicle id registered an action in the simulation
    def origin(self, id):
        df = self.filter_by_id(id)
        df = df.loc[[0]]
        return df

    # The last time a vehicle id registered an action in the simulation
    def destiny(self, id):
        df = self.filter_by_id(id)
        df = df.loc[[0]]
        return df

if __name__ == "__main__":
    log.info("GeoBundler, query, filder and cluster your geodata with power")

def test_check():
    assert True
