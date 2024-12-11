# Taha Ahmad 101065676


import random


def instructions():
	print("In order to interact and progress further in the game, there are different commands which are at your disposal. Use the NORTH, SOUTH, EAST and WEST commands to travel between the different regions in the map. The LOOK command gives a description of the surrounding area as well as the non-playable characters (NPC’s) and items which appear in that region. You can interact with NPC’s by using the command TALK and then the name of the NPC if there are multiple when prompted. To interact with items, use the PICKUP command. To view the items you have picked up, use the BAG command. To view score, use the command SCORE. The HELP command can be used whenever to display instructions.")
	
	
def init_game_data():
	game_data = {"open": True,
				"items": ["RATIONS", "χ-Blade"],
				"equipped_item": "NONE",
				"player_location": "SPACESHIP",
				"MAX_HP": 100,
				"HP": 100,
				"ATK": 10,
				"EVA": 4,
				"score": 10,
				"area_check": False,
				"chosen": False,
				"boat": False,
				"egg": False,
				"egg_pickup": False,
				}
				
	game_data["locations"] = {"SPACESHIP": {"NORTH": "WASTELAND", "EAST": "SPACESHIP", "SOUTH": "SPACESHIP", "WEST": "SPACESHIP", "visits": 0},
							"WASTELAND": {"NORTH": "MOUNTAIN_F1", "EAST": "LAVA_STREAM", "SOUTH": "SPACESHIP", "WEST": "RIVER", "visits": 0},
							"MOUNTAIN_F1": {"NORTH": "MOUNTAIN_F2", "EAST": "MOUNTAIN_F1", "SOUTH": "WASTELAND", "WEST": "MOUNTAIN_F1", "visits": 0},
							"MOUNTAIN_F2": {"NORTH": "MOUNTAIN_F3", "EAST": "MOUNTAIN_F2", "SOUTH": "MOUNTAIN_F1", "WEST": "MOUNTAIN_F2", "visits": 0},
							"MOUNTAIN_F3": {"NORTH": "SUMMIT", "EAST": "MOUNTAIN_F3", "SOUTH": "MOUNTAIN_F2", "WEST": "MOUNTAIN_F3", "visits": 0},
							"SUMMIT": {"NORTH": "SUMMIT", "EAST": "SUMMIT", "SOUTH": "MOUNTAIN_F3", "WEST": "SUMMIT", "visits": 0},
							"LAVA_STREAM": {"NORTH": "LAVA_STREAM", "EAST": "VILLAGE_ENTRANCE", "SOUTH": "VOLCANO", "WEST": "WASTELAND", "visits": 0, "cross": False},
							"VOLCANO": {"NORTH": "LAVA_STREAM", "EAST": "VOLCANO", "SOUTH": "VOLCANO", "WEST": "VOLCANO", "visits": 0},
							"VILLAGE_ENTRANCE": {"NORTH": "VILLAGE", "EAST": "VILLAGE_ENTRANCE", "SOUTH": "VILLAGE_ENTRANCE", "WEST": "LAVA_STREAM", "visits": 0},
							"VILLAGE": {"NORTH": "SHRINE", "EAST": "VILLAGE", "SOUTH": "VILLAGE_ENTRANCE", "WEST": "VILLAGE", "visits": 0},
							"SHRINE": {"NORTH": "SHRINE", "EAST": "SHRINE", "SOUTH": "VILLAGE", "WEST": "SHRINE", "visits": 0},
							"RIVER": {"NORTH": "WOODS", "EAST": "WASTELAND", "SOUTH": "JUNGLE", "WEST": "RIVER", "visits": 0},
							"WOODS": {"NORTH": "WOODS", "EAST": "WOODS", "SOUTH": "RIVER", "WEST": "WOODS", "visits": 0},
							"JUNGLE": {"NORTH": "RIVER", "EAST": "TEMPLE_ENTRANCE", "SOUTH": "JUNGLE", "WEST": "JUNGLE", "visits": 0},
							"TEMPLE_ENTRANCE": {"NORTH": "TEMPLE_ENTRANCE", "EAST": "TEMPLE_ENTRANCE", "SOUTH": "TEMPLE", "WEST": "JUNGLE", "visits": 0},
							"TEMPLE": {"NORTH": "TEMPLE_ENTRANCE", "EAST": "TEMPLE", "SOUTH": "TEMPLE", "WEST": "TEMPLE", "visits": 0},
							}
							
	game_data["enemies"] = {"FLYING_LEMUR": {"HP": 15, "ATK": 4},
							"TURTLE_BISON": {"HP": 30, "ATK": 2},
							"MONKEY_SNAKE": {"HP": 20, "ATK": 3},
							"DRAGON": {"HP": 55, "ATK": 12},
							}

	return game_data

	
def handle_input(game_data, input_string):
	if "NORTH" in input_string:
		return "NORTH"
	elif "SOUTH" in input_string:
		return "SOUTH"
	elif "EAST" in input_string:
		return "EAST"
	elif "WEST" in input_string:
		return "WEST"
	elif "HELP" in input_string:
		return "HELP"
	elif "LOOK" in input_string:
		return "LOOK"
	elif "SCORE" in input_string:
		return "SCORE"
	elif "TALK" in input_string:
		return "TALK"
	elif "BAG" in input_string:
		return "BAG"
	elif "PICKUP" in input_string:
		return "PICKUP"
	
	elif "QUIT" in input_string:
		return "QUIT"
	else:
		print(random.choice(["Invalid input.", "Try again.", "I can't understand what you're saying."]))
		return "invalid_input"


def update_location(game_data, move):
	
	if game_data["locations"][game_data["player_location"]][move] == "WOODS" or game_data["locations"][game_data["player_location"]][move] == "JUNGLE":
		if "BOAT" in game_data["items"]:
			game_data["player_location"] = game_data["locations"][game_data["player_location"]][move]
			game_data["locations"][game_data["player_location"]]["visits"] += 1
			location_description(game_data["player_location"])
		else:
			print("You need a boat and paddles to continue.")
	
	elif game_data["locations"][game_data["player_location"]][move] == "VILLAGE_ENTRANCE":		
		if game_data["chosen"] == True:
			game_data["player_location"] = game_data["locations"][game_data["player_location"]][move]
			game_data["locations"][game_data["player_location"]]["visits"] += 1
			location_description(game_data["player_location"])
		else:
			print("It's impossible to cross right now.")
	
	elif game_data["locations"][game_data["player_location"]][move] == "MOUNTAIN_F2":
		if "WEATHER SUIT" in game_data["items"]:
			game_data["player_location"] = game_data["locations"][game_data["player_location"]][move]
			game_data["locations"][game_data["player_location"]]["visits"] += 1
			location_description(game_data["player_location"])
		else:
			print("You'll need to find something that will help protect you from the weather conditions before you climb the mountain.")
	
	else:
		game_data["player_location"] = game_data["locations"][game_data["player_location"]][move]
		game_data["locations"][game_data["player_location"]]["visits"] += 1
		location_description(game_data["player_location"])
	
	if game_data["player_location"] == "SPACESHIP":
		game_data["HP"] = game_data["MAX_HP"]
		
	elif game_data["player_location"] == "MOUNTAIN_F2":
		if game_data["chosen"] == False:
			number = random.randint(1, 10)
			if number < 6:
				enemy_name = random.choice(["FLYING_LEMUR", "TURTLE_BISON", "MONKEY_SNAKE"])
				attack_phase(game_data, enemy_name)
	elif game_data["player_location"] == "MOUNTAIN_F3":
		if game_data["chosen"] == False:
			enemy_name = random.choice(["FLYING_LEMUR", "TURTLE_BISON", "MONKEY_SNAKE"])
			attack_phase(game_data, enemy_name)
			
	elif game_data["player_location"] == "VOLCANO":
		if game_data["items"][1] == "χ-Blade":
			game_data["items"][1] = "Molten χ-Blade"
			game_data["ATK"] += 5
		
	return game_data
	
	
def location_description(location):
	
	if location == "SPACESHIP":
		print("You are in your ship. There is a lot of complex equipment and instruments. Your crew members seem to have left the ship to explore already. The exit of the ship is open.")
		
	elif location == "WASTELAND":
		print("You are just outside your ship in a barren wasteland. Altough there doesn't seem to be any life in this area, it seems to be connected to various other locations which look more promising. Some of your crew memebers are around.")
		
	elif location == "MOUNTAIN_F1":
		print("You are at the foot of the mountain. It towers over you with superiority. You can barely see the peak, however, from the bottom you can see living creatures move around.")
		
	elif location == "MOUNTAIN_F2":
		print("You are midway through climbing the mountain. The creatures seem to appear more often and become hostile the closer you get to the peak. The winds start to blow faster.")
		
	elif location == "MOUNTAIN_F3":
		print("You are nearly at the top of the mountain. The winds have grown extremely violent almost throwing you off the moutain. The creatures have begun to attack more often, but they have yet to show any signs of willingness to return to Earth along with you.")
		
	elif location == "SUMMIT":
		print("You are at the summit of the mountain. The peak is so high that it resides above the clouds. The violent winds are left below you and in front of you there is what seems to be a dragon of colour white as snow.")
		
	elif location == "LAVA_STREAM":
		print("You are in front of a long stream of lava. The source of the lava seems to be coming from a volcano towards the south. Across the stream of lava there is something that appears to be a village.")
		
	elif location == "VOLCANO":
		print("You are the top of a volcano. The heat makes you feel as though you are melting. From atop the volcano, the village across the stream of lava becomes more clear and there is what appears to be living creatures.")
		
	elif location == "VILLAGE_ENTRANCE":
		print("You are the entrance to a fortified village. There is a gate to enter the village, but it appears to be guarded by a gatekeeper.")
		
	elif location == "VILLAGE":
		print("You are inside a village with many living creatures. They all seem to be hybrid beings composed of different animals from Earth.")
		
	elif location == "SHRINE":
		print("You are at the shrine of the ruler of this world, Indra. Many creatures seem to be worshiping a statue which resembles the dragon you fought at the summit of the moutain.")
		
	elif location == "RIVER":
		print("In front of you is a large waterfall which connects to a long river flowing in two directions. The ecosystem is flourishing in this area.")
		
	elif location == "WOODS":
		print("You are in the woods where many different fruits seem to be growing.")
		
	elif location == "JUNGLE":
		print("You are in a vast jungle with many insects flying around. All around there seems to be large pillars covered in vines and moss.")
		
	elif location == "TEMPLE_ENTRANCE":
		print("You are in the middle of the jungle. In front of you is the entrance to what seems to be an ancient temple.")
		
	elif location == "TEMPLE":
		print("You are in a massive ancient temple. Vines are moss are growing out from in between the stones. The temple probably dates back thousands of years.")
	
	
def attack_phase(game_data, enemy):

	enemy_hp = game_data["enemies"][enemy]["HP"]
	enemy_atk = game_data["enemies"][enemy]["ATK"]
	print("An enemy suddenly attacks!")
	
	while enemy_hp > 0 and game_data["HP"] > 0:
		print("Player Health: ", end = "")
		print(game_data["HP"], end = "")
		print("\tEnemy Health: ", end = "")
		print(enemy_hp)
		print("ACTIONS:\nATTACK\nFLEE\n")
		next_move = input("What would you like to do next? ").strip().upper()
		
		if next_move == "ATTACK":
			enemy_hp = enemy_hp - game_data["ATK"]
			game_data["HP"] = game_data["HP"] - enemy_atk
		elif next_move == "FLEE":
			number = random.randint(1, 10)
			if number < 9:
				print("Escaped!")
				break
			else:
				print("Could not escape!")
		else:
			print(random.choice(["Invalid input.", "Try again.", "I can't understand what you're saying."]))

	if enemy_hp <= 0:
		print("Enemy defeated!")
		game_data["score"] += 10
	if game_data["HP"] <= 0:
		print("Your HP ran out. A distress signal was sent to your friends. They rush you back to the spaceship.")
		game_data["player_location"] = "SPACESHIP"
		game_data["HP"] = 100
		
	return game_data
	

def NPC(location):
	
	if location == "WASTELAND":
		print("Your crew members Zeta and Omicron are around. You should go talk to them to see if they have helpful information.")
		
	if location == "RIVER":
		print("Your crew member Omicron is around.")
		
	if location == "TEMPLE" or location == "TEMPLE_ENTRANCE":
		print("Your crew memeber Gamma is around.")
		
	if location == "MOUNTAIN_F1":
		print("YOur crew memeber Zeta is around.")
		
	if location == "LAVA_STREAM":
		print("Your crew memeber Zeta is around.")
		
	if location == "SUMMIT":
		print("A massive dragon towers over you with it's cold gaze.")
		
	if location == "SHRINE":
		print("The ruler of the village seems to be in front the shrine of Indra.")


def update_score(game_data):
	
	if game_data["locations"]["MOUNTAIN_F1"]["visits"] > 0 and game_data["locations"]["RIVER"]["visits"] > 0 and game_data["locations"]["LAVA_STREAM"]["visits"] > 0:
		if game_data["area_check"] == False:
			game_data["score"] += 10
			game_data["area_check"] = True
				
	if game_data["locations"]["WOODS"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["WOODS"]["visits"] += 1
		
	if game_data["locations"]["TEMPLE_ENTRANCE"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["TEMPLE_ENTRANCE"]["visits"] += 1
		
	if game_data["locations"]["TEMPLE"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["TEMPLE"]["visits"] += 1
		
	if game_data["locations"]["SUMMIT"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["SUMMIT"]["visits"] += 1
		
	if game_data["locations"]["VOLCANO"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["VOLCANO"]["visits"] += 1
		
	if game_data["locations"]["VILLAGE_ENTRANCE"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["VILLAGE_ENTRANCE"]["visits"] += 1
		
	if game_data["locations"]["VILLAGE"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["VILLAGE"]["visits"] += 1
		
	if game_data["locations"]["SHRINE"]["visits"] == 1:
		game_data["score"] += 10
		game_data["locations"]["SHRINE"]["visits"] += 1
		
	if game_data["chosen"] == True:
		game_data["score"] += 10
		game_data["chosen"] == False
	
	return game_data
	

def interaction(location, game_data):
	
	if location == "WASTELAND":
		print("Speak to:\nZETA\nOMICRON")
		while True:
			npc_choice = input("").strip().upper()
			if npc_choice == "ZETA":
				print("ZETA: Most of the crew members have gone to do research. I will be doing some research up north and east.")
				break
			elif npc_choice == "OMICRON":
				print("OMICRON: Gamma went far west to do his search. I'll be in the west area, but i'll be staying close to the ship to monitor it for any danger.")
				break
			else:
				continue
				
	if location == "RIVER":
		if game_data["boat"] == False:
			print("OMICRON: Gamma went south to continue his search. Here, you can use this boat and these paddles to travel up and down the river. Sorry it had to manual. We needed to save all the fuel for the journey here and back.")
			game_data["boat"] = True
			game_data["items"].append("BOAT")
			game_data["items"].append("PADDLES")
		else:
			print("OMICRON: It seems Gamma has went south. You can meet up with him there using the boat and paddles I gave you.")
	
	if location == "TEMPLE_ENTRANCE":
		print("GAMMA: Hey, glad you could make it here. From my what I've collected in my research from the jungle and this area, this temple seems to date back thousands of years ago. It's incredible that it hasn't gone crumbling down yet.")
	
	if location == "TEMPLE":
		print("GAMMA: This temple is massive on the inside. That egg over there looks awfully valuable. To think it would still be intact and living after all these years. I wonder what creatures is inside.")
	
	if location == "MOUNTAIN_F1":
		if "WEATHER SUIT" in game_data["items"]:
			print("ZETA: Good luck on the climb!")
		else:
			game_data["items"].append("WEATHER SUIT")
			print("ZETA: This moutain is incredibly tall. The peak seems to be above the clouds. I wonder what secrets could lie up there. Maybe you should go check it out.")
	
	if location == "LAVA_STREAM":
		print("ZETA: This lava stream seems to be coming from that volcano down south. Something seems to be across. It looks kind of like a village, but it's pretty hard to tell from here.")
	
	if location == "SUMMIT":
		if game_data["equipped_item"] == "EGG":
			print("DRAGON: That egg you hold in your hand. Where did you find it? It bear's my child. I have been waiting over 1000 years for it to return to me. I will implore you to give it back.")
			attack_phase(game_data, "DRAGON")
			if game_data["HP"] > 0:
				print("DRAGON: You have defeated me and yet you still choose to return what's mine. I am truly grateful. I have been watching over you for some time now. What you seek is across the lava stream. For your kind deed, I shall allow you to cross and find what it is you're searching for by freezing it and creating a path for you. Also, the creatures who attacked you on the moutain shall cease their violence and comply to your wishes.")
				game_data["locations"]["LAVA_STREAM"]["cross"] = True
				game_data["chosen"] = True
		else:
			print("DRAGON: ...")
			
	if location == "SHRINE":
		print("KING ASHURA: Greetings traveller. So you're here to bring along some of our people with you to your planet. It would be our honor. Many of our villagers have been looking for oppurtunites to experience new things.")
		game_data["open"] = False
	
	return game_data


def items(game_data, location, pickup):
	
	if location == "WOODS":
		print("There are many fruits which seem to be able to boost you max health.")
		if pickup == True:
			game_data["items"].append("GOLDEN APPLE")
			game_data["items"].append("GOLDEN ORANGE")
			game_data["items"].append("GOLDEN MANGO")
			
	if location == "TEMPLE":
		if game_data["egg_pickup"] == False:
			print("The seems to be a big egg lying on a pedastale.")
			if pickup == True:
				game_data["items"].append("EGG")
				game_data["egg_pickup"] = True
				
	if location == "VILLAGE":
		print("There many items in the village such as vehicles, vegetable farms, fruits like the ones from the woods and technological equipment which show that this species is quite intelligent and capable of growing and adapting.")
			
	return game_data


def bag(game_data):
	
	for i in range(len(game_data["items"])):
		print(game_data["items"][i])
		
	while True:
		item_choice = input("Which item would you like to equip? (Type EXIT to leave bag.) ").strip().upper()
		if item_choice == "EXIT":
			break
		elif item_choice in game_data["items"]:
			game_data["equipped_item"] = item_choice
			break
		else:
			print("You don't have that item.")
			
	if game_data["equipped_item"] == "GOLDEN APPLE":
		game_data["MAX_HP"] += 5
	elif game_data["equipped_item"] == "GOLDEN ORANGE":
		game_data["ATK"] += 2
	elif game_data["equipped_item"] == "GOLDEN MANGO":
		game_data["MAX_HP"] += 5
		game_data["ATK"] += 2
	elif game_data["equipped_item"] == "RATIONS":
		game_data["HP"] = game_data["MAX_HP"]
		
	return game_data
	

def main():

	instructions()
	game_data = init_game_data()
	print("\nYour ship has landed on the planet Indra and your mission is to search for new species to bring back to Earth.\n")
	location_description(game_data["player_location"])
	
	while game_data["open"] == True:
		command = handle_input(game_data, input("What would you like to do next? ").strip().upper().split())
		
		if command == "invalid_input":
			continue
		
		if command == "NORTH" or command == "EAST" or command == "WEST" or command == "SOUTH":
			update_location(game_data, command)
		
		elif command == "HELP":
			instructions()
			
		elif command == "LOOK":
			location_description(game_data["player_location"])
			NPC(game_data["player_location"])
			items(game_data, game_data["player_location"], False)
			
		elif command == "SCORE":
			print("CURRENT SCORE: ", end = "")
			print(game_data["score"])
			
		elif command == "TALK":
			interaction(game_data["player_location"], game_data)
			
		elif command == "BAG":
			bag(game_data)
			
		elif command == "PICKUP":
			items(game_data, game_data["player_location"], True)
		
		elif command == "QUIT":
			game_data["open"] = False
		
		update_score(game_data)
		
	print("Congratulations! You've managed to discover many different new species, unconver some of the secrets of this world and have completed your mission!\n\nYOU WIN!")


if __name__ == "__main__":
	main()