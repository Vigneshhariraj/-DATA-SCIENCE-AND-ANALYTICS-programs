'''Data: 
Systolic blood pressures of 14 patients are given below: 
183, 152, 178, 157, 194, 163, 144, 114, 178, 152, 118, 158, 172, 138 
Test, whether the population mean, is less than 165
Hypothesis 
H0: There is no significant mean difference in systolic blood pressure. i.e., μ = 165 
H1: The population mean is less than 165. i.e., μ < 165'''
sys_bp=[183, 152, 178, 157, 194, 163, 144, 114, 178, 152, 118, 158, 172, 138] 
mu=165 
from scipy import stats 
t_value,p_value=stats.ttest_1samp(sys_bp,mu) 
one_tailed_p_value=float("{:.6f}".format(p_value/2)) 
print('Test statistic is %f'%float("{:.6f}".format(t_value))) 
print('p-value for one tailed test is %f'%one_tailed_p_value) 
alpha = 0.05 
if one_tailed_p_value<=alpha: 
    print('Conclusion','n','Since p value(=%f)'%p_value,'<','alpha(=%.2f)'%alpha,'''We 
    reject the null hypothesis H0. So we conclude that there is no significant mean 
    difference in systolic blood pressure. i.e., μ = 165 at %.2f level of significance'''%alpha) 
else: 
    print('Conclusion','Sincep-value(=%f)'%one_tailed_p_value,'>','alpha(=%.2f)'%alpha,'We do not reject the null hypothesis H0.') 