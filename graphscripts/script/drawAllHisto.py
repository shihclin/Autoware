import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines
 
def parse_csv(filename):
    lines = read_file(filename)
    raw_data = []
    for line in lines:
        items = line.strip().split(",")
        for item in items:
            raw_data.append(float(item))
    return raw_data

loc_data    = parse_csv("../csv/KLT_tracking_test_1/klt_track_histogram.csv")
det_data    = parse_csv("../csv/KLT_tracking_test_2/klt_track_histogram.csv")
tra_data    = parse_csv("../csv/KLT_tracking_test_3/klt_track_histogram.csv")
#vel_data    = parse_csv("../csv/velocity_set_histogram.csv")
#ang_data    = parse_csv("../csv/angle_set_histogram.csv")
out_filename = "KLT_track_timestamp.png"

#myList[:] = [x / myInt for x in myList]
#vel_data[:] = [x / 1000.0 for x in vel_data]
#ang_data[:] = [x / 1000.0 for x in ang_data]


n, bins, patches = plt.hist(loc_data, 100, alpha=0.5, color='blue', label='1')
n, bins, patches = plt.hist(det_data, 100, alpha=0.5, color='red', label='2')
n, bins, patches = plt.hist(tra_data, 100, alpha=0.5, color='yellow', label='3')
#n, bins, patches = plt.hist(vel_data, 100, alpha=0.5, color='orange', label='Velocity Setting')
#n, bins, patches = plt.hist(ang_data, 100, alpha=0.5, color='green', label='Angle Setting')

plt.xlabel('Latency (ms)')
plt.xlim((0,200))
plt.ylim((0,900))
plt.ylabel('Number')
plt.grid()
plt.legend(loc='upper right')
plt.savefig(out_filename)
#`plt.show()
