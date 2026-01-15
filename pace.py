
def main():
   pace = get_pace(miles=26.2, minutes=-1)
   
   print(f"You need to run each mile in {round(pace, 2)} minutes.")


def get_pace(miles, minutes):
    # if  minutes < 0: #this one rejects only negative numbers
    if not min > 0 : # rejects both 0 and negative numbers

        raise ValueError("please input valid minute")   
    

    return minutes / miles


main()
