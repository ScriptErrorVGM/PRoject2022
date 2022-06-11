import pandas as pd

def weight_grades(grades, weights):
    print(grades.dot(weights))
    return grades.dot(weights)

grades = pd.DataFrame(dict(hw1=[3, 2, 2], hw2=[2, 3, 4]), index=['Alice','Claudia','Bob'])

weights = pd.Series([0.75, 0.25], index=['hw2', 'hw1']) 
assert (weight_grades(grades, weights) == pd.Series([2.25, 2.75, 3.5],                                                   
index = ['Alice','Claudia','Bob'])).all()

grades = pd.DataFrame(dict(hw1=[3, 2], hw2=[2, 3], hw3=[0, 1]),                      
index=['Alice', 'Claudia']) 
weights = pd.Series(dict(hw1=0.25, hw2=0.5, hw3=0.25)) 
assert weight_grades(grades, weights).to_dict() == {'Alice': 1.75,'Claudia': 2.25}
