import csv
import random
import pandas as pd
import statistics as st
import plotly.figure_factory as pff
import plotly.graph_objects as pgo

fil= pd.read_csv('medium_data.csv')

tmp= fil['reading_time'].tolist()

mean=st.mean(tmp)
sd=st.stdev(tmp)

print(mean)
print(sd)


ds=[]

def de():
 for i in range(0,30):
     rnd= random.randint(0,len(tmp)-1)
     val = tmp[rnd]
     ds.append(val)
 
 dsm= st.mean(ds)
 dsd = st.stdev(ds)

 return dsm
 return dsd

def setup():
    meanlist=[]
    for i in range(0,100):
        setmeans= de()
        meanlist.append(setmeans)
    
    print(st.mean(meanlist))
    grap= pff.create_distplot([meanlist],['name'],show_hist=False)
    grap.add_trace(pgo.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='mean'))
    grap.show()

setup()