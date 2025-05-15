import pandas as pd
from sqlalchemy import create_engine

#Define drop count
book_drop_count = 0
customer_drop_count = 0

#Read 03_Library Systembook.csv file
book_data = pd.read_csv('Data/03_Library Systembook.csv')

#Drop rows where empty
na_book_drop = book_data.dropna()
book_drop_count +=  len(book_data) - len(na_book_drop)
book_data = book_data.dropna()

#Drop rows where duplicated --- No duplicates?
dup_book_drop = book_data.drop_duplicates()
book_drop_count +=  len(book_data) - len(dup_book_drop)
book_data = book_data.drop_duplicates()

#Change Book checkout data type to datetime - first remove double " and format d/m/y. Also removes wrong dates e.g. 32/05/2023
book_data['Book checkout'] = book_data['Book checkout'].str.strip('"')

book_data['Book checkout'] = pd.to_datetime(
    book_data['Book checkout'],
    format='%d/%m/%Y',
    errors='coerce'
)

subna_book_drop = book_data.dropna()
book_drop_count += len(book_data) - len(subna_book_drop)
book_data = book_data.dropna(subset=['Book checkout'])

#Change Book Returned data type to datetime and format d/m/y.
book_data['Book Returned'] = pd.to_datetime(book_data['Book Returned'], format='%d/%m/%Y')

#Add Loan Duration column
book_data['Loan Duration'] = (book_data['Book Returned'] - book_data['Book checkout']).dt.days

neg_loans = book_data[book_data['Loan Duration'] < 0]
book_drop_count += len(neg_loans)
book_data = book_data[book_data['Loan Duration'] >= 0]

#Read 03_Library SystemCustomers.csv file
customers_data = pd.read_csv('Data/03_Library SystemCustomers.csv')

#Drop rows where empty
na_customer_drop = customers_data.dropna()
customer_drop_count +=  len(customers_data) - len(na_customer_drop)
customers_data = customers_data.dropna()

#Connection details for SQLAlchemy
server = 'localhost'
database = 'LibraryDB'

#Create connection string WITHOUT username and password
connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

#Create engine
engine = create_engine(connection_string)

drop_count = {
    'Record Loss: Books': book_drop_count,
    'Record Loss: Customers': customer_drop_count
}

metrics = pd.DataFrame([drop_count])

#Write data to CSV files
book_data.to_csv('Python/LibraryBooks.csv', index=False)
customers_data.to_csv('Python/LibraryCustomers.csv', index=False)
metrics.to_csv('Python/LibraryMetrics.csv', index=False)

print("Data successfully written to LibraryBooks.csv")
print("Data successfully written to LibraryCustomers.csv")
print("Data successfully written to LibraryMetrics.csv")