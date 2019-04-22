set datafile separator ","
set xlabel "Actual"
set ylabel "Predict"
set title "Data Set 1"
set xrange [-6.4:-5.0]
set yrange [-6.4:-4.6]
file = "./predict1.csv"
plot file u 1:2 title "DATA"
replot x title "CORRECT"