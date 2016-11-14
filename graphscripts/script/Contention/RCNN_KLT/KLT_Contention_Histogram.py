import matplotlib.cm as cmx
import matplotlib.colors as cl
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rc("font", family="serif")
plt.rc("font", size=11)
plt.rc("legend", fontsize=11)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(9, 6)


def color_maker(count, map='gnuplot2', min=0.100, max=0.900):
  assert(min >= 0.000 and max <= 1.000 and max > min)
  gran = 100000.0
  maker = cmx.ScalarMappable(norm=cl.Normalize(vmin=0, vmax=int(gran)),
                             cmap=plt.get_cmap(map))
  r = [min * gran]
  if count > 1:
    r = [min * gran + gran * x * (max - min) / float(count - 1) for x in range(0, count)]
  return [maker.to_rgba(t) for t in r]


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
#loc_data    = parse_csv("../../../csv/Contention/SameGPU/RCNN_KLT/rcnn_detect_histogram.csv")
#det_data    = parse_csv("../../../csv/Contention/DifferentGPU/RCNN_KLT/rcnn_detect_histogram.csv")
tra_data    = parse_csv("../../../csv/Contention/SameGPU/RCNN_KLT/klt_track_histogram.csv")
vel_data    = parse_csv("../../../csv/Contention/DifferentGPU/RCNN_KLT/klt_track_histogram.csv")
#ang_data    = parse_csv("../csv/angle_set_histogram.csv")
out_filename = "KLT_Contention.png"

#myList[:] = [x / myInt for x in myList]
#vel_data[:] = [x / 1000.0 for x in vel_data]
#ang_data[:] = [x / 1000.0 for x in ang_data]
color_list = color_maker(4, map="afmhot")

#n, bins, patches = plt.hist(loc_data, 100, alpha=0.5, color='red', label='RCNN Same GPU')
#n, bins, patches = plt.hist(det_data, 100, alpha=0.5, color='blue', label='RCNN Different GPU')
n, bins, patches = plt.hist(tra_data, 100, alpha=0.5, color='red', label='KLT Same GPU')
n, bins, patches = plt.hist(vel_data, 100, alpha=0.5, color='blue', label='KLT Different GPU')
#n, bins, patches = plt.hist(ang_data, 100, alpha=0.5, color='green', label='Angle Setting')

plt.xlabel('Latency (ms)')
#plt.xlim((0,400))
#plt.ylim((0,500))
plt.ylabel('Number')
plt.grid()
plt.legend(loc='upper right')
plt.savefig(out_filename)
#`plt.show()
