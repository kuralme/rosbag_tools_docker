#!/usr/bin/env python
# coding: utf-8

from bagpy import bagreader
import bagpy
import pandas as pd
import matplotlib.pyplot as plt


rosbag = bagreader('rosbag.bag')

# Read Laser Data
laserdat = rosbag.laser_data()
laser = pd.read_csv(laserdat[0])

# Read Velocity Data and Plot
veldat = rosbag.vel_data()
vel = pd.read_csv(veldat[0])
vel.columns.values[1:].tolist()
fig, ax = bagpy.create_fig(1)
ax[0].scatter(x='Time', y='linear.x', data=vel)
plt.show()
bagpy.animate_timeseries(vel['Time'], vel['linear.x'], title='Velocity Timeseries')


# Read Standard Messages
msgdat = rosbag.std_data()
data = pd.read_csv(msgdat[0])

# Read odometry Data
odomdat = rosbag.odometry_data()
odom = pd.read_csv(odomdat[0])

# Read Wrench Data
wrenchdat = rosbag.wrench_data()
wrench = pd.read_csv(wrenchdat[0])
# Plot wrench
# fig, ax = bagpy.create_fig(1)
# ax[0].scatter(x='Time', y='force.x', data=wrench, s= 6, c = 'Time', cmap = "winter")
# plt.show()


# Get the plots
rosbag.plot_odometry()
rosbag.plot_vel()
rosbag.plot_wrench()

# Animate Velocity Timeseries
bagpy.animate_timeseries(vel['Time'], vel['linear.x'], title='Velocity Timeseries Plot')



