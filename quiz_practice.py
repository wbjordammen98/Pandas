import pandas as pd

file_object1 = open('Holiday Schedule Ranking 2019.csv','r')

data = pd.read_csv(file_object1, index_col=0).T

print(data)

file_object1.close()

file_object2 = open('Holiday Schedule Ranking 2019.csv','r')

# Create a dataframe for the final schedule.
schedule = pd.read_csv(file_object2,index_col=0)

for c in schedule.columns:
    schedule[c].values[:] = 0

print(schedule)

data["col_sum"] = data.apply(lambda x:x.sum(), axis=1)

print(data)

data = data.sort_values(by="col_sum",ascending=False)
data = data.T

print(data)

for date in data.columns:
    date_series = data[date].nsmallest(5,keep='all')
    slot_count = 0 # increases shift counter by one for each person

    print(date)
    print(date_series)


schedule.replace(0,'',inplace=True)
#print(schedule)

schedule.to_csv("final_schedule.csv")
