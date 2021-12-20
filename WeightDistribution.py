import pandas as pd
import csv 
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("HeightWeight.csv")
weightlist=df["Weight"].tolist()
meanweight=statistics.mean(weightlist)
modeweight=statistics.mode(weightlist)
medianweight=statistics.median(weightlist)
stdevweight=statistics.stdev(weightlist)
print("Mean: ", meanweight)
print("Mode: ", modeweight)
print("Median: ", medianweight)
print("Standard Deviation: ", stdevweight)
graph=ff.create_distplot([df["Weight"].tolist()], ["Weightdistribution"], show_hist=False)
graph.show()