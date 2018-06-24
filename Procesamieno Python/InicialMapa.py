import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
marker = folium.CircleMarker(location=[40.738, -73.98])
marker.add_to(folium_map)

bike_data = pd.read_csv("JC-201805-citibike-tripdata.csv")
bike_data["Start Time"] = pd.to_datetime(bike_data["starttime"])
bike_data["Stop Time"] = pd.to_datetime(bike_data["stoptime"])
bike_data["hour"] = bike_data["Start Time"].map(lambda x: x.hour)
locations = bike_data.groupby("start station id").first()
locations = locations.loc[:, ["start station latitude","start station longitude","start station name"]]

subset = bike_data[bike_data["hour"]<=5]
departure_counts =  subset.groupby("start station id").count()
# select one column
departure_counts = departure_counts.iloc[:,[0]]
# and rename that column
departure_counts.columns= ["Departure Count"]
trip_counts = departure_counts.join(locations)


for index, row in trip_counts.iterrows():
    net_departures = (row["Departure Count"])
    radius = net_departures/20
    if net_departures>0:
        color="#E37222" # tangerine
    else:
        color="#0A8A9F" # teal
        
        folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
marker = folium.CircleMarker(location=[40.738, -73.98])
marker.add_to(folium_map)
    
    folium.CircleMarker(location=[row["start station latitude"],
                                  row["start station longitude"]],
                        radius=radius,
                        color=color,
                        fill=True).add_to(folium_map)


folium_map.save('mappp.html')