#!/usr/bin/python3

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# CSV DATASET from InterSCimulator
TRACE_DATA = '/home/tallys/git/master-research/src/../datasets/car-bus-simulation/output/events_lat_long.csv'
COLUMNS = ['time', 'action', 'vid', 'lat', 'lon']

# Define input size number of rows to be read from the csv into the pandas dataframe
SMALL_1_MILLION = 1000000 #
MEDIUM_10_MILLION = 10000000
BIG_30_MILLION = None
INPUT_SIZE=MEDIUM_10_MILLION

mdf = pd.read_csv(TRACE_DATA, nrows=INPUT_SIZE, names=COLUMNS, delimiter=";", header=None)
       
# All data points from a given vehicle id
def filter_by_id(id):
    return mdf.loc[mdf['vid'] == id]

# The first time a vehicle id registered an action in the simulation
def origin(id):
    return filter_by_id(id).loc[[0]]
        
# The last time a vehicle id registered an action in the simulation
def destiny(id):
    return filter_by_id(id).iloc[[-1]]

tool_tip = lambda x: 'time: ' + str(x["time"]) + ', lat: ' + str(x["lat"]) + ', lon: ' + str(x["lon"])

import geoplotlib

points_df = filter_by_id('4858_52').reset_index()
start = origin('4858_52').reset_index()
end = destiny('4858_52').reset_index()

geoplotlib.dot(start, color="green", point_size=5, f_tooltip=tool_tip)
geoplotlib.dot(end, color="black", point_size=5, f_tooltip=tool_tip)

# Custom layer
from geoplotlib.layers import BaseLayer
from geoplotlib.layers import HotspotManager
from geoplotlib.utils import BoundingBox
from geoplotlib.core import BatchPainter
import random
import time

class DotDensityLayer(BaseLayer):

    def __init__(self, data, color=None, point_size=2, f_tooltip=None):
        """Create a dot density map
        :param data: data access object
        :param color: color
        :param point_size: point size
        :param f_tooltip: function to return a tooltip string for a point
        """
        self.frame_counter = 0
        self.data = data
        self.color = color
        if self.color is None:
            self.color = [255,0,0]
        self.point_size = point_size
        self.f_tooltip = f_tooltip

        self.hotspots = HotspotManager()


    def invalidate(self, proj):
        self.x, self.y = proj.lonlat_to_screen(self.data['lon'], self.data['lat'])



    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        self.painter = BatchPainter()
        x, y = proj.lonlat_to_screen(self.data['lon'], self.data['lat'])
        if self.f_tooltip:
            for i in range(0, len(x)):
                record = {k: self.data[k][i] for k in self.data.keys()}
                self.hotspots.add_rect(x[i] - self.point_size, y[i] - self.point_size,
                                       2*self.point_size, 2*self.point_size,
                                       self.f_tooltip(record))
        self.color= "blue" #random.choice(foo)
        self.painter.set_color(self.color)
        self.painter.points(x[self.frame_counter], y[self.frame_counter], 2*self.point_size, False)
        
        self.painter.batch_draw()
        picked = self.hotspots.pick(mouse_x, mouse_y)
        if picked:
            ui_manager.tooltip(picked)
        self.frame_counter += 1
        time.sleep(0.4)
        if self.frame_counter == len(x):
            self.frame_counter = 0


    def bbox(self):
        return BoundingBox.from_points(lons=self.data['lon'], lats=self.data['lat'])
        
geoplotlib.add_layer(DotDensityLayer(points_df))
#geoplotlib.show()

# Custom layer
# crash on five million
trajectories_graph = mdf

trajectories_graph.loc[:, 'dest_lat'] = trajectories_graph.shift(-1).loc[:, 'lat']
trajectories_graph.loc[:, 'dest_lon'] = trajectories_graph.shift(-1).loc[:, 'lon']
trajectories_graph = trajectories_graph[:-1]

# Edge colors are based on distance between points
geoplotlib.graph(trajectories_graph, src_lat='lat', src_lon='lon', dest_lat='dest_lat', dest_lon='dest_lon', linewidth=80, alpha=255)
geoplotlib.show()
#trajectories[self.frame_counter]
