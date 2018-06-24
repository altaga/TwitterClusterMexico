import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import numpy

#Geolocalizacion del area de interes

PuntoInicial=[19.27,-99.24]
PuntoFinal=[19.52,-99.02]
Cuadricula=[5,5]
Difer=[(PuntoFinal[0]-PuntoInicial[0])/Cuadricula[0],(PuntoFinal[1]-PuntoInicial[1])/Cuadricula[1]]
Negativ=numpy.matrix('0 0.2 0.4 1 0.2; 0.3 0.25 0 0.01 0.8; 0.4 0 0.2 0.1 0.4 ; 0.7 0.1 0 0.2 0.1; 0.4 0.6 0.5 0.1 0.2')   


MapaPrincipal = folium.Map(location=[(PuntoInicial[0]+PuntoFinal[0])*0.5,(PuntoInicial[1]+PuntoFinal[1])*0.5],zoom_start=13,tiles='cartodbpositron')

for aa in range(0, Cuadricula[0]-1):
    for bb in range(0, Cuadricula[1]-1):
        marca = folium.CircleMarker(location=[PuntoInicial[0]+aa*Difer[0],PuntoInicial[1]+bb*Difer[1]],radius=40*Negativ[aa,bb],color='#f44242',fill_color='#f44242',fill=True).add_to(MapaPrincipal)

MapaPrincipal.save('MEXA64.html')