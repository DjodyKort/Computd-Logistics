# ========= Imports =========
import time
import datetime
# ======== Functions ========

def ProgramQuit():
    # ======= Start Function =======
    input("Press enter to quit...")
    quit()


def ConvertToDateTime(raw_date):
    # ======= Start Function =======
    return datetime.datetime.strptime(raw_date, "%d-%m-%Y %H:%M:%S")


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
        print("Error: Invalid date format. Please use the format dd-mm-yyyy hh:mm:ss")
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