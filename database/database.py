import pandas as pd
from sqlalchemy import create_engine
# MySQL Connection Details
HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "root"
DATABASE = "crime_analytics"

# Create MySQL Connection
engine = create_engine(
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

print("Connected to MySQL Successfully!")

# Read CSV File
df = pd.read_csv("crime_dataset_india (1).csv")

print(df.head())

# Upload Dataset to MySQL
df.to_sql(
    name="crime_data",
    con=engine,
    if_exists="replace",   # replace table if already exists
    index=False
)

print("Dataset Imported Successfully!")
