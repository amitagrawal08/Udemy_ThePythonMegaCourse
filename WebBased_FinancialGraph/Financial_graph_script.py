from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start=datetime.datetime(2016,3,2)
end=datetime.datetime(2016,10,8)
#type(data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end))
df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

date_increase=df.index[df.Close > df.Open]
date_decrease=df.index[df.Close < df.Open]

def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else:
        value="Equal"
    return value

df["status"]=[inc_dec(c,o) for c,o in zip (df.Close,df.Open)]
df["Middle"]=(df.Close+df.Open)/2
df["Height"]=abs(df.Close-df.Open)
df

p=figure(x_axis_type='datetime',width=1200,height=400)
p.title.text="CandleStick Chart"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, color='black')

p.rect(df.index[df["status"]=="Increase"],df.Middle[df["status"]=="Increase"], hours_12,
       df.Height[df["status"]=="Increase"], fill_color="#CCFFFF", line_color="black")

p.rect(df.index[df["status"]=="Decrease"],df.Middle[df["status"]=="Decrease"], hours_12,
       df.Height[df["status"]=="Decrease"], fill_color="#FF3333", line_color="black")


#output_file("CS.html")
#show(p)

script1, div1 = components(p)

cdn_js=CDN.js_files
cdn_css=CDN.css_files

## pip install virtualenv
## python -m venv virtual


