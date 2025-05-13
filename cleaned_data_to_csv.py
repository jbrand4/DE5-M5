import pandas as pd
from sqlalchemy import create_engine

#Read 03_Library Systembook.csv file
book_data = pd.read_csv('Data/03_Library Systembook.csv')

#Drop rows where empty
book_data = book_data.dropna()

#Drop rows where empty
book_data = book_data.drop_duplicates()

#Change Book checkout data type to datetime - first remove double " and format d/m/y. Also removes wrong dates e.g. 32/05/2023
book_data['Book checkout'] = book_data['Book checkout'].str.strip('"')
book_data['Book checkout'] = pd.to_datetime(
    book_data['Book checkout'],
    format='%d/%m/%Y',
    errors='coerce'
)
book_data = book_data.dropna(subset=['Book checkout'])

#Change Book Returned data type to datetime and format d/m/y.
book_data['Book Returned'] = pd.to_datetime(book_data['Book Returned'], format='%d/%m/%Y')

#Assuming date input error where Book checkout > Book Returned - swap rows where affected
bad_dates = book_data['Book Returned'] < book_data['Book checkout']
book_data.loc[bad_dates, ['Book checkout', 'Book Returned']] = book_data.loc[bad_dates, ['Book Returned', 'Book checkout']].values

#Read 03_Library SystemCustomers.csv file
customers_data = pd.read_csv('Data/03_Library SystemCustomers.csv')

#Drop rows where empty
customers_data = customers_data.dropna()

#Write data to CSV files
book_data.to_csv('Python/LibraryBooks.csv', index=False)
customers_data.to_csv('Python/LibraryCustomers.csv', index=False)

print("Data successfully written to LibraryBooks.csv")
print("Data successfully written to LibraryCustomers.csv")