# 15-112, Summer 2, Term Project
######################################
# Full name: Kunal Vaishnavi
# Section: C
# Andrew ID: kvaishna
######################################

import csv

class Pitcher(object):
    def __init__(self, row):
        pos = 0
        self.team = row[pos]; pos += 1
        self.name = row[pos]; pos += 1
        self.age = int(row[pos]); pos += 1
        self.GS = int(row[pos]); pos += 1
        self.ERA = float(row[pos]); pos += 1
        self.IP = float(row[pos]); pos += 1
        self.HRPer9 = float(row[pos]); pos += 1
        self.BBPer9 = float(row[pos]); pos += 1
        self.SOPer9 = float(row[pos]); pos += 1
        self.BABIP = float(row[pos]); pos += 1
        self.ERAPlus = int(row[pos]); pos += 1
        self.FIP = float(row[pos]); pos += 1
        self.WAR = float(row[pos]); pos += 1

    def printNicely(self):
        print(self.team, self.name, self.age, self.GS, self.ERA, self.IP,
              self.HRPer9, self.BBPer9, self.SOPer9, self.BABIP, self.ERAPlus,
              self.FIP, self.WAR)
        
allPitchers = []
def readFile():
    with open('pitchers.csv') as pitchers:
        readCSV = csv.reader(pitchers, delimiter=',')
        for row in readCSV:
            allPitchers.append(Pitcher(row))

def getAllPitchers():
    readFile()
    return allPitchers
