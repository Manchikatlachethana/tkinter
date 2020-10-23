#Type the color just by seeing its name but not the same word!
import tkinter,random

#list of colors
colors=['Red','Yellow','Green','Blue','pink','Orange','voilet','Balck','Grey','Purple','Brown','White']

#players score initial,0
score=0

#game timeleft, initially 3 seconds. 
timeleft=30

#function that starts the game!

def startGame(event):

	#if there's still timeleft...
	if timeleft==30:
		countdown()  #start the countdown timer.
	nextcolor()			#run next color.


#function to choose nextcolor.

def nextcolor():
	global score,timeleft		#use of globally declared score and play variables above.

#if the game is currently in play
	if timeleft>0:
		e.focus_set()	#make the text entry box active.

		if e.get().lower()==colors[1].lower():
			score+=1	#..add one to the score.
		#clear the entry box.
		e.delete(0,tkinter.END)
		#shuffle the colors.
		random.shuffle(colors)
		label.config(fg=str(colors[1]),text=str(colors[0]))
		#update score
		scoreLabel.config(text="score:"+str(score))

#countdowm timer function.

def coundown():
	#use the globally declared play variable.
	global timeleft
#if game is in play
	if timeleft>0:
		timeleft-=1		#decrement timer.
#update time left label.
		timeLabel.config(text="timeleft: "+str(timeleft))









