set title 'Decays'
set ylabel 'Decays'
set xlabel 'Time (s)'
set grid
set term svg
set output 'plot_gnuplot.svg'
plot 'decays.csv' every ::1 using 1:2 with lines lt rgb 'blue'


