Requires:
	python 3.5
	pytorch 0.4
Important files:
	DQN.py
	pacmanDQN_Agents.py 


To test the DQN network, launch:
	python3 pacman.py -p PacmanDQN -n 200 -x 100 -l smallGrid

To train the DQN network, launch:
	python3 pacman.py -p PacmanDQN -n 3000 -x 2900 -l smallGrid

Where:
	-n = number of episodes
	-x = episodes used for training (graphics = off)

Remarks:
	the game files had to be updated for python3 (print was not working)
	the model has already been trained and wins most of the time
	the model has been optimized, it requires less then 30 000 episodes to converge
	
To test training, change:
	model_trained = False
		in pacmanDQN_Agents.py (line 26)

