"""
#Author: Jordan Collier
#This programme tests a compound interest calculator.
#Version: 1.0 14/02/2022
"""
from calc import monthly_compounding

def test_tautology():
    assert 3 == 2 + 1
    
def test_zeros():
    #establish input values
    initial = 0
    monthly = 0
    annual_rate = 0
    years = 0
    # calc an output
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    #test via 0's
    assert final_sum == 0
    
    
def test_cash():
    #e test cash
    initial = 1000
    monthly = 100
    annual_rate = 0
    years = 1
    # calc an output
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    #test via 0's
    assert final_sum == 2200
    
def test_compound():
    #testing adding interest rate
    initial = 1000
    monthly = 100
    annual_rate = 12
    years = 1/12
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    assert final_sum == 1110