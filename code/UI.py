# 15-112, Summer 2, Term Project
######################################
# Full name: Kunal Vaishnavi
# Section: C
# Andrew ID: kvaishna
######################################

# Below template is from: https://pd43.github.io/notes/notes4-2.html
# Also: http://www.kosbie.net/cmu/spring-17/15-112/notes/button-demo2.py

from tkinter import *
import Simulator

# Initialize the data which will be used to draw on the screen.
def init(data):
    # load data as appropriate
    data.playMenu = False
    data.helpMenu = False
    data.alreadyPrinted = False
    data.start = True
    data.gameOver = False
    data.temp = True
    data.tall_image = PhotoImage(file = "mlbteamstall.gif")
    data.long_image = PhotoImage(file = "mlbteamslong.gif")
    data.awayTeam, data.homeTeam = '', ''

def createButtons(data):
    data.buttonFrame = Frame(data.root)
    data.b1 = Button(data.buttonFrame, text="Play",
                     command=lambda:onButton(data,1))
    data.b1.grid(row=0,column=0)
    data.b2 = Button(data.buttonFrame, text="Help",
                     command=lambda:onButton(data,2))
    data.b2.grid(row=0,column=1)
    data.buttonFrame.pack(side=BOTTOM)

def createDropdownMenus(canvas, data):
    data.buttonFrame = Frame(data.root)
    data.b3 = Button(data.buttonFrame, text="Start Simulation",
                     command=lambda:onButton(data,3))
    data.b3.grid(row=0,column=2)
    data.buttonFrame.pack(side=BOTTOM)
    away, home = StringVar(data.root), StringVar(data.root)
    away.set("Away Team")
    home.set("Home Team")
    away_menu = OptionMenu(data.root, away, 'ARI', 'ATL', 'BAL', 'BOS',
                           'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
                           'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM',
                           'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SFG', 'SEA',
                           'STL', 'TBR', 'TEX', 'TOR', 'WAS',
                           command=lambda away_menu:getAwaySelection(away, data))
    home_menu = OptionMenu(data.root, home, 'ARI', 'ATL', 'BAL', 'BOS',
                           'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
                           'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM',
                           'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SFG', 'SEA',
                           'STL', 'TBR', 'TEX', 'TOR', 'WAS',
                           command=lambda home_menu:getHomeSelection(home, data))
    away_menu.pack()
    home_menu.pack()

def getAwaySelection(event, data): data.awayTeam = event
def getHomeSelection(event, data): data.homeTeam = event

# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym == 'b' and data.helpMenu:
        data.alreadyPrinted = False
        data.helpMenu = False
        data.start = True

def timerFired(data):
    pass

def playMenuPressed(data):
    data.playMenu = not data.playMenu
    data.start = False
    data.b1.destroy()
    data.b2.destroy()
    data.buttonFrame.destroy()
    
def helpButtonPressed(data):
    data.helpMenu = not data.helpMenu
    data.start = False
    data.b1.destroy()
    data.b2.destroy()
    data.buttonFrame.destroy()

def startMatchupButtonPressed(data):
    #data.b3.destroy()
    #data.buttonFrame.destroy()
    Simulator.main(data.awayTeam.get(), data.homeTeam.get())

def onButton(data, buttonId):
    if (buttonId == 1): playMenuPressed(data)
    elif (buttonId == 2): helpButtonPressed(data)
    elif (buttonId == 3): startMatchupButtonPressed(data)

# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.
def redrawAll(canvas, data):
    if not data.alreadyPrinted:
        createButtons(data)
        data.alreadyPrinted = True
    if data.start:
        image = canvas.create_image(5, 75, anchor=NW, image=data.tall_image)
        canvas.create_text(data.width/2, 45,
                            text="Welcome to the Baseball Simulator 3000!")
    if data.helpMenu:
        image = canvas.create_image(0, 0, anchor=NW, image=data.long_image)
        displayHelpText(canvas, data)
    if data.playMenu:
        if data.temp: createDropdownMenus(canvas, data)
        canvas.create_text(data.width/2, 45, text="Choose Your Teams:")
        data.temp = False
        #data.gameOver = True
    if data.gameOver: init(data)

def displayHelpText(canvas, data):
    canvas.create_text(data.width/2, (3/5)*data.height, text='Instructions:')
    canvas.create_text(data.width/2, (4/5)*data.height, text='Select \
two teams to simulate a game against.\n\nThe simulator will then display the \
results, along \nwith a scoring summary for the game.\n\nPress \'b\' to go \
back to the main menu.')

####################################
####################################
# use the run function as-is
####################################
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas
    root = Tk()
    data.root = root
#    data.root.geometry('%dx%d+%d+%d' % (data.width, data.height, 100, 100))
    init(data)
    root.title("      Baseball Simulator 3000 by Kunal Vaishnavi")
    # draw background image
#    data.bg_image = PhotoImage(file='mlbteams.gif')
#    data.bg_label = Label(data.root, image=data.bg_image)
#    data.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)
