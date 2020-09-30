import pandas as pd

grades_dict = {'Wally':[87,96,70],'Eva':[100,87,90],
            'Sam':[94,77,90],'Katie':[100,81,82],
            'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

#print(grades)

grades.index = ['Test1','Test2','Test3']

#print(grades)
#print(grades.Sam)
#print(grades.loc[['Test1','Test2'],['Eva','Kate']])
#print(grades.iloc[[0,1],[1,3]])
#print(grades[(grades >= 80) & (grades < 90)])
#print(grades.at['Test2','Eva'])

grades.at['Test2','Eva'] = 100
print(grades)
print(grades.iat[1,2])

grades.iat[1,2] = 87

#print(grades.describe())

pd.set_option('precision',2)
#print(grades.describe())
#print(grades.mean())
#print(grades.T.mean())
#print(grades.sort_index(ascending=False))
#print(grades.sort_index(axis=1)) # axis 1 sorts columns
print(grades.sort_values(by='Test1',axis=1,ascending=False))
print(grades.T.sort_values(by='Test1',ascending=False))
print(grades.loc['Test1'].sort_values(ascending=False))