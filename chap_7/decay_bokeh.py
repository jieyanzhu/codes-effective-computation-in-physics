import numpy as np
# import the Bokeh plotting tools
from bokeh import plotting as bp

# load decays.csv into a NumPy array
decaydata = np.loadtxt('decays.csv', delimiter=',', skiprows=1)

# provide handles for the x and y columns
time = decaydata[:,0]
decays = decaydata[:,1]

# define some output metadata
bp.output_file('decays.html', title='Experiment 1 Radioactivity')

# create a figure with fun Internet-friendly features (optional)
p = bp.figure(tools='pan,wheel_zoom,box_zoom,reset')

# on that figure, create a line plot
p.line(time, decays, x="Time (s)", y='Decays (#)',
    color='#1F78B4', legend='Decays per second')

# open a browser
bp.show(p)
