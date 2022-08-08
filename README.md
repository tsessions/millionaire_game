# millionaire_game
A simple game of "Who Wants to be a Millionaire" that can be run solely on Turtle graphics.

This was a game I developed early in my college career as a final project for my introductory Python class. Since then, I have streamlined mamy of the  functions and improved on the in-game logic. I was able to cut the number of lines down to just over half of the game's original size and with greater functionality.  There was a concept added that has been commented out that would have allowed for "Ask the Audience" functionality with matplotlib, but I decided against implementing it as a main feature, because I wanted the game to be solely playable on one screen. Bar charts on matplotlib output in the IDLE shell instead of on the turtles interface. The question bank is small (~ 50 questions), and there are 15 possible questions to be asked each game. Note that each of the player aids (ask the audience, 50/50, phone-a-friend) can only be used once each. 

NOTES
The turtles aspect of the programming is slightly buggy, so in order for the game to run smoothly, please allow the animations to compelely finish before clicking anything on the screen. I am currently working on a way to fix this issue.

I am also almost done fixing a problem where the different player aids (50/50, ask the audience, phone a friend) do not build on each other. For example, when you eliminate half the answer choices with 50/50, I am setting the ask the audience and phone a friend to only select from remaining options.
