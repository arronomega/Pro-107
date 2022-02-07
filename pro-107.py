import pandas as pd
import plotly.express as px
import csv
import plotly.graph_objects as go

df = pd.read_csv("lvl.csv")
df['level'].value_counts()
df['attempt'].value_counts()
print(df.groupby('level')["attempt"].mean())
fig1 =px.scatter(df,x ="student_id",y = "level" ,color = "attempt",size_max = 67)
 fig1.show()
