from sys import exit

hungry = True
bored = True

def start():
	print "You wake up on 14th St., hungry and bored."
	print "Do you stay on 14th St. or leave?"
	
	while True:
		choice = raw_input("> ")
	
		if choice == "stay":
			fourteenth()
		elif choice == "leave":
			transit_fourteenth()
		else:
			print "I didn't get that."
	
def fourteenth():
	print "You're looking for dinner on 14th Street. Careful: here be monsters."
	print "Where would you like to eat?"
	
	while True:
		choice = raw_input("> ")
		if choice == "Le Diplomate":
			print "There is a two hour wait for a table."
			choice = raw_input("> ")
			
			if "bribe" in choice:
				dinner()
				transit_fourteenth()
			else:
				print "You die of starvation waiting for a table."
				raw_input("> ")
				start()
		
		elif choice == "Garden District":
			print "A freezing rain begins to fall."
			choice = raw_input("> ")
			if "umbrella" or "jacket" in choice:
				dinner()
				transit_fourteenth()
			else:
				print "You have frozen to death in an outdoor beer garder."
				raw_input("> ")
				start()
		else:
			print "There are no tables available for three weeks. You starve to death."
			raw_input("> ")
			start()
		
def transit_fourteenth():
	print "You can leave via the G2 West/East, 90 West/East, Uber, or Bikeshare."
	print "What do you take?"
	
	while True:
		choice = raw_input("> ")
		if choice == "G2 West":
			print "You arrive in Georgetown and die of despair."
			raw_input("> ")
			start()
		elif choice == "G2 East":
			bloomingdale()	
		elif choice == "90 West":
			print "You arrive in Adams Morgan. You have died of jumbo slice."
			raw_input("> ")
			start()
		elif choice == "90 East":
			h_st()
		elif choice == "Uber":
			print "A mob of taxi drivers storms your Uber. You perish in the flames."
			raw_input("> ")
			start()
		elif choice == "Bikeshare":
			print "You are hunted for sport by an SUV with Maryland tags."
			print "Better luck next time."
			raw_input("> ")
			start()
		else:
			print "That can't help you here."

def bloomingdale():
	print "You have arrived in Bloomingdale! where would you like to go?"
	
	while True:
		choice = raw_input("> ")
	
		if choice == "Red Hen":
			print "'May I help you?', asks the host"
			choice = raw_input("> ")
			if "reservation" in choice:
				dinner()
			else:
				print "Maybe Big Bear can help you."
				raw_input("> ")
				bloomingdale()
		elif choice == "Big Bear":
			print "Welcome to Big Bear! Would you like to try our Farmer's Market buffet?"
			choice = raw_input("> ")
			if choice == "yes":
				print "You die of food poisoning."
				raw_input()
				start()
			else:
				print "Would you like some coffee?"
				energy()
				print "You walk outside, in search of the next thing."
				raw_input()
				bloomingdale_transit()
		else:
			print "I didn't get that."

def bloomingdale_transit():
	print "You can leave via the 90 West/East, the G2, Uber, or Bikeshare."
	bus = false
	
	while True:
		choice = raw_input("> ")
		if choice == "90 East":
			h_st()
		elif choice == "90 West" and not bus:
			print "I wouldn't reccomend going back there"
			bus = True
		elif choice == "90 West" and bus:
			print "I warned you."
			raw_input()
			start()
		elif choice == "Uber":
			print "Elitist."
		elif choice == "Bikeshare":
			print "Hipster."
		elif choice == "G2":
			print "You just came from there!"
		else:
			print "That can't help you here."
			raw_input()

def h_st():
	print "Welcome to H Street! Watch out for the streetcar."
	
	if bored:
		print "Be careful! You're getting bored!"
		raw_input("> ")
		
	print "Where would you like to go?"
	heart_attack = False
	indigestion = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "Sidamo" and not bored and not heart_attack:
			print "Your energy level is too high! Careful!"
			heart_attack = True
		elif choice == "Sidamo" and heart_attack:
			print "Too much caffeine! You have a heart attack and die."
			raw_input()
			start()
		elif choice == "Sidamo" and bored:
			print "Would you like some coffee?"
			energy()
			print "You walk outside, in search of the next thing."
			h_st_transit()
		elif "Toki" in choice and hungry:
			dinner()
			h_st_transit()
		elif "Toki" in choice and not hungry and not indigestion:
			print "You already ate! Careful!"
			indigestion = True
		elif "Toki" in choice and indigestion:
			print "You ate too much!"
			raw_input()
			start()
		else:
			print "That can't help you here"
	
def h_st_transit():
	print "You can leave via the Streetcar or the X2"
	streetcar = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "Streetcar" and not streetcar:
			print "Still testing! Careful!"
			streetcar = True
		elif choice == "Streetcar" and streetcar:
			print "A runanway Streetcar ran you over."
			raw_input()
			start()
		elif choice == "X2":
			ft_reno()

def ft_reno():
	print "You take the Red Line north to Tenleytown. Ft Reno is in sight!"
	print "Do you go to Whole Foods before the show?"
	
	while True:
		choice = raw_input("> ")
	
		if choice == "yes" and hungry:
			print "You're fueled up for the show!"
			ice_cream()
		elif choice == "yes" and not hungry:
			print "You already ate!"
			ice_cream()
		elif choice == "no" and hungry:
			print "That wasn't a good idea."
			raw_input()
			start()
		elif choice == "no" and not hungry:
			ice_cream()
		else:
			print "I didn't understand that."

def ice_cream():
	print "You've arrived at Ft. Reno! There's only one thing left to do."
	motherfucker = 1
	
	while True:
		choice = raw_input("> ")
		
		if "ice cream" in choice:
			print "You're an Ice Cream Eating Motherfucker. Congratulations."
			exit(0)
		elif motherfucker < 3:
			print "Aren't you forgetting something?"
			motherfucker += 1
		else:
			print "So close. Let's try again."
			raw_input()
			start()
		
					
def energy():
	choice = raw_input("> ")
	
	if choice == "yes":
		print "You feel your energy rising. Careful, though! This won't last long."
		global bored
		bored = False
	else:
		print "Careful about your energy level. You don't want to get too bored!"
	
	raw_input("> ")
	
def dinner():
	print "You have successfully found dinner! You are no longer hungry."
	global hungry
	hungry = False
	
	if bored:
		print "You are still bored. Find entertainment soon or you will be bored to death."
	
	raw_input("> ")
	
start()