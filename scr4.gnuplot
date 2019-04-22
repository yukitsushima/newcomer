set datafile separator ","
set xlabel "Actual"
set ylabel "Predict"
set yrange [-6.8:-4.6]
set title "Data Set 4"
file = "./predict4.csv"
plot file u 1:2 title "DATA"
replot x title "CORRECT"