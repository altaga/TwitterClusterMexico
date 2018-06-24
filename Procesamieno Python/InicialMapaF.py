import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

#Geolocalizacion del area de interes

PuntoInicial=[19.27,-99.24]
PuntoFinal=[19.52,-99.02]
Cuadricula=[5,5]
Difer=[(PuntoFinal[0]-PuntoInicial[0])/Cuadricula[0],(PuntoFinal[1]-PuntoInicial[1])/Cuadricula[1]]

MapaPrincipal = folium.Map(location=[(PuntoInicial[0]+PuntoFinal[0])*0.5,(PuntoInicial[1]+PuntoFinal[1])*0.5],zoom_start=13,tiles='cartodbpositron')
marca = folium.CircleMarker(location=[(PuntoInicial[0]+PuntoFinal[0])*0.5,(PuntoInicial[1]+PuntoFinal[1])*0.5]).add_to(MapaPrincipal)


for aa in range(0, Cuadricula[0]):
    for bb in range(0, Cuadricula[1]):
        marca = folium.CircleMarker(location=[PuntoInicial[0]+aa*Difer[0],PuntoInicial[1]+bb*Difer[1]]).add_to(MapaPrincipal)
   
MapaPrincipal.save('MEXA53.html')