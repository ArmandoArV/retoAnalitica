import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from StatistaP import Changefrequencies, PriceUSA
from StatistaP import ChangeUSA
from StatistaP import DatesUSA
from StatistaP import usa
from StatistaP import PriceOF
from StatistaP import ChangeOF
from StatistaP import DatesOF

plt.style.use('grayscale')   # https://matplotlib.org/3.5.0/gallery/style_sheets/grayscale.html


x = DatesUSA
y = PriceUSA
y1 = ChangeUSA

ex1 = DatesOF
ye1 = PriceOF

plt.plot(x,y)
plt.xlabel("Fechas de 2005 a 2008")
plt.ylabel("Costos")
plt.xlim(500,50)
plt.title("BAJA CON RESPECTO A LOS COSTOS DE 2009 - 2008")
plt.show()

plt.plot(x,y1)
plt.xlabel("Fechas de 2005 a 2008")
plt.ylabel("Costos")
plt.xlim(500,50)
plt.title("BAJA CON RESPECTO A LOS COSTOS DE 2009 - 2008")
plt.show()