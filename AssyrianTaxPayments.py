def getPairs(filename1, filename2, commodity):
    infile1 = open(filename1, 'r')
    infile2 = open(filename2, 'r')
    useful_tablets = []
    useful_amounts = []
    for line in infile1:
        line1 = infile1.readline()
        for line in infile2
            line2 = infile2.readline()
            if line1[0] = line2[0]
                useful_tablets.append(line1[0])
                useful_amounts.append(line1[commodity])
    return useful_tablets, useful_amounts       
        

def main():
    filename1 = input("Please enter the name of the first province ")
    filename2 = input("Please enter the name of the second province ")
    for commodity in range(1,5):
        tablets, amounts = getPairs(filename1, filename2, commodity)
        print(tablets)
        print(amounts)
