import streamlit as st
import numpy as np
import pandas as pd
import geopandas
from bokeh.plotting import figure
from bokeh.io import show
from matplotlib import pyplot as plt
import pandas_bokeh
pandas_bokeh.output_file("sweden.html")

world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
germany = world[world.name=="Germany"]
germany.plot()
plt.axis("off")
st.pyplot()

cities = pd.DataFrame({
	'City':["Berlin", "Stuttgart", "Frankfurt", "Hamburg", "Munich", "Dortmund"],
	'Country':["Germany", "Germany", "Germany", "Germany", "Germany", "Germany"],
	'Latitude':[52.51, 48.78, 50.11, 53.57, 48.15, 51.51],
	'Longitude':[13.4, 9.18, 8.68, 10.01, 11.58, 7.46]
})

gdf = geopandas.GeoDataFrame(cities, geometry=geopandas.points_from_xy(cities.Longitude, cities.Latitude))
ax = world[world.name=="Germany"].plot(color="white", edgecolor='k')
plt.axis("off")
# ax = germany.plot(color="white", edgecolor="black")
for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf.City):
	if label == "Berlin":
		ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points", size=15)
	else:
		ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
gdf.plot(ax=ax, color="red")
st.pyplot()

p = figure(title="Indian Railway Map")
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None


ax = world[world.name=="India"].plot(color="white", edgecolor='k')
plt.axis("off")
rails = geopandas.read_file("/Users/mehuljangir/Downloads/IND_rrd/IND_rails.shp")
rails.plot_bokeh()