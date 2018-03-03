# 15-112, Summer 2, Term Project
######################################
# Full name: Kunal Vaishnavi
# Section: C
# Andrew ID: kvaishna
######################################

import csv

class Batter(object):
    def __init__(self, row):
        index = 0
        self.team = row[index]; index += 1
        self.name = row[index]; index += 1
        self.age = int(row[index]); index += 1
        self.pos = row[index]; index += 1
        self.games = int(row[index]); index += 1
        self.singles = int(row[index]); index += 1
        self.doubles = int(row[index]); index += 1
        self.triples = int(row[index]); index += 1
        self.HR = int(row[index]); index += 1
        self.RBI = int(row[index]); index += 1
        self.SB = int(row[index]); index += 1
        self.BBPer = float(row[index]); index += 1
        self.KPer = float(row[index]); index += 1
        self.BABIP = float(row[index]); index += 1
        self.BAA = float(row[index]); index += 1
        self.OBP = float(row[index]); index += 1
        self.SLG = float(row[index]); index += 1
        self.OPS = float(row[index]); index += 1
        self.OPSPlus = int(row[index]); index += 1
        self.WAR = float(row[index]); index += 1

    def printNicely(self):
        print(self.team, self.name, self.age, self.pos, self.games,
              self.singles, self.doubles, self.triples, self.HR, self.RBI,
              self.SB, self.BBPer, self.KPer, self.BABIP, self.BAA, self.OBP,
              self.SLG, self.OPS, self.OPSPlus, self.WAR)

allBatters = []
def readFile():
    with open('batters.csv') as batters:
        readCSV = csv.reader(batters, delimiter=',')
        for row in readCSV:
            allBatters.append(Batter(row))

def getAllBatters():
    readFile()
    return allBatters
