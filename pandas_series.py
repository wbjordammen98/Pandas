import pandas as pd

grade = pd.Series([87,100,94])

print(grade)

myarray = pd.Series(98.6, range(3))

#print(myarray)
#print(grades[0])

#print(grade.describe())

grades = pd.Series([87,100,94], index=['Wally','Eva','Sam'])

grades = pd.Series({'Wally':87, 'Eva':100, 'Sam': 94})

print(grades['Eva'])
print(grades.Eva)

hardware = pd.Series(['Hammer','Saw','Wrench'])

a = hardware.str.contains('a')

print(a)

b = hardware.str.upper()

print(b)

