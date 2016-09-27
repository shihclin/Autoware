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

path = "../csv/20160922_FirstTest/"


filename = path + "ndt_matching_histogram.csv"
data    = parse_csv(filename)
tmp_0   = np.mean(data)
print "Localization: ", '{:.2f}'.format(np.mean(data)), "ms"

filename = path + "dpm_ocv_detection_histogram.csv"
data    = parse_csv(filename)
tmp_1   = np.mean(data)
print "Detection: ", '{:.2f}'.format(np.mean(data)), "ms"

filename = path + "kf_track_histogram.csv"
data    = parse_csv(filename)
tmp_2   = np.mean(data)
print "Tracking: ", '{:.2f}'.format(np.mean(data)), "ms"

filename = path + "velocity_set_histogram.csv"
data    = parse_csv(filename)
tmp_3   = np.mean(data)
print "Velocity Setting: ", '{:.2f}'.format(np.mean(data)), "us"

filename = path + "angle_set_histogram.csv"
data    = parse_csv(filename)
tmp_4   = np.mean(data)
print "Angle Setting: ", '{:.2f}'.format(np.mean(data)), "us"

final   = tmp_0 + tmp_1 + tmp_2 + (tmp_3/1000) + (tmp_4/1000)
print "End-to-end latency: ", '{:.2f}'.format(final), "ms"

