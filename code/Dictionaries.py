# 15-112, Summer 2, Term Project
######################################
# Full name: Kunal Vaishnavi
# Section: C
# Andrew ID: kvaishna
######################################

import Batters, Pitchers

allTeams = dict()
def createAllTeamsDict():
    allBatters = Batters.getAllBatters() # Bunch of Batter objects
    allPitchers = Pitchers.getAllPitchers() # Bunch of Pitcher objects
    for p in allPitchers:
        tempTeam = []
        tempTeam.append(p) # Adds pitcher of that team
        for b in allBatters:
            if b.team == p.team: tempTeam.append(b) # Adds batters of that team
        allTeams[p.team] = tempTeam

def printAllTeamsRoster():
    teamAcronyms = allTeams.keys()
    for team in teamAcronyms:
        teamRoster = allTeams[team]
        for player in teamRoster:
            player.printNicely()

def printTeamRoster(teamRoster):
    for player in teamRoster:
        player.printNicely()

def setAllTeams(): createAllTeamsDict()
def getAllTeams(): return allTeams
def getAllTeamsNames(): return allTeams.keys()
def getTeamRoster(team): return allTeams[team]
