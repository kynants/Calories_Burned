'''
Running on a particular treadmill you will burn 3.9 calories/minute. Design a
program that uses a loop to display the number of calories burned after 10, 15,
20, 25, and 30 minutes.
'''

# Initialized Variables
cal = 3.9
min = 10

# The third number in the range() increments the loop by 5
for min in range(10, 31, 5):
    print("You burned", cal, "calories in", min, "minutes.")
    cal += cal