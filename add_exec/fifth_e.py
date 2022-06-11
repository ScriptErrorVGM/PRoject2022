import pandas as pd
import numpy as np

def mean_by_gender(grades, genders) :
    df = pd.DataFrame({'col1' : genders.values, 'col2' : grades.values})
    gp = df.groupby('col1')['col2'].median().to_dict()
    return gp
    

def test(a, b, c): 
    assert mean_by_gender(pd.Series(a), pd.Series(b)) == c

assert (mean_by_gender(pd.Series([5, 5, 3, 5, 2], index=['Alice', 'Bob', 'Dan', 'Claudia', 'John']),
                       pd.Series(["male", "female",  "male", "female", "male"], index=['Bob', 'Alice', 'Dan', 'Claudia', 'John'])) == {'female': 5, 'male': 3})
test([1, 0]*10, ['female', 'male']*10, {'female': 1, 'male': 0})
test(range(100), ['female', 'male'] * 50, {'female': 49.0, 'male': 50.0})
test(list(range(100))+[100], ['male']*100 +
     ['female'], {'male': 49.5, 'female': 100.0})
