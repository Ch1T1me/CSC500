'using nested loops to collect data and calculate avg rainfall'

# input gathering
years = int(input('Enter number of years:\n'))
months = ['January', 'February', 'March', 'April', 
          'May', 'June', 'July', 'August', 
          'September', 'October','November', 'December']
# initiate total rainfall
total_rainfall = 0

# setting boundaries / data collection
for year in range(years): # outer loop for each year
    print(f'Year {year + 1}')
    for month in months: # inner loop for each month
        rainfall = float(input('Enter the inches of rainfall ' \
                                f'for {month}:\n'))
        total_rainfall += rainfall
#calculate months
total_months = years * 12
# calculate average rainfall per month
if total_months > 0:
    avg_rainfall = total_rainfall / total_months
else:
    avg_rainfall = 0

# print statements
print(f'Total number of months: {total_months}')
print(f'Total inches of rainfall: {total_rainfall}')
print(f'Average rainfall per month: {avg_rainfall:.2f}')

# singular and plural
if years == 1:
    print(f'Data was collected for {years} year.')
else:
    print(f'Data was collected for {years} years.')