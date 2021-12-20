import pandas as pd
import csv 
import plotly.figure_factory as ff

df=pd.read_csv("HeightWeight.csv")
heightlist=df["Height"].tolist()
meanheight=statistics.mean(heightlist)
modeheight=statistics.mode(heightlist)
medianheight=statistics.median(heightlist)
stdevheight=statistics.stdev(heightlist)
print("Mean: ", meanheight)
print("Mode: ", modeheight)
print("Median: ", medianheight)
print("Standard Deviation: ", stdevheight)
graph=ff.create_distplot([df["Height"].tolist()], ["Heightdistribution"], show_hist=False)
graph.show()