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


filename = "rcnn_detect_histogram.csv"
csv_filename = filename
graph_filename = filename
#csv_filename = "../../../csv/RCNN_LOC/" + filename
#graph_filename = "../../../graph/EECS573/" + filename
data    = parse_csv(csv_filename)
out_filename = graph_filename[:-3] + "png"


n, bins, patches = plt.hist(data, 100, alpha=0.5, color='blue', label='RCNN Detection')
plt.xlabel('Latency (ms)')
plt.ylabel('Number')
plt.grid()
plt.legend(loc='upper right')
plt.savefig(out_filename)
plt.show()
