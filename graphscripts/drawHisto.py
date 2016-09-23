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

filename = "angle_set_histogram.csv"
data    = parse_csv(filename)
out_filename = filename[:-3] + "png"


n, bins, patches = plt.hist(data, 100, alpha=0.5, color='orange', label='Angle Setting')
plt.xlabel('Latency (us)')
plt.ylabel('Number')
plt.grid()
plt.legend(loc='upper right')
plt.savefig(out_filename)
#`plt.show()
