import numpy as np
import math
import matplotlib.pyplot as plt
from StatistaP import Changefrequencies, PriceUSA
from StatistaP import ChangeUSA
from StatistaP import DatesUSA

plt.style.use('grayscale')   # https://matplotlib.org/3.5.0/gallery/style_sheets/grayscale.html


x = DatesUSA
y = PriceUSA
y1 = ChangeUSA


plt.plot(x,y)
plt.xlabel("Fechas de 2008 a 2009")
plt.ylabel("Costos")
plt.xlim(500,50)
plt.title("Ecuación lineal")
plt.show()


plt.hist(y1,bins=[Changefrequencies])
plt.xlabel("Fechas de 2008 a 2009")
plt.ylabel("Tasa de interes")
plt.xlim(500,50)
plt.title("Ecuación lineal")
plt.show()
