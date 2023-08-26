import numpy as np

# Load the CSV file using numpy's genfromtxt function
data = np.genfromtxt('customers-100.csv', delimiter=',', names=True, dtype=None)

# Access data using column names
#print(data['Date'])       # Access the 'Date' column
print(data['Country'])    # Access the 'Country' column
print(data['Company'])  # Access the 'Confirmed' column
#print(data['Recovered'])  # Access the 'Recovered' column
#print(data['Deaths'])     # Access the 'Deaths' column
