# ========= Imports =========
import time
import datetime
import pandas as pd
# ======== Functions ========

def ProgramQuit():
    # ======= Start Function =======
    input("Press enter to quit...")
    quit()


def ConvertToDateTime(raw_date):
    # ======= Start Function =======
    return datetime.datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")


def ConvertToUnix(date):
    # ======= Start Function =======
    return int(time.mktime(date.timetuple()))


def ConvertDateToTimeDifference(orderDate, deliveryDate):
    # ===== Declaring Variables =====
    # Converting the raw date to a Python datetime object
    try:
        dateOrderPlaced_processed = ConvertToDateTime(orderDate)
        dateOrderDelivered_processed = ConvertToDateTime(deliveryDate)
    except ValueError:
        print("Error: Invalid date format. Please use the format yyyy-dd-mm hh:mm:ss")
        ProgramQuit()

    # Converting the datetime object to a Unix timestamp
    dateOrderPlaced_Unix = ConvertToUnix(dateOrderPlaced_processed)
    dateOrderDelivered_Unix = ConvertToUnix(dateOrderDelivered_processed)

    # ======= Start Function =======
    timeDifference = dateOrderDelivered_Unix - dateOrderPlaced_Unix
    # Converting to days
    timeDifference = timeDifference / 86400

    # Returning the time difference
    return timeDifference


def AddTimeDifferenceToCSV(df, csv_doc):
    # ======= Declaring Variables =======
    # Variables
    counternumber = 0

    # csv's
    csv_doc = csv_doc
    csv_doc_new = "./csv/OrdersCleanedNew2.csv"
    excel_doc_new = "./excel/OrdersCleanedNew2.xlsx"
    # ======= Start Function =======

    # Making a new column in the df if it doesn't exist already
    try:
        # making the df['Time Difference in Days'] to an excel readable decimal
        df['Time Difference in Days'] = float(0.0)
    except:
        print("Column already exists")
    
    # Converting the 'Date Placed' and 'Date Delivered to' columns to a time difference
    for index, row in df.iterrows():
        # ==== Declaring Variables ====
        orderDate = row['Date Placed']
        deliveryDate = row['Date Delivered']

        # Increasing the counternumber
        counternumber += 1

        # The actual converting
        timeDifference = round(ConvertDateToTimeDifference(orderDate, deliveryDate), 2)

        # Adding the time difference to the df
        df.at[index, 'Time Difference in Days'] = timeDifference

    # Saving the new df to a new csv file
    df.to_csv(csv_doc_new, index=False)
    df.to_excel(excel_doc_new, index=False)