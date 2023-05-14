import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fitter import Fitter

from bokeh.plotting import figure
from bokeh.io import output_file, show, curdoc
from bokeh.models import ColumnDataSource, Slider, Select
from bokeh.layouts import column, row, widgetbox
from bokeh.io import output_notebook
from bokeh.plotting import output_notebook
from bokeh.sampledata import iris
output_notebook()

data = iris.flowers
data.head()

##Figure
fig1=figure(title="Iris set")
source=ColumnDataSource(data)
fig1.scatter(x="sepal_length", y="sepal_width", source=source)


def updated_plot(atrr, old, new):
    new_selection=select1.value
    new=data[data["species"]==new_selection]
    source.data=new

##Select option
list_flowers=list(data["species"].unique())
select1=Select(value="setosa", options=list_flowers)
select1.on_change("value", updated_plot)
layout=row(fig1, select1)


#show(layout)
curdoc().add_root(layout)