# XyloProj-or-FaceTune-

Idea and Mission Statement: 

		The aim of this project is to create an interactive music player that uses data from a facial recognition program to actuate playing a xylophone. This project is an extension of a facial recognition music player that Mary has developed previously in the fall 2018 semester that used three different facial cues each to play a different song. Along with being just a fun thing to play with, this could also be used to teach people about and aid people with playing music especially young children and the physically or developmentally handicapped. Although this project will be realized on a small scale, it has the potential to be expanded to full sized keyboards which would not only be fun but could be used to aid in accessibility for piano players who are no longer able to play.

	The original vision for the project was a fully-digital MIDI-connected facial recognition program, but upon researching MIDI inputs for python we were unable to find many good options for importing a basic note-playing system besides jythonmusic, which is a little too limited for this project. Calvin has previously created a midi visualizer that we would consider weaving into this project, but the main goal and focus of this project is a mechanical xylophone player. 

	The new plan for this project is to create a monitor interface that will collect facial data and use it to control hammers that will play a small “kid’s” xylophone. We are still deciding what facial gestures we want to use to control the hammers and how exactly we want to use machine learning in the project, but we will be more able to sort out those specifics once we have a working model. 
	
Technologies: 

	The bulk of the code for this project is being written in python and run from the terminal. We are planning on using the afdex me (that’s what it’s called right) (please spell check this Mary!) software for the facial recognition, although we do want to edit the source code a little to alter the display. We have also discussed the possibility of using a leap motion to incorporate hand motions as well, although that is not the main focus at the moment. 

	We plan on 3D printing one mallet for each key on the xylophone—8 in total—and then using solenoids or arduinos (spelling?) in order to make the mallet hit the keys. Talia and Mary have more experience with arduinos so we are leaning more towards using those, but of course we will need to make sure they will hold up to what we need.


Challenges: 

	There are of course many thing that could go wrong in this project, especially with something that has so many moving parts, but I think the biggest challenge will be deciding on eight unique expressions that will control each of the mallets and then training the model to be able to actually distinguish between each of those expressions and recognize a blend of them and react accordingly. 

	In addition it could be difficult getting all the mallets to react in a speedy fashion to make it clear which facial gestures are sparking each reaction. It could also potentially be difficult to get the mallets to hit the keys in an appropriate way so that they make enough sound but are also not over aggressive or overly tentative and are only hitting one key at a time.

	Lastly, we want this to be something that people of all ages and skill levels can use quickly and easily, so we want the “on boarding” for the program to be fast and efficient so designing an aesthetic and simple UI will be important and could be challenging. 
