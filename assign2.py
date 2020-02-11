# Answer-1
import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

import requests

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    

links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

url_gdp = links['GDP']
print(url_gdp)

df_gdp=pd.read_csv(url_gdp)

#Answer-2
print("Head GDP")
print(df_gdp.head())

#Answer-3
url_employ=links['unemployment']

df_unemploy = pd.read_csv(url_unemploy)

print(df_unemploy.head())

#Answer-3
df_employ2 = df_unemploy[df_unemploy['unemployment'] > 8.5]
print(df_employ2)

#Answer-4
x=df_unemploy['date']
print(x)

gdp_change=df_gdp['change-current']
print(gdp_change)

unemployment=df_unemploy["unemployment"]
print(unemployment)


title="Analyzing US Economic Data"


file_name = "index.html"

make_dashboard(x, gdp_change, unemployment, title, file_name)

