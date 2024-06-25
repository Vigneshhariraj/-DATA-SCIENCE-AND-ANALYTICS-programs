'''Eleven schoolboys were given a test in Statistics. They were given a Month’s tuition and second 
tests were held at the end of it. Do the marks give evidence that the students have benefited 
from the exam coaching? 
Marks in 1st test: 23 20 19 21 18 20 18 17 23 16 19
Marks in 2nd test: 24 19 22 18 20 22 20 20 23 20 18
Hypothesis 
H0: The students have not benefited from the tuition class. i.e., d = 0 
H1: The students have benefited from the tuition class. i.e., d < 0 
Where, d = x-y; d is the difference between marks in the first test (say x) and marks in the 
second test (say y). '''
alpha = 0.05 
first_test =[23, 20, 19, 21, 18, 20, 18, 17, 23, 16, 19] 
second_test=[24, 19, 22, 18, 20, 22, 20, 20, 23, 20, 18] 
from scipy import stats 
t_value,p_value=stats.ttest_rel(first_test,second_test) 
one_tailed_p_value=float("{:.6f}".format(p_value/2)) 
print('Test statistic is %f'%float("{:.6f}".format(t_value))) 
print('p-value for one_tailed_test is %f'%one_tailed_p_value) 
alpha = 0.05 
if one_tailed_p_value<=alpha: 
    print('Conclusion','n','Since p-value(=%f)'%one_tailed_p_value,'<','alpha(=%.2f)'%alpha,'''We 
    reject the null hypothesis H0.So we conclude that the students have benefited by the tuition 
    class. i.e., d = 0 at %.2f level of significance.'''%alpha) 
else:
    print('Conclusion','n','Since p-value(=%f)'%one_tailed_p_value,'>','alpha(=%.2f)'%alpha,'''We 
    do not reject the null hypothesis H0. So we conclude that the students have not benefited by the 
    tuition class. i.e., d = 0 at %.2f level of significance.'''%alpha)