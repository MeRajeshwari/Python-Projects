import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_student_data = pd.read_csv("studata.csv", header=0, sep=",")

x = full_student_data["latitude"]
y = full_student_data["longitude"]

slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("latitude")
plt.ylabel ("longitude")
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
