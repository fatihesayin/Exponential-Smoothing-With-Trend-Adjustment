# Exponential-Smoothing-With-Trend-Adjustment
Based on the exponential smoothing with trends method, implement a python code, which will perform the exponential smoothing method and calculate the optimal alpha and beta values minimizing
a) MAD
b) MSE
c) MAPE
You should calculate 3 different alpha and beta values for each error measure separately.
You will read your paramters from an input file called input.txt. An example input.txt is given as an attachment
Input.txt file format:
1) The first value will be number of actual sales observed.
2) The second value is the initial F(0) value.
3) The third value is the initial T(0) value.
4) The remaining numbers are the actual sales data in sorted order.

From this data you should calculate:
Optimal alpha and beta values minimzing three measures separately.
You should try all numbers between 0 and 1 in steps of 0.05 for each alpha and beta values.
The output of the code should be:
1) optimal alpha and beta values minimizing MAD and the related MAD,MSE,MAPE values for this alpha and beta values
2) optimal alpha and beta values minimizing MSE and the related MAD,MSE,MAPE values for this alpha and beta values
3) optimal alpha and beta values minimizing MAPE and the related MAD,MSE,MAPE values for this alpha and beta values

You don't need to round F(t) and T(t) values you have calculated but you have to round FIT(t) values to the nearest integer.
