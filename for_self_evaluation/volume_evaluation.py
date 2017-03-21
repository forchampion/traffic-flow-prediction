import csv
from datetime import datetime

#actual file read
actual_result_file = file('testing_actual_results/timewindow_20min_avg_volume.csv')
actual_reader = csv.reader(actual_result_file)

first_line = True
tollgate_dict = {}
for line in actual_reader:
    if first_line:
        first_line = False
        continue
    tollgate = line[0] + line[2]
    starttime = line[1].split(',')[0][1:]
    starttime = datetime.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    if tollgate in tollgate_dict:
        tollgate_dict[tollgate][starttime] = float(line[3])
    else:
        new_dict = {}
        new_dict[starttime] = float(line[3])
        tollgate_dict[tollgate] = new_dict

for key in tollgate_dict:
    print key, tollgate_dict[key]
#prediction file read
prediction_file = file('testing_prediction/volume.csv')
prediction_reader = csv.reader(prediction_file)
first_line = True
MAPE = 0
for line in prediction_reader:
    if first_line:
        first_line = False
        continue
    tollgate = line[0] + line[2]
    starttime = line[1].split(',')[0][1:]
    starttime = datetime.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    actual_tt = tollgate_dict[tollgate][starttime]
    prediction_tt = float(line[3])
    #print actual_tt, prediction_tt, len(tollgate_dict[tollgate])
    MAPE += 1./len(tollgate_dict[tollgate]) * abs((actual_tt-prediction_tt)/actual_tt)

MAPE = MAPE/5.
print "volume MAPE = ",MAPE
