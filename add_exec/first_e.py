import pandas as pd

def get_grade(df, lastname, firstname, course):
    res = df.loc[(df['First Name'] == firstname) & (df['Last Name'] == lastname)]
    return int(res[course])
    

def test(table, columns):    
    df = pd.DataFrame(table, columns=columns)    
    for row in table:        
        firstname = row[columns.index('First Name')]        
        lastname = row[columns.index('Last Name')]        
        for j, course in enumerate(columns[2:], 2):       
            print(row[j])     
            assert get_grade(df, lastname, firstname, course) == row[j]
test(    
    [        
        ['Doe', 'John', 1, 2, 3, 4],         
        ['Smith', 'Alice', 5, 4, 2, 4]    
    ],     
    columns=['Last Name', 'First Name', 'Algebra', 'Calculus', 'Music', 'Law'] 
    )

test(    
    [        
        ['John', 'Doe', 1, 2, 3, 4],         
        ['Max', 'Katz', 5, 4, 2, 4]    
    ],     
    columns=['First Name', 'Last Name', 'Algebra', 'Calculus', 'Music', 'Law'] 
    )

test(    
    [        
        ['John', 'Doe', 1, 2, 3, 4, 3, 2],         
        ['Jennifer', 'Lopez', 5, 4, 2, 4, 1, 1],        
        ['John', 'Smith', 2, 1, 4, 3, 3, 2]    
    ],    
    columns=['First Name', 'Last Name', 'Algebra', 'Calculus', 'Music', 'Law', 'CS', 'P'] 
    )
test(    
    [        
        ['John', 'Doe', 1, 2, 3, 4, 3, 2],         
        ['Jack', 'Doe', 5, 4, 2, 4, 1, 1],        
        ['John', 'Smith', 2, 1, 4, 3, 3, 2]    
    ],    
    columns=['First Name', 'Last Name', 'Algebra', 'Calculus', 'Music', 'Law', 'CS', 'P'] 
    )

