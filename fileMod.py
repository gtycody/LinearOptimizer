import csv

csvFile = open("playerdata.csv","r")
reader = csv.reader(csvFile)
playerlists = list(reader)

BPRQB = 99999
BPRWR = 99999
BPRTE = 99999
BPRDST = 99999
BPRK= 99999
BPRFLEX= 99999
BPRRB1 = 99999
BPRRB2 = 99999


used = list()

print(type(float(playerlists[1][5])))

for i in playerlists:
    if i[2] == "DST" and float(i[5]) < BPRDST: #DST 1
        BPRDST = float(i[5])
        BDST = i
print(BDST)

for i in playerlists:
    if i[2] == "K" and float(i[5]) < BPRK: #DST 1
        BPRK = float(i[5])
        BK = i
print(BK)

for i in playerlists:
    if i[2] == "TE" and float(i[5]) < BPRTE: #DST 1
        BPRTE = float(i[5])
        BTE = i
print(BTE)

for i in playerlists:
    if i[2] == "QB" and float(i[5]) < BPRQB: #DST 1
        BPRQB = float(i[5])
        BQB = i
print(BQB)

for i in playerlists:
    if i[2] == "RB" and float(i[5]) < BPRRB1:
        BPRRB1 = float(i[5])
        BRB1 = i
    if i[2] == "RB" and float(i[5]) < BPRRB2 and BRB1 is not i:
        BPRRB2 = float(i[5])
        BRB2 = i

print(BRB1) 
print(BRB2)











