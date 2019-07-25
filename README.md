# Casino Simulation


The casino simulation is a culmination of a semester-long project to create a realistic simulator that can play up to 5 different games made for the casino. The players within the casino act dynamically, with different play styles and movements about the casino. The game compiles the statistics of each game and player based on the game settings chose at the start of the simulation.

## Starting the Simulator

Step 1. Click on Casino.exe found in the repository.                               
Step 2. Click on download in the top right hand corner or 'View raw'                                
Step 3. Your broswer might think the file is dangerous, click 'Keep' anyway.                         
Step 4. Save the executable to a location on your computer.                                    
Step 5. Go to the location of the executable and run it.                                  
Step 6. Windows might unrecognize the app, click 'More info' and then click 'Run anyway'    
Step 7. Click Yes and save the Casino folder to a location on your computer.                         
Step 8. Go to that location and click on the Casino folder.                               
Step 9. Double click on 'casino.exe' and follow the prompts.                                  

## Setting up the Simulation

The simulator opens with a user menu, allowing the user to choose what games run and under what conditions those games run. Each option comes with specific instructions on how to choose the settings. If a game is run, it comes with one or more variable settings, that effect each game directly. They are as follows:

 - Poker Vig: Set the percentage that the casino collects off of the final table pot. Recommended to be 0.03 to 0.1 (3% to 10 %)
 - Blackjack Stand: Sets the value that the dealer has to stand on, which is typically 17 in casinos.
 - Blackjack Total Number: Blackjacks goal is to hit to 21 without going over, but the number that you hit to can be changed. If you write 25, blackjack will be given at 25.
 - Horse Racing Odds Accuracy: The horse racing odds are always the most current, accurate odds, but the casino can select to display less accurate odds, making it harder to bet on the winning horse.
 - Go Fish Table Minimum: There are three options, type 1 for a high buy in (1000+), type 2 for an average bet (500-1000) and type 3 for a low bet (<500)
 - Go Fish Vig: Just as with poker, the final ante has a percentage taken out by the casino. This should again be set between 0.03 to 0.1.
 
## Known Bugs

When running a simulation with a large amount of rounds, sometimes go fish will get stuck in a loop. We currently do not know the cause of this bug. 

Sometimes the percentages of profit for the casino do not add up properly. We currently do not know the cause of this bug. 
