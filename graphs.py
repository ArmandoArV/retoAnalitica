import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from StatistaP import Changefrequencies, PriceSIX, PriceUSA
from StatistaP import ChangeUSA
from StatistaP import DatesUSA
from StatistaP import usa
from StatistaP import PriceOF
from StatistaP import ChangeOF
from StatistaP import DatesOF
from StatistaP import PriceSIX

plt.style.use('grayscale')   # https://matplotlib.org/3.5.0/gallery/style_sheets/grayscale.html


x = DatesUSA
y1 = PriceUSA
y2 = ChangeUSA

ex1 = DatesOF
ye1 = PriceOF
ye2 = PriceSIX

plt.plot(x,y1)
plt.xlabel("Fechas de 2005 a 2008")
plt.ylabel("Costos")
plt.xlim(500,50)
plt.title("BAJA CON RESPECTO A LOS COSTOS DE 2009 - 2008")
plt.show()

plt.plot(x,y2)
plt.xlabel("Fechas de 2005 a 2008")
plt.ylabel("Costos")
plt.xlim(500,50)
plt.title("BAJA CON RESPECTO A LOS COSTOS DE 2009 - 2008")
plt.show()

plt.subplot(221) 
plt.plot(x, y1, y2)
plt.xlabel("Fechas")
plt.ylabel("Precios")
plt.title("Precios")
plt.show()

plt.subplot(222) 
plt.plot(ex, ye1,ye2)
plt.xlabel("Fechas")
plt.ylabel("Precios")
plt.title("Precios")
plt.show()