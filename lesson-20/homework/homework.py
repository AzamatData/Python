# Homework 1:
# Using chinook.db write pandas code.
# 1.	Customer Purchases Analysis:
# •	Find the total amount spent by each customer on purchases (considering invoices).
import sqlite3
import pandas as pd

with sqlite3.connect('chinook.db') as connection:
    query = """
    SELECT InvoiceId, InvoiceDate, BillingAddress, BillingCity,
    BillingState, BillingCountry, BillingPostalCode, Total, customers.CustomerId, FirstName, LastName, Company, Address, City, State, Country,
    PostalCode, Phone, Fax, Email, SupportRepId
    FROM invoices
    INNER JOIN customers ON invoices.CustomerId = customers.CustomerId

    """

    df = pd.read_sql_query(query, connection)   

total_amount = df.groupby('CustomerId')['Total'].sum().reset_index()

total_amount


# •	Identify the top 5 customers with the highest total purchase amounts.
total_amount['rank'] = total_amount['Total'].rank(ascending=False, method='dense')
total_amount.sort_values(by = 'rank', inplace=True)
total_amount.head()
# •	Display the customer ID, name, and the total amount spent for the top 5 customers.
total_amount = (
    df.groupby(['CustomerId', 'FirstName', 'LastName'])['Total']
      .sum()
      .reset_index()
      .rename(columns={'Total': 'TotalSpent'})
)

top5 = total_amount.sort_values(by='TotalSpent', ascending=False).head(5)

top5


# 2.	Album vs. Individual Track Purchases:
# •	Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
import pandas as pd
import sqlite3

# Connect to the Chinook database
conn = sqlite3.connect('chinook.db') # Replace 'chinook.db' with your database file path

# Load relevant tables into DataFrames
invoiceline_df = pd.read_sql_query("SELECT * FROM invoice_items", conn)
track_df = pd.read_sql_query("SELECT * FROM tracks", conn)
album_df = pd.read_sql_query("SELECT * FROM albums", conn)

# Close the connection
conn.close()


merged_df = pd.merge(invoiceline_df, track_df, on='TrackId')


invoice_album_counts = merged_df.groupby(['InvoiceId', 'AlbumId']).size().reset_index(name='TracksInInvoice')


total_album_tracks = track_df.groupby('AlbumId').size().reset_index(name='TotalAlbumTracks')


album_purchase_check = pd.merge(invoice_album_counts, total_album_tracks, on='AlbumId')


album_purchases = album_purchase_check[album_purchase_check['TracksInInvoice'] == album_purchase_check['TotalAlbumTracks']]


album_purchase_invoice_lines = merged_df[merged_df['InvoiceId'].isin(album_purchases['InvoiceId']) & 
                                        merged_df['AlbumId'].isin(album_purchases['AlbumId'])]

all_invoice_line_ids = invoiceline_df['InvoiceLineId']

album_purchase_line_ids = album_purchase_invoice_lines['InvoiceLineId']


individual_track_purchases_df = invoiceline_df[~invoiceline_df['InvoiceLineId'].isin(album_purchase_line_ids)]
num_album_tracks = album_purchase_invoice_lines.shape[0]
num_individual_tracks = individual_track_purchases_df.shape[0]

print(f"Number of tracks purchased as part of albums: {num_album_tracks}")
print(f"Number of tracks purchased individually: {num_individual_tracks}")


total_tracks = num_album_tracks + num_individual_tracks
if total_tracks > 0:
    perc_album_tracks = (num_album_tracks / total_tracks) * 100
    perc_individual_tracks = (num_individual_tracks / total_tracks) * 100
    print(f"Percentage of tracks purchased as part of albums: {perc_album_tracks:.2f}%")
    print(f"Percentage of tracks purchased individually: {perc_individual_tracks:.2f}%")

