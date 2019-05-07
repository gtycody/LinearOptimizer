import csv

csvFile = open("playerdata.csv","r")
reader = csv.reader(csvFile)
playerlists = list(reader)

class player:
    def getBestDst(self,playerlists,used):
        BPRDST = 99999
        for i in playerlists :
            if i[2] == "DST" and float(i[5]) < BPRDST and i not in used:  # DST 1
                BPRDST = float(i[5])
                BDST = i
        print(BDST)
        return BDST

    def getBestK(self,playerlists,used):
        BPRK = 99999
        for i in playerlists:
            if i[2] == "K" and float(i[5]) < BPRK and i not in used:  # K 1
                BPRK = float(i[5])
                BK = i
        print(BK)
        return BK

    def getBestTE(self,playerlists,used):
        BPRTE = 99999
        for i in playerlists:
            if i[2] == "TE" and float(i[5]) < BPRTE and i not in used:  # TE 1
                BPRTE = float(i[5])
                BTE = i
        used.append(BTE)
        print(BTE)
        return BTE

    def getBestQB(self,playerlists,used):
        BPRQB = 99999
        for i in playerlists:
            if i[2] == "QB" and float(i[5]) < BPRQB and i not in used:  # QB 1
                BPRQB = float(i[5])
                BQB = i
        print(BQB)
        return BQB

    def getBestRB1(self,playerlists,used):
        BPRRB1 = 99999
        for i in playerlists:
            if i[2] == "RB" and float(i[5]) < BPRRB1 and i not in used:  # RB 1
                BPRRB1 = float(i[5])
                BRB1 = i
        used.append(BRB1)
        print(BRB1)
        return BRB1

    def getBestRB2(self,playerlists,used):

        BPRRB2 = 99999
        for i in playerlists:
            if i[2] == "RB" and float(i[5]) < BPRRB2 and i not in used:  # RB 1
                BPRRB2 = float(i[5])
                BRB2 = i
        used.append(BRB2)
        print(BRB2)
        return BRB2

    def getBestWR1(self,playerlists,used):
        BPRWR1 = 99999
        for i in playerlists:
            if i[2] == "WR" and float(i[5]) < BPRWR1 and i not in used:  # WR 1
                BPRWR1 = float(i[5])
                BWR1 = i
        used.append(BWR1)
        print(BWR1)
        return BWR1

    def getBestWR2(self,playerlists,used):
        BPRWR2 = 99999
        for i in playerlists:
            if i[2] == "WR" and float(i[5]) < BPRWR2 and i not in used:  # WR 1
                BPRWR2 = float(i[5])
                BWR2 = i
        used.append(BWR2)
        print(BWR2)
        return BWR2

    def getBestFLEX(self,playerlists,used):
        BPRFLEX = 99999
        for i in playerlists:
            if (i[2] == "WR" or i[2] =="TE" or i[2] == "RB") and float(i[5]) < BPRFLEX and i not in used:  # FLEX 1
                BPRFLEX = float(i[5])
                BFLEX = i
        print(BFLEX)
        return BFLEX

    def getBestSwap(self,playerlists,list1,direction):
        list2 = list()
        if direction == 1:
            for i in list1:
                store = i
                for j in playerlists:
                    if (i[2] == j[2] and i[0] is not j[0]) and j[3] > i[3]:
                        store = j
                        break
                list2.append(store)


        elif direction == -1:
            for i in list1:
                store = i
                for j in playerlists:
                    if (i[2] == j[2] and i[0] is not j[0]) and j[3] < i[3]:
                        store = j
                        break
                list2.append(store)
            p1.printList(list2)
            print("---------------------------")
            list2.pop()
            for j in playerlists:
                if (j[2] == "WR" or j[2] == "RB" or j[2] == "TE")and j[0] is not list1[-1][0] and j[3] < list1[-1][3]:
                    list2.append(j)
                    break
            p1.printList(list2)

        return list2

    def Compare(self,list1,list2,direction):
        store = 99999
        idstore = 99999
        if direction == -1:
            for i in range(len(list1)):
                if list1[i][3] == list2[i][3]:
                    pass
                else:
                    PRDiff= (float(list2[i][5]) - float(list1[i][5]))
                    ScoreDiff =  (float(list2[i][4]) - float(list1[i][4]))
                    MoneyDiff =  (float(list2[i][3]) - float(list1[i][3]))   
                    if store > ScoreDiff/ MoneyDiff and list2[i] not in list1:
                        store = ScoreDiff/ MoneyDiff
                        idstore = i

        elif direction == 1:
            for i in range(len(list1)):
                if list2[i][3] == list1[i][3]:
                    pass
                else:
                    PRDiff= (float(list2[i][5]) - float(list1[i][5]))
                    ScoreDiff =  (float(list2[i][4]) - float(list1[i][4]))
                    MoneyDiff =  (float(list2[i][3]) - float(list1[i][3])) 
                    if store > ScoreDiff/ MoneyDiff and list2[i] not in list1:
                        store = ScoreDiff/ MoneyDiff                        
                        idstore = i
        list1[idstore] = list2[idstore]
        return list1

    def getTotalCost(self,list):
        sum = 0
        for i in list:
            sum += int(i[3])
        return sum

    def printTotalScore(self,list):
        sum = 0
        for i in list:
            sum += float(i[4])
        print(sum)

    def printList(self,list):
        for i in list:
            print(i)

# initializing----------------------------------------------------------------------
p1 = player()
used = []

list1 = []
list1.append(p1.getBestDst(playerlists, used))
list1.append(p1.getBestK(playerlists, used))
list1.append(p1.getBestQB(playerlists, used))
list1.append(p1.getBestTE(playerlists, used))
list1.append(p1.getBestRB1(playerlists, used))
list1.append(p1.getBestRB2(playerlists, used))
list1.append(p1.getBestWR1(playerlists, used))
list1.append(p1.getBestWR2(playerlists, used))
list1.append(p1.getBestFLEX(playerlists, used))

print("---------------------------------------initializing end --------------------------------------------------------")

totalcost = p1.getTotalCost(list1)
p1.printTotalScore(list1)
decision_lower_bound=49900

while totalcost > 50000 or totalcost < decision_lower_bound:
    used = []
    used = list1

    if totalcost < decision_lower_bound:
        direction = 1
        print("direction", direction)
        list2 = p1.getBestSwap(playerlists,list1,direction)
        list3 = p1.Compare(list1, list2, direction)
    elif totalcost > 50000:
        direction = -1
        print("direction", direction)
        list2 = p1.getBestSwap(playerlists, list1,direction)
        list3 = p1.Compare(list1,list2,direction)

    print("------------------------------------list 2 above----------------------------------------------")
    p1.printList(list3)
    print("------------------------------------list 3 above----------------------------------------------")
    list1 = list3
    totalcost = p1.getTotalCost(list1)

    p1.printList(list1)
    print(totalcost)
    p1.printTotalScore(list1)


    print("==============================================one iteration end and new list1 above=====================================================")

























