from math import sqrt
def getPairs(filename1, filename2, com, assessments1, assessments2):
    infile1 = open(filename1, 'r')
    useful_tablets = []
    useful_amounts1 = []
    useful_amounts2 = []
    for line1 in infile1:
        line1list = line1.split('\t')
        infile2 = open(filename2, 'r')
        for line2 in infile2:
            line2list = line2.split('\t')
            if line1list[0] == line2list[0] and line1list[com] != 'x'and line1list[com] != 'x\n' and line2list[com] != 'x' and line2list[com] != 'x\n':
               useful_tablets.append(line1list[0])
               useful_amounts1.append(eval(line1list[com])/assessments1[com-1])
               useful_amounts2.append(eval(line2list[com])/assessments2[com-1])
    return useful_tablets, useful_amounts1, useful_amounts2

def main():
    Province_names = ['Arbail', 'Kilizu', 'Halahhu', 'Talmussu', 'Idu',
                      'Katmuhhu', 'Sudu', 'Taidu', 'Amasakku', 'Kulishinas',
                      'Assur', 'UpperProvince', 'LowerProvince', 'Tursan',
                      'Libbiale', 'Ninua', 'Kurda', 'Apku', 'Addarik',
                      'Karana', 'Sibanibe', 'Hissutu', 'Simi', 'Husananu',
                      'Kalhu', 'Sa-sille', 'Sumela']
    assessments_list = [['Arbail', 29530, 188, 1770, 1160,],
                        ['Kilizu', 9710, 77, 770, 580],
                        ['Halahhu', 28030, 180, 1540, 1260],
                        ['Talmussu', 13560, 77, 770, 580],
                        ['Idu', 13560, 77, 770, 580],
                        ['Katmuhhu', 27860, 187, 1870, 2150],
                        ['Sudu', 7710, 66, 660, 70],
                        ['Taidu', 0, 88, 880, 590],
                        ['Amasakku', 0, 66, 660, 670],
                        ['Kulishinas', 0, 33, 330, 320],
                        ['Assur', 0, 88, 880, 890],
                        ['UpperProvince', 0, 180, 1800, 910],
                        ['LowerProvince', 14560, 88, 880, 90],
                        ['Tursan', 17560, 110, 1100, 440],
                        ['Libbiale', 12560, 100, 1000, 90],
                        ['Ninua', 0, 20, 200, 0],
                        ['Kurda', 0, 66, 660, 470],
                        ['Apku', 0, 66, 660, 270],
                        ['Addarik', 0, 66, 660, 270],
                        ['Karana', 0, 66, 660, 270],
                        ['Sibanibe', 0, 66, 660, 270],
                        ['Hissutu', 0, 66, 660, 270],
                        ['Simi',6030, 44, 440, 310],
                        ['Husananu', 11710, 88, 880, 360],
                        ['Kalhu', 6350, 44, 440, 60],
                        ['Sa-sille', 0, 11, 110, 110],
                        ['Sumela', 0, 0, 0, 150]]
    Province1 = input("Please enter the name of the first province ")
    Province2 = input("Please enter the name of the second province ")
    index1 = Province_names.index(Province1)
    index2 = Province_names.index(Province2)
    assessments1 = assessments_list[index1][1:5]
    assessments2 = assessments_list[index2][1:5]
    filename1 =  Province1 + '.py'
    filename2 =  Province2 + '.py'
    differences = []
    commodity_list = ['grain', 'honey', 'sesame', 'fruit']
    for commodity in range(1,5):
        if assessments1[commodity-1] == 0 or assessments2[commodity-1] == 0:
            average = 0
        else:
            #print()
            #print(commodity_list[commodity-1])
            useful_tablets, useful_amounts1, useful_amounts2 = getPairs(filename1, filename2, commodity, assessments1, assessments2)
            #print("texts", '\t\t', Province1, '\t\t', Province2)
            #for i in range(len(useful_tablets)):
            #    print("{0} \t {1:0.3} \t\t {2:0.3}".format(useful_tablets[i], useful_amounts1[i], useful_amounts2[i]))
            total = 0
            for i in range(len(useful_amounts1)):
                total = total + abs(useful_amounts1[i]- useful_amounts2[i])
            average = total/len(useful_amounts1)
            differences.append(average)
        grandAverage = 0
    for i in range(len(differences)):
        grandAverage = grandAverage + differences[i]
    print("The grand average for {0} and {1} is".format(Province1, Province2),
          round(grandAverage/4,3))
    
main()
