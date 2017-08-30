# 15-112, Summer 2, Term Project
######################################
# Full name: Kunal Vaishnavi
# Section: C
# Andrew ID: kvaishna
######################################

import Algorithms, Dictionaries, random

badOutcomes = ['K', 'GO', 'FO', 'LO']
def processAtBat(outcome, bases, boxScore, outs):
    print(outcome, ': OUTCOME')
    if outcome in badOutcomes: outs += 1; print(outs, 'OUTS')
    else:
        shiftNum, hit, error = 0, 0, 0
        if outcome[0] in ['B', 'I', 'E']: shiftNum = 5
        elif outcome == '1B': shiftNum = 1; hit = 1
        elif outcome == '2B': shiftNum = 2; hit = 1
        elif outcome == '3B': shiftNum = 3; hit = 1
        elif outcome == 'HR': shiftNum = 4; hit = 1
        if outcome == 'E': error = 1
        (runs, bases) = moveRunners(bases, shiftNum)
        boxScore = editBoxScore(boxScore, runs, hit, error)
    return (bases, boxScore, outs)

def moveRunners(bases, shiftNum):
    runsToAdd = 0
    if shiftNum == 0: return (runsToAdd, bases)
    bases[-1] = 1
    if shiftNum == 4:
        numRunners = bases.count(1)
        bases = [0,0,0,1]
        return (runsToAdd+numRunners, bases)
    if shiftNum == 5:
        if bases[-2] != 0: # runner on first cases
            if bases[-3] == 0: bases[-3] = bases[-2] # second base open
            elif bases[-4] == 1: runsToAdd += 1 # bases loaded
            else: bases = bases[1:]; bases.extend([0])
        bases[-2] = 1
        return (runsToAdd, bases)
    else:
        for i in range(shiftNum):
            runsToAdd += bases[0]
            # need to add 0's and 1's appropriately
            bases = bases[1:]
            while len(bases) != 4:
                bases.extend([0])
        return (runsToAdd, bases)

def editBoxScore(boxScore, runs, hit, error):
    boxScore[0] += runs
    boxScore[1] += hit
    boxScore[2] += error
    return boxScore

def setOutcomes(batter, pitcher):
    (constant,tempOutcomes) = Algorithms.setConstantAndOutcomes(batter,pitcher)
    return (constant,tempOutcomes)

def posInLineup(pos):
    pos += 1
    if pos == 10: pos = 1
    return pos

def addResult(scoringSummary, result, batter, pitcher, RBIs, inning):
    scoringSummary.append("In inning " + str(inning) + ", " + batter.name + \
                          " got a " + result + " that scored " \
                          + str(RBIs) + " runs off of " + pitcher.name)
    return scoringSummary

Dictionaries.setAllTeams()
allKeys = Dictionaries.getAllTeamsNames()
def main(awayTeam, homeTeam):
#    isValid, awayTeam, homeTeam = False, '', ''
#    while not isValid:
#        print("Here are your options: ")
#        print(list(allKeys))
#        awayTeam = input("Type the team acronym of the away team: ")
#        homeTeam = input("Type the team acronym of the home team: ")
#        if awayTeam in allKeys and homeTeam in allKeys: isValid = True
#        else: print("Try again")
    gameRoster = [0, 0]
    gameRoster[0] = Dictionaries.getTeamRoster(awayTeam)
    gameRoster[1] = Dictionaries.getTeamRoster(homeTeam)
#    Dictionaries.printTeamRoster(gameRoster[0])
#    Dictionaries.printTeamRoster(gameRoster[1])
    posAway, posHome, topHalf, bottomHalf = 0, 0, True, False
    totalOuts, awayBoxScore, homeBoxScore = 0, [0,0,0], [0,0,0]
    bases, boxScore, outs, inning = [0,0,0,1], [], 0, 1
    scoringSummary = []
    while totalOuts != 54: # Needs to be b/c 27 (per team) * 2 teams
        # top half of inning
        prevRuns, batter, pitcher = 0, None, None
        if topHalf:
            posAway = posInLineup(posAway)
            boxScore = awayBoxScore
            prevRuns = awayBoxScore[0]
            batter = gameRoster[0][posAway]
            pitcher = gameRoster[1][0]
            (constant, tempOutcomes) = setOutcomes(batter, pitcher)
        # bottom half of inning
        if bottomHalf:
            posHome = posInLineup(posHome)
            boxScore = homeBoxScore
            prevRuns = homeBoxScore[0]
            batter = gameRoster[1][posHome]
            pitcher = gameRoster[0][0]
            (constant, tempOutcomes) = setOutcomes(batter, pitcher)
        allOutcomes = Algorithms.editOutcomes(constant, tempOutcomes)
        result = random.randint(0, len(allOutcomes)-1)
        (bases, boxScore, outs) = processAtBat(allOutcomes[result], bases,\
                                               boxScore, outs)
        if prevRuns < boxScore[0]:
            RBIs = boxScore[0] - prevRuns
            scoringSummary = addResult(scoringSummary, allOutcomes[result],
                                       batter, pitcher, RBIs, inning)
        if topHalf: awayBoxScore = boxScore
        if bottomHalf: homeBoxScore = boxScore
        # Switch inning if 3 outs made
        if outs == 3:
            totalOuts += outs
            half = ''
            if topHalf: half = "Top of "
            if bottomHalf: half = "Bottom of "
            print(half + "Inning " + str(inning) + " Over!")
            if bottomHalf: inning += 1
            topHalf, bottomHalf = bottomHalf, topHalf
            outs = 0
            bases, boxScore = [0, 0, 0, 1], []
    print("Game Over!")
    print("Away: ", awayBoxScore, "\nHome: ", homeBoxScore)
    winner = awayTeam if awayBoxScore[0] > homeBoxScore[0] else homeTeam
    print(winner + " won!")
    print("Scoring Summary:")
    for elm in scoringSummary: print(elm)
    
if __name__ == "__main__":
     main()
