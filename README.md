# Baseball Simulator Project by Kunal Vaishnavi
# Carnegie Mellon's 15-112 Course
# See this YouTube link to learn more about my project: https://youtu.be/bbwQ6icfWzo

What is this project?:

A baseball simulator game that pits any two teams against one another and simulates what a real life game would be between them, based off of players’ current statistics in a CSV file.

How to play?:

Open the UI.py file in your IDE (the app you use to write your Python code). Run the file and you will see a popup (it may be hidden behind your windows at first), which is the simulator. Press the ‘help’ button if you’re confused/need help and press ‘b’ to go back to the main menu. Press ‘play’ to start the simulation. 

Once you press ‘play,’ select your away and home teams and press the ‘start simulation’ button. Then, your IDE’s shell will start printing the results. You may see the ‘spinning wheel’ on your cursor. Do not be alarmed! The simulation is merely running; your computer has not crashed. At the end of the simulation, the shell will display the results of the matchup, including the box score of both teams, who won, and a scoring summary. Then, you can continue to run simulations against any two teams by repeating the selection process. 

Hit the red ‘x’ at the top left of the simulator to quit the program.

A Few Notes...:

Note 1: I am using recent data. In fact, the stats in my Excel sheet are as of Sun, Aug 6, 2017 and of the 2017 baseball season.

Note 2: This is a very accurate simulator. I have spent many hours to perfect my algorithms and the results are on par with what one would expect. For example, if I choose a matchup of NYY vs. BOS, I should expect NYY to not score many runs because of how great BOS’s pitcher (Chris Sale) has been in the 2017 season. However, since this is baseball, anything out of the ordinary can occur so my algorithms take that into account. Thus, sometimes the simulator will show out-of-the-blue results and that is done on purpose.

Note 3: Every batter-pitcher matchup has its own personalized list of outcomes, based on how the batter and the pitcher are doing in the 2017 season.

Note 4: Since this project was done in a six day span, many possible baseball scenarios were ignored. See the file called "Probability of Outcomes.txt" for more information.

Note 5: In the timesheet that I've uploaded, it says that I created a file called readme.txt. This is the same readme, just copied and pasted in this file.
