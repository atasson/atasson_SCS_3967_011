# Defining the mean() function to calculate a list average

 

def mean(x):

    mean = sum(x) / len(x)

    return mean

 

X = 10

list_1 = [8, 19, 10, 12]

 

print(f"The average of the list is {mean(list_1)}")

 

list_2 = []

 

for i in list_1:

    list_2.append(i*X)

 

print(f"The average of the list when multiplied by {X} is {mean(list_2)}")