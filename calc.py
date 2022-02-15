"""
#Author: Jordan Collier
#This programme calculates a compound interest.
#Version: 1.0 14/02/2022

"""
"""
def test_compound():
    #testing adding interest rate
    initial = 1000
    monthly = 100
    annual_rate = 12
    years = 1/12
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    assert final_sum == 1110
"""

def monthly_compounding(initial, monthly, annual_rate, years): 
    
    final_sum = initial
    
    months = years * 12
    
    for month in range(int(months)):
        
        
        
       final_sum = final_sum*(1 + annual_rate/1200) + monthly
        
    
    
    return final_sum
    
