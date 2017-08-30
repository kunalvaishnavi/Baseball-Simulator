# 15-112, Summer 2, Term Project
######################################
# Full name: Kunal Vaishnavi
# Section: C
# Andrew ID: kvaishna
######################################

import Dictionaries, random, math

# Probability constants
allOptions = ['BB','IBB', 'HBP', '1B', '2B', '3B', 'HR', 'E',
              'K', 'GO', 'FO', 'LO']
probabilityConstants = [5, 1, 1, 15, 10, 1, 1, 1, 30, 20, 10, 5]
def setAllOutcomes():
    temp = []
    for i in range(len(allOptions)):
        temp.append([allOptions[i]]*probabilityConstants[i])
    temp = flatten(temp)
    random.shuffle(temp)
    return temp

def applyPitcherEffect(pitcher, constant):
    constant = Age_Effect(pitcher, constant)
    constant = GS_Started_Effect(pitcher, constant)
    constant = IPEffect(pitcher, constant)
    constant = ERA_Effect(pitcher, constant)
    constant = HRPer9_Effect(pitcher, constant)
    constant = SOPer9_Effect(pitcher, constant)
    constant = BBPer9_Effect(pitcher, constant)
    constant = BABIP_Effect(pitcher, constant)
    constant = ERAPlus_Effect(pitcher, constant)
    constant = FIP_Effect(pitcher, constant)
    constant = WAR_Effect(pitcher, constant)
    return constant

def Age_Effect(pitcher, constant):
    if int(pitcher.age) <= 27: constant += 4
    elif 28 <= int(pitcher.age) <= 31: constant += 6
    elif 32 <= int(pitcher.age) <= 35: constant += 3
    elif int(pitcher.age) >= 36: constant -= 2
    return constant
    
def GS_Started_Effect(pitcher, constant):
    if int(pitcher.GS) >= 20: constant += 2
    elif int(pitcher.GS) < 20: constant -= 2
    return constant

def IPEffect(pitcher, constant):
    if float(pitcher.IP) >= 140: constant += 5
    elif float(pitcher.IP) < 140: constant += 2
    return constant

def ERA_Effect(pitcher, constant):
    if float(pitcher.ERA) < 1: constant += 15
    elif 1 <= float(pitcher.ERA) < 2: constant += 10
    elif 2 <= float(pitcher.ERA) < 2.5: constant += 8
    elif 2.5 <= float(pitcher.ERA) < 3: constant += 6
    elif 3 <= float(pitcher.ERA) < 3.5: constant += 4
    elif 3.5 <= float(pitcher.ERA) < 4: constant += 2
    elif float(pitcher.ERA) >= 4: constant -= 4
    return constant

def HRPer9_Effect(pitcher, constant):
    if float(pitcher.HRPer9) >= 1: constant -= 3
    elif float(pitcher.HRPer9) < 1: constant += 2
    return constant
    
def SOPer9_Effect(pitcher, constant):
    if float(pitcher.SOPer9) < 6: constant -= 6
    elif 6 <= float(pitcher.SOPer9) < 7: constant -= 4
    elif 7 <= float(pitcher.SOPer9) < 8: constant -= 2
    elif 8 <= float(pitcher.SOPer9) < 9: constant += 2
    elif 9 <= float(pitcher.SOPer9) < 10: constant += 4
    elif float(pitcher.SOPer9) >= 10: constant += 6
    return constant
    
def BBPer9_Effect(pitcher, constant):
    if float(pitcher.BBPer9) >= 3: constant -= 3
    elif float(pitcher.BBPer9) < 3: constant += 2
    return constant
    
def BABIP_Effect(pitcher, constant):
    if float(pitcher.BABIP) < 2.75: constant -= 1
    elif 2.75 <= float(pitcher.BABIP) <= 3.15: constant += 5
    elif float(pitcher.BABIP) > 3.15: constant -= 3
    return constant
    
def ERAPlus_Effect(pitcher, constant):
    if int(pitcher.ERAPlus) < 100: constant -= 5
    elif 100 <= int(pitcher.ERAPlus) < 125: constant += 5
    elif 125 <= int(pitcher.ERAPlus) < 150: constant += 6
    elif 150 <= int(pitcher.ERAPlus): constant += 7
    return constant
    
def FIP_Effect(pitcher, constant):
    if float(pitcher.FIP) < 1: constant += 15
    elif 1 <= float(pitcher.FIP) < 2: constant += 10
    elif 2 <= float(pitcher.FIP) < 2.5: constant += 8
    elif 2.5 <= float(pitcher.FIP) < 3: constant += 6
    elif 3 <= float(pitcher.FIP) < 3.5: constant += 4
    elif 3.5 <= float(pitcher.FIP) < 4: constant += 2
    elif float(pitcher.FIP) >= 4: constant -= 4
    return constant
    
def WAR_Effect(pitcher, constant):
    if 0 <= float(pitcher.WAR) < 1.5: constant += 0
    elif 1.5 <= float(pitcher.WAR) < 2.5: constant += 1
    elif 2.5 <= float(pitcher.WAR) < 3.5: constant += 2
    elif 3.5 <= float(pitcher.WAR) < 4.5: constant += 3
    elif float(pitcher.WAR) >= 4.5: constant += 5
    return constant

#allTeams = Dictionaries.setAllTeams()
def setConstantAndOutcomes(batter, pitcher):
    allOutcomes = setAllOutcomes()
    bConstant = applyBatterEffect(batter, allOutcomes, 0)
    pConstant = applyPitcherEffect(pitcher, 0)
    constant = pConstant % bConstant # Randomizes the # of outcomes to be edited
    constant = math.ceil(constant) # Makes constant an int
    return (constant, allOutcomes)

def find(L, elm):
    if elm in L: return L.index(elm)
    else: return -1

def editOutcomes(constant, allOutcomes):
    for i in range(constant):
        # add a random K b/c of increase in K's in 2017 season
        goodOutcomes = ['1B', '2B', '3B', 'HR', 'BB', 'IBB', 'E']
        pos = find(allOutcomes, goodOutcomes[\
                                    random.randint(0, len(goodOutcomes)-1)])
        allOutcomes[pos] = 'K'
    return allOutcomes

# Try to calculate value closest to batter's WAR (but at least greater than) so
# that when run through the pitcher effects, the constant is shifted around
def applyBatterEffect(batter, allOutcomes, num):
    if num == 100: return 4
    factor = float(batter.BAA) - float(batter.BABIP)
    onBaseAbility = float(batter.OBP) * (float(batter.BBPer)/100)
    sluggingAbility = (int(batter.doubles) + int(batter.triples) + \
                       int(batter.HR)) * float(batter.SLG)
    hittingAbility = (int(batter.singles)-float(batter.KPer)/100) -\
                     (int(batter.games)*int(batter.SB)*float(batter.OBP)) +\
                     (float(batter.OPS)*int(batter.RBI))
    # Make value in [0, 4]
    value = abs(factor * (onBaseAbility + sluggingAbility - hittingAbility))
    temp = str(value)
    value = value % 10**(len(temp)-1)
    # The most likely max WAR a player can attain in the remainder of the season
    if value > 4:
        # change BABIP value
        if factor < 0: batter.BABIP -= .05
        else: batter.BABIP += .05
        # add a random K b/c of increase in K's in 2017 season
        goodOutcomes = ['1B', '2B', '3B', 'HR', 'BB', 'IBB', 'E']
        pos = find(allOutcomes, random.randint(0, len(goodOutcomes)-1))
        allOutcomes[pos] = 'K'
        return applyBatterEffect(batter, allOutcomes, num+1) # repeat process
    else: return value

# Makes L into a 1D list. From hw5-1b.py.
def flatten(L):
    if not isinstance(L, list): return L # flatten(3)
    elif len(L) == 0: return [] # flatten([])
    elif not isinstance(L[0], list): return [L[0]] + flatten(L[1:])
    else: return flatten(L[0]) + flatten(L[1:])
