from dice import Die
import pytest

def prob_double_roll(x, n):
    """
    Expected probabilities for the sum of two dice.
    """
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.

    return (n - abs(x - (n + 1))) / n ** 2
    
@pytest.mark.parametrize("sides,rolls",[(5,5000000),(8,8000000)])
def test_double_roll(sides,rolls):

    die= Die(sides)
    
    
    
    # store the expected probability 
    expect={}
    for i in range(2,sides*2+1):
        expect[i]=prob_double_roll(i,sides)
        
    tally= {}
    #initialise the tally
    for key in expect:
        tally[key]=0
        
    for i in range(rolls):
        rsum=die.roll()+die.roll()
        
        tally[rsum]+=1
    for i in range(2,sides*2+1):
        
        assert tally[i]/rolls == pytest.approx(expect[i],rel=1e-2)





def test_valid_roll():
    """ Test that a die roll is valid """
    
    die= Die()
    
    # Roll the die.
    roll=die.roll()
    
    # check that the value is valid
    assert roll > 0 and roll < 7

def test_always_valid_roll():
    """ Test that a die roll is always valid"""
    
    die= Die()
    
    for i in range(10000):
        roll= die.roll()
        
        assert roll> 0 and roll < 7
        
def test_average():
    """ Test that the average die roll is correct. """
    
    die = Die()
    
    # work out the expected average
    expect = sum(range(1,7))/6
    
    # to calculate the total of rolls
    total = 0
    
    rolls =10000
    
    for i in range(0, rolls):
        total+= die.roll()
        
    average= total/rolls
    
    assert average == pytest.approx(3.5,rel=1e-2)
    
def test_fair():
    """ Test that a dice is fair. """
    die = Die()
    
    # Set the number of rolls
    rolls = 1000000
    
    # Create a dictionary keep tally
    tally={}
    for i in range(1,7):
        tally[i] =0
    #Roll the dice 'rolls' times
    for i in range(0,rolls):
        tally[die.roll()]+=1
        
    # Assert that the probability is correct
    for i in range(1,7):
        assert tally[i]/rolls == pytest.approx(1/6, 1e-2)
    