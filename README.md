# Calculating-R

A python program which computes the correlation coefficient  R , which is a measure of how well the data fits a straight line. The equation for determining $R$ for the $n$ data points in the input file is as follows:
### <center>$R = \frac{a - b}{cd} \mbox{,  where } a = (n) \sum_{i=0}^{n-1} x_i y_i \mbox{, } b = (\sum_{i=0}^{n-1} x_i)(\sum_{i=0}^{n-1} y_i) $</center>

and

### <center>$c = \sqrt{(n) \sum_{i=0}^{n-1} x_i^2 - (\sum_{i=0}^{n-1} x_i)^2}, ~~~d = \sqrt{(n) \sum_{i=0}^{n-1} y_i^2 - (\sum_{i=0}^{n-1} y_i)^2}$</center><br><br>
