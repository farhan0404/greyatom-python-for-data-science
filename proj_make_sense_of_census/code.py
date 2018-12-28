# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
'''Note:

The parameter 'delimiter="," ' is set because file that we are opening has extension 'csv'(Comma Separated Values)

The parameter 'skip_header=1' is set because the first row of the data(which is called header) contains string values but in our numpy array we need only integers(Remember numpy array can only store data of a single data type)'''
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census = np.concatenate((data, new_record))

print(census)


# --------------
#Code starts here
age = census[:,0]
print(age)

max_age = age.max()
print(max_age)

min_age = age.min()
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race = census[:, 2]
#print(race)


race_0 = [ i for i in census[:, :] if i[2] == 0 ]
race_0 = np.array(race_0)
print(race_0)

race_1 = [ i for i in census[:, :] if i[2]  == 1 ]
race_1 = np.array(race_1)

race_2 = [ i for i in census[:, :] if i[2]  == 2 ]
race_2 = np.array(race_2)

race_3 = [ i for i in census[:, :] if i[2]  == 3 ]
race_3 = np.array(race_3)

race_4 = [ i for i in census[:, :] if i[2]  == 4 ]
race_4 = np.array(race_4)

'''
race_0 = np.zeros(2)
print(race_0)
race_1 = np.zeros(1)
race_2 = np.zeros(1)
race_3 = np.zeros(1)
race_4 = np.zeros(1)
'''
#for val in race:
#    print(val)
'''
for val in race:
    if(val == 0.0):
        np.append(race_0, int(val))
    elif(val == 1.0):
        np.append(race_1, int(val))
    elif(val == 2.0):
        np.append(race_2, int(val))
    elif(val == 3.0):
        np.append(race_3, int(val))
    elif(val == 4.0):
        np.append(race_4, int(val))
'''
#print(race_0)
#print(race_1)
#print(race_2)
#print(race_3)
#print(race_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

min_citizen = min(len_0, len_1, len_2, len_3, len_4)

if(min_citizen == len(race_0)):
    minority_race = 0
elif(min_citizen == len(race_1)):
    minority_race = 1
elif(min_citizen == len(race_2)):
    minority_race = 2
elif(min_citizen == len(race_3)):
    minority_race = 3
elif(min_citizen == len(race_4)):
    minority_race = 4

print(minority_race)



# --------------
#Code starts here
senior_citizens = np.asarray([i for i in census if i[0] >60])
#print(senior_citiaens)

#working_hours_array = [ i for i in senior_citizens[:, 6] ]

#print(working_hours_array)
working_hours_sum = senior_citizens[:,6].sum()
print(working_hours_sum)

senior_citizens_len = len(senior_citizens[:,6])

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = np.asarray([ i for i in census if i[1] > 10])
low = np.asarray([ i for i in census if i[1] <= 10])

#print(high)
#print(low)
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()

print(avg_pay_high)
print(avg_pay_low)


