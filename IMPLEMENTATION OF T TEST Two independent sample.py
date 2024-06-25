'''Data: 
Compare the effectiveness of ammonium chloride and urea, on the grain yield of paddy, an 
experiment was conducted. The results are given below: 
Ammonium 
chloride (X1) 13.4 10.9 11.2 11.8 14 15.3 14.2 12.6 17 16.2 16.5
 15.7 
Urea (X2) 12 11.7 10.7 11.2 14.8 14.4 13.9 13.7 16.9 16 15.6 16 
Hypothesis 
H0: The effect of ammonium chloride and urea on grain yield of paddy are equal i.e., μ1 = μ2 
H1: The effect of ammonium chloride and urea on grain yield of paddy is not equal i.e., μ1 ≠ μ2 '''
Ammonium_chloride=[13.4,10.9,11.2,11.8,14,15.3,14.2,12.6,17,16.2,16.5,15.7] 
Urea=[12,11.7,10.7,11.2,14.8,14.4,13.9,13.7,16.9,16,15.6,16] 
from scipy import stats 
t_value,p_value=stats.ttest_ind(Ammonium_chloride,Urea) 
print('Test statistic is %f'%float("{:.6f}".format(t_value))) 
print('p-value for two tailed test is %f'%p_value) 
alpha = 0.05 
if p_value<=alpha: 
    print('Conclusion','n','Since p-value(=%f)'%p_value,'<','alpha(=%.2f)'%alpha,'''We reject the 
    null hypothesis H0. So we conclude that the effect of ammonium chloride and urea on grain 
    yield of paddy are not equal i.e., μ1 = μ2 at %.2f level of significance.'''%alpha) 
else: 
    print(
        'Conclusion\n'
        'Since p-value(=%f)' % p_value, '>', 'alpha(=%.2f)' % alpha,
        'We do not reject the null hypothesis H0.'
    )  