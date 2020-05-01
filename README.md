# Idle SpeedTest Service

Bash script that let's you perform background speedtests for your wifi netwowork.
And python script to plot the results

## Getting Started

Bash script requires **speedtest-cli** package

```
sudo apt-get install speedtest-cli
``` 

Python script requires **pandas** and **plotly** modules

```
sudo pip install pandas plotly
```

To download the scripts:

```
git clone https://github.com/Pokawa/idle-speed-test idle-speed-test
```

## Usage 

Bash script saves the results in .csv with given format
```
time,server name,ping,download,upload
```
each file is associated with different wifi network and it's name is wifi's ssid

To setup tests in the backgorund. Second argument is number of minutes between each test.
```
./speed_test.sh setup 5
```

To stop scheduled tests.
```
./speed_test.sh remove 
```

To perform test manually.
```
./speed_test.sh test
```

To plot results 
```
python plot.py yourssid.csv
```