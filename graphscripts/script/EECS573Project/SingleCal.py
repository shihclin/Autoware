import numpy as np


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

filename = "ndt_matching_histogram.csv"


loc_data    = parse_csv(filename)
tmp_0   = np.mean(loc_data)
me_0    = np.median(loc_data)
loc_95  = np.percentile(loc_data,95)
loc_99  = np.percentile(loc_data,99)

print "Mean"
print "Localization: ", '{:.2f}'.format(tmp_0), "ms"
print "Median"
print "Localization: ", '{:.2f}'.format(me_0), "ms"
print "95% "
print "Localization: ", '{:.2f}'.format(np.percentile(loc_data,95)), "ms"
print "99% "
print "Localization: ", '{:.2f}'.format(np.percentile(loc_data,99)), "ms"
