# input for time of day
current_time = int(input('Enter the current time (0-23):\n'))

# alarm set to go off in 50 hrs
alarm = current_time + 50

# adjust for if greater than 24
if alarm >= 24:
    alarm %= 24

# print
print(f'''If it is currently {current_time}:00, 
      after 50hrs your alarm will go off at {alarm}:00''')