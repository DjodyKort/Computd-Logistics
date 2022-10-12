# ====== Imports ======
# Local
from py.functions import *
# Packages

# ============ Declaring Variables ============
oderDate_raw =      "31-1-2021  17:45:00"
deliveryDate_raw =  "14-2-2021  04:37:00"

# ========= Start Program =========
if __name__ == "__main__":
    timeDifference = round(ConvertDateToTimeDifference(oderDate_raw, deliveryDate_raw), 2)

    print(f"Time difference is: {timeDifference} days")