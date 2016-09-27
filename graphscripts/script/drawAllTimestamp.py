#!/usr/bin/env python

import warnings
#import seaborn
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import matplotlib.cm as cmx
import matplotlib.colors as cl

from matplotlib.ticker import FuncFormatter

plt.rc("font", family="serif")
plt.rc("font", size=11)
plt.rc("legend", fontsize=11)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(9, 6)

"""
Function to format percentage numbers
"""
def to_percentage(y, position):
  v = str(100 * y)
  if matplotlib.rcParams["text.usetex"] is True:
    return v + r"$\%$"
  else:
    return v + "%"

# map is the name of one of the colormaps from
# http://matplotlib.org/1.2.1/examples/pylab_examples/show_colormaps.html
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

  raw_data = {}
  legend_labels = []
  for line in lines:
    items = line.strip().split(",")
    legend_labels.append(items[0])
    x = []
    y = []
    for item in items[1:]:
      tup = item.strip().split(" ")
      x.append(float(tup[0]))
      y.append(float(tup[1]))
    raw_data[items[0]] = {}
    raw_data[items[0]]["x"] = x
    raw_data[items[0]]["y"] = y

  return raw_data, legend_labels

# FIXME: Change the file name to plot
localization = "ndt_matching_timeseries.csv"
detection = "dpm_ocv_detection_timeseries.csv"
tracking = "kf_track_timeseries.csv"
velocity_set = "velocity_set_timeseries.csv"
angle_set = "angle_set_timeseries.csv"


#if filename == "line_graph.csv":
#  warnings.warn("line_graph.csv contains only bogus data, you should change "
#                "the filename to plot the data you want. (search for FIXME in "
#                "the code)")

#data, legend_labels = parse_csv(filename)
loc_data, loc_labels = parse_csv(localization)
det_data, det_labels = parse_csv(detection)
tra_data, tra_labels = parse_csv(tracking)
vel_data, vel_labels = parse_csv(velocity_set)
ang_data, ang_labels = parse_csv(angle_set)


#myList[:] = [x / myInt for x in myList]
vel_data[vel_labels[0]]["y"][:] = [ x / 1000.0 for x in vel_data[vel_labels[0]]["y"]]
ang_data[ang_labels[0]]["y"][:] = [ x / 1000.0 for x in ang_data[ang_labels[0]]["y"]]


ax = plt.subplot(1, 1, 1)

#NUM_LINES = len(legend_labels)

# configs
#color_list = color_maker(NUM_LINES, map="brg")
color_list = color_maker(5, map="jet")


#for j in 5:
#    for i in range(NUM_LINES):
#        ax.plot(data[legend_labels[i]]["x"], data[legend_labels[i]]["y"], "-",
#            color=color_list[j], label=legend_labels[i], lw=1)

ax.plot(loc_data[loc_labels[0]]["x"], loc_data[loc_labels[0]]["y"], "-",
        color=color_list[0], label=loc_labels[0], lw=1)
ax.plot(det_data[det_labels[0]]["x"], det_data[det_labels[0]]["y"], "-",
        color=color_list[1], label=det_labels[0], lw=1)
ax.plot(tra_data[tra_labels[0]]["x"], tra_data[tra_labels[0]]["y"], "-",
        color=color_list[2], label=tra_labels[0], lw=1)
ax.plot(vel_data[vel_labels[0]]["x"], vel_data[vel_labels[0]]["y"], "-",
        color=color_list[3], label=vel_labels[0], lw=1)
ax.plot(ang_data[ang_labels[0]]["x"], ang_data[ang_labels[0]]["y"], "-",
        color=color_list[4], label=ang_labels[0], lw=1)


#ax.axhline(y=490, color='red', linestyle='--', lw=1)
# x-axis and y-axis labels
ax.set_xlabel("Time (s)")
ax.set_ylabel("Latency (ms)")
#ax.set_yticks(np.arange(0, 400, 50))

# legend
#ax.legend(loc="center right")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), fancybox=True, ncol=5)

# title
#ax.set_title("Timestamp")

# grid
ax.yaxis.grid()

out_filename = "Timestamp" + ".png"

plt.savefig(out_filename)
#plt.show()
