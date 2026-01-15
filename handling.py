
distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft=input("Enter a spacecraft: ").title()
    try:
        au=float(distances[spacecraft])
        m =convert(au)
    
    except KeyError:
        print(f"'{spacecraft}' is'nt in our dictionary")
        return
    except ValueError:
        print(f"can't convert string '{distances[spacecraft]}' into float")
        return


def convert(l):
   
    return l * 149597870700


main()
