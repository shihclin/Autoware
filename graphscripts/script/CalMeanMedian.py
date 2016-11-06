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

path = "../csv/gpu/"

'''
filename = path + "ndt_matching_histogram.csv"
loc_data    = parse_csv(filename)
tmp_0   = np.mean(loc_data)
me_0    = np.median(loc_data)
loc_95  = np.percentile(loc_data,95)
loc_99  = np.percentile(loc_data,99)


filename = path + "dpm_ocv_detection_histogram.csv"
det_data    = parse_csv(filename)
tmp_1   = np.mean(det_data)
me_1    = np.median(det_data)
det_95  = np.percentile(det_data,95)
det_99  = np.percentile(det_data,99)
'''
filename = path + "kf_track_histogram.csv"
tra_data    = parse_csv(filename)
tmp_2   = np.mean(tra_data)
me_2    = np.median(tra_data)
tra_95  = np.percentile(tra_data,95)
tra_99  = np.percentile(tra_data,99)
'''
filename = path + "velocity_set_histogram.csv"
vel_data    = parse_csv(filename)
tmp_3   = np.mean(vel_data)
me_3    = np.median(vel_data)
vel_95  = np.percentile(vel_data,95)
vel_99  = np.percentile(vel_data,99)


filename = path + "angle_set_histogram.csv"
ang_data    = parse_csv(filename)
tmp_4   = np.mean(ang_data)
me_4    = np.median(ang_data)
ang_95  = np.percentile(ang_data,95)
ang_99  = np.percentile(ang_data,99)


final   = tmp_0 + tmp_1 + tmp_2 + (tmp_3/1000) + (tmp_4/1000)
median_final = me_0 + me_1 + me_2 + (me_3/1000) + (me_4/1000)
final_95    = loc_95 + det_95 + tra_95 + (vel_95/1000) + (ang_95/1000)
final_99    = loc_99 + det_99 + tra_99 + (vel_99/1000) + (ang_99/1000)
'''

print tmp_2, me_2, tra_95, tra_99
'''
print "Mean"

print "Localization: ", '{:.2f}'.format(tmp_0), "ms"
print "Detection: ", '{:.2f}'.format(tmp_1), "ms"
print "Tracking: ", '{:.2f}'.format(tmp_2), "ms"
print "Velocity Setting: ", '{:.2f}'.format(tmp_3), "us"
print "Angle Setting: ", '{:.2f}'.format(tmp_4), "us"
print "End-to-end mean latency: ", '{:.2f}'.format(final), "ms", "\n"


print "Median"
print "Localization: ", '{:.2f}'.format(me_0), "ms"
print "Detection: ", '{:.2f}'.format(me_1), "ms"
print "Tracking: ", '{:.2f}'.format(me_2), "ms"
print "Velocity Setting: ", '{:.2f}'.format(me_3), "us"
print "Angle Setting: ", '{:.2f}'.format(me_4), "us"
print "End-to-end median latency: ", '{:.2f}'.format(median_final), "ms", "\n" 



print "95% "
print "Localization: ", '{:.2f}'.format(np.percentile(loc_data,95)), "ms"
print "Detection: ", '{:.2f}'.format(np.percentile(det_data,95)), "ms"
print "Tracking: ", '{:.2f}'.format(np.percentile(tra_data,95)), "ms"
print "Velocity Setting: ", '{:.2f}'.format(np.percentile(vel_data,95)), "us"
print "Angle Setting: ", '{:.2f}'.format(np.percentile(ang_data,95)), "us"
print "End-to-end 95% latency: ", '{:.2f}'.format(final_95), "ms", "\n" 


print "99% "
print "Localization: ", '{:.2f}'.format(np.percentile(loc_data,99)), "ms"
print "Detection: ", '{:.2f}'.format(np.percentile(det_data,99)), "ms"
print "Tracking: ", '{:.2f}'.format(np.percentile(tra_data,99)), "ms"
print "Velocity Setting: ", '{:.2f}'.format(np.percentile(vel_data,99)), "us"
print "Angle Setting: ", '{:.2f}'.format(np.percentile(ang_data,99)), "us"
print "End-to-end 99% latency: ", '{:.2f}'.format(final_99), "ms", "\n" 
'''

