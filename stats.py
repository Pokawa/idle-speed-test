import sys
import plotly.express as px
import pandas
import datetime

data = pandas.read_csv(filepath_or_buffer=sys.argv[1], header=0, error_bad_lines=False, warn_bad_lines=False)
data['time'] = pandas.to_datetime(data['time'])
data['download'] = data['download'] / 1000000
data['upload'] = data['upload'] / 1000000


if (sys.argv[2] == 'day'):
    data = data[data['time'] > datetime.datetime.now() - datetime.timedelta(days=1)]

if (sys.argv[2] == 'week'):
    data = data[data['time'] > datetime.datetime.now() - datetime.timedelta(weeks=1)]

if (sys.argv[2] == 'month'):
    data = data[data['time'] > datetime.datetime.now() - datetime.timedelta(weeks=4)]

print("Max/Min/Mean download: {:.2f}/{:.2f}/{:.2f} Mb/s".format(data['download'].max(), data['download'].min(), data['download'].mean()))
print("Max/Min/Mean upload: {:.2f}/{:.2f}/{:.2f} Mb/s".format(data['upload'].max(), data['upload'].min(), data['upload'].mean()))
print("Max/Min/Mean ping: {:.2f}/{:.2f}/{:.2f} ms".format(data['ping'].max(), data['ping'].min(), data['ping'].mean()))


