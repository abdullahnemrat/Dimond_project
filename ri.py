import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

x1=[65.9	,65.1,	60.9,	60.2]
y1=[1,2,3,4]
x2=[56.9,	52.7,	47.7,	47.2]
y2=[0.5,1.5,2]
x3=1
y3=[0.7,1.5,2.1]
# plt.plot(y1,x1,"ro-")
# plt.plot(y1,x2,"bv-")
# plt.plot(y1,x3,"yP-")
# plt.title("Improve Heat Transfer with Increased plate")
# plt.xlabel("Distance from center of the duct (mm)")
# plt.ylabel("Temperature (C)")
# plt.legend(["at 0.6","at 1.4","at 2"])
# plt.show()



y1=np.array(y1)
mymodel = np.poly1d(np.polyfit(y1,x1,2))
myline = np.linspace((y1).min(), (y1 ).max(), len(y1))
plt.scatter(y1,x1)
plt.plot(myline, mymodel(myline))

mymodel = np.poly1d(np.polyfit(y1,x2,2))
plt.scatter(y1,x2)
plt.plot(myline, mymodel(myline))

mymodel = np.poly1d(np.polyfit(y1,x3,2))
plt.scatter(y1,x3)
plt.plot(myline, mymodel(myline))
plt.xlim(0,6.2)
plt.ylim(22,80)
plt.title("Temperature Distribution(Fin Plate)")
plt.xlabel("Distance from the flat plate (mm)")
plt.ylabel("Temperature Degree(C)")
plt.legend(["at 0.13","at 1.02","at 2.04"])

plt.show()


