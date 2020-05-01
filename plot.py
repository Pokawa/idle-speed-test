import sys
import plotly.express as px
import pandas

data = pandas.read_csv(filepath_or_buffer=sys.argv[1], header=0, error_bad_lines=False, warn_bad_lines=False)
#from bits to megabits
data['download'] = data['download'] / 1000000
data['upload'] = data['upload'] / 1000000
xaxis = range(len(data))

fig = px.line(data, x=xaxis, y="upload", hover_name="time", hover_data=["server name", "ping"], )
fig.show()
fig = px.line(data, x=xaxis, y="download", hover_name="time", hover_data=["server name", "ping"])
fig.show()