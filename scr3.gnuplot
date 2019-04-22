set datafile separator ","
set xlabel "Actual"
set ylabel "Predict"
set xrange [-6.7:-3.5]
set title "Data Set 3"
file = "./predict3.csv"
plot file u 1:2 title "DATA"
replot x title "CORRECT"