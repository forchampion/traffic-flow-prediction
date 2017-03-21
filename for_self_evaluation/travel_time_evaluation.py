import csv
from datetime import datetime

#actual file read
actual_result_file = file('testing_actual_results/timewindow_20min_avg_travel_time.csv')
actual_reader = csv.reader(actual_result_file)

first_line = True
route_dict = {}
for line in actual_reader:
    if first_line:
        first_line = False
        continue
    route = line[0] + line[1]
    starttime = line[2].split(',')[0][1:]
    starttime = datetime.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    if route in route_dict:
        route_dict[route][starttime] = float(line[3])
    else:
        new_dict = {}
        new_dict[starttime] = float(line[3])
        route_dict[route] = new_dict

#prediction file read
prediction_file = file('testing_prediction/travel_time.csv')
prediction_reader = csv.reader(prediction_file)
first_line = True
MAPE = 0
for line in prediction_reader:
    if first_line:
        first_line = False
        continue
    route = line[0] + line[1]
    starttime = line[2].split(',')[0][1:]
    starttime = datetime.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    if starttime in route_dict[route]:
        actual_tt = route_dict[route][starttime]
        prediction_tt = float(line[3])
        MAPE += 1./84 * abs((actual_tt-prediction_tt)/actual_tt)

MAPE = MAPE/6.
print "travel time MAPE = ",MAPE
