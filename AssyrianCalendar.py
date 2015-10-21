def main():
    print("This program calculates the shift in the Assyrian calendar")
    k77 = 30
    k78 = 37
    k79 = 4
    k80 = 6
    k81 = 5
    k82 = 13
    k83 = 46
    k84 = 1
    k85 = 1
    k86 = 18
    k87 = 39
    solar = 365.24
    lunar = 354.37
    yearlist = [k87, k86, k85, k84, k83, k82, k81, k80, k79, k78, k77]
    TPIshift = 5.9 #in months
    stop = "y"
    while stop == "y":
        listyes = input("would you like a list of kings? (y/n) ")
        if listyes == "y":
            print("no. 77 Salmaneser I {0} years".format(k77))
            print("no. 78 Tukulti-Ninurta I {0} years".format(k78))
            print("no. 79 Assur-nadin-aple {0} years".format(k79))
            print("no. 80 Adad-nerari III {0} years".format(k80))
            print("no. 81 Enlil-Kudurri-usur {0} years".format(k81))
            print("no. 82 Ninurta-apil-Ekur {0} years".format(k82))
            print("no. 83 Assur-dan I {0} years".format(k83))
            print("no. 84 Ninurta-Tukulti-Assur {0} year".format(k84))
            print("no. 85 Mutakkil-Nusku {0} year".format(k85))
            print("no. 86 Assur-resa-isi I {0} years".format(k86))
            print("no. 87 Tiglath-pileser I {0} years".format(k87))
        kNumber = eval(input("Please enter the number of the king: "))
        kYear = eval(input("Please enter the year number of that king: "))
        king = 87 - kNumber
        yearshift = 0
        if king <= 0:
            yearshift = 1 - kYear
            dayshift = ( TPIshift*29.5 - 10.88*yearshift)
        else:
            if king > 1:
                for i in range(king-1):
                    yearshift = yearshift + yearlist[i+1]
            yearshift = yearshift + yearlist[king] - kYear + 1
            dayshift = (TPIshift*29.5 + 10.88*yearshift)
        totalmonthshift =dayshift/29.5
        monthshift = totalmonthshift%12
        print("Add {0:0.2f} months to convert to the Babylonian Month".format(monthshift))
        print("That is {0} years before the reign of Tiglath-pileser I".format(yearshift))
        stop = input("Repeat (y/n): ")
main()
