# ===== Imports =====
# Local imports
from functions import *

# Packages
import pandas as pd
# ========== Declaring Variables ==========
csv_doc = './csv/OrdersCleanedNew.csv'

# ========= Start Program =========
# Read csv file
df = pd.read_csv(csv_doc)

# Putting the time difference in a new column
AddTimeDifferenceToCSV(df, csv_doc)

print(df)


