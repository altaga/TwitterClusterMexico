import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

map_2 = folium.Map(location=[45.5236, -122.6750],
                   tiles='Stamen Toner',
                   zoom_start=13)
folium.Marker([45.5244, -122.6699],
              popup='The Waterfront'
             ).add_to(map_2)
folium.CircleMarker([45.5215, -122.6261],
                    radius=500,
                    popup='Laurelhurst Park',
                    color='#3186cc',
                    fill_color='#3186cc',
                   ).add_to(map_2)
map_2
map_2.save('map31.html')