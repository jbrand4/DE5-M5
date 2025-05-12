#Read csv file
customers_data = pd.read_csv('Data/03_Library SystemCustomers.csv')

#Drop rows where empty
customers_data = customers_data.dropna()