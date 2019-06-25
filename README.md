Idea and Mission Statement: 

The aim of this project is to create an interactive music player that uses data from a facial recognition program to actuate playing a xylophone. This project is an extension of a facial recognition music player that Mary has developed previously in the fall 2018 semester that used three different facial cues each to play a different song and aimed to highlight inter-computer connections. Along with being just a fun thing to play with, this could also be used to teach people about and aid people with playing music especially young children and the physically or developmentally handicapped. Although this project will be realized on a small scale, it has the potential to be expanded to full sized keyboards which would not only be fun but could be used to aid in accessibility for piano players who are no longer able to play with their hands.

The original vision for the project was a fully-digital MIDI-connected facial recognition program, but upon researching MIDI inputs for python we were unable to find many good options for importing a basic note-playing system besides jythonmusic, which is a little too limited for this project. Calvin has previously created a midi visualizer that we would consider weaving into this project if we want to up the “art” element, but the main goal and focus of this project is a mechanical xylophone player. 

The new plan for this project is to create a monitor interface that will collect facial data and use it to control hammers that will play a small “kid’s” xylophone. We want to include a dial that allows the user to switch between three modes of gameplay. The first would be a one to one mapping where specific facial or hand gestures (possibly asl?) would produce specific and predictable results by playing specific notes on the xylophone. This would be most useful for allowing users who are physically handicaped to still play music and has the potential to be expanded into larger instruments as a physical aid. The second mode would be “emo” mode, in which the facial detection software would read the emotion of the user (or combinations of emotions) and produce a song of the appropriate mood and intensity to match that of the user. This would require emotions to be mapped two dimensionally, with the positivity or negativity of the emotion on one axis and the intensity of that emotion on the other. Affdex has a feature that detects emotion, but we believe some refining might be necessary to make it perfect. Not only could this produce interesting and fun results, but could also be useful and interesting in helping individuals on the autism spectrum better understand emotion. There has been research done that suggests that autistic listeners of music respond in the same way that non-autistic listeners of music do and so by directly mapping facial expressions of emotions to fitting music to match that emotion it could help individuals on the autism spectrum to more concretely correlate facial expressions with emotion. The third mode would be a challenge mode which would be a game similar to simon says in which a note or tune would be played on the xylophone and then the user would have to try and recreate that by repeating the correct facial or hand gestures. This would be more of a stretch goal for the project, but it would be a fun way for first time users to learn how to use the manual one to one mapping mode by understanding which facial gestures will produce the desired results. 
	


Technologies: 

The bulk of the code for this project is being written in python and run from the terminal. We are planning on using the affdexMe software for facial recognition, although we do want to edit the source code a little to alter the display to make it simpler and more aesthetically cohesive. We have also discussed the possibility of using a leap motion to incorporate hand motions as well, although that is not the main focus at the moment. 
	
For the ‘emo’ mode of the project we are hoping to use wekinator to run our inputs through a linear regression model and then have it output the appropriate tune on the xylophone. We will need some help making that integration smooth and easy to understand and use, but with our current understanding of wekinator we believe that will be the best route. 

We plan on 3D printing one mallet for each key on the xylophone—8 in total—and then using servos in order to make the mallet hit the keys. Talia and Mary have more experience with servos and arduino so we are leaning more towards using those, but of course we will need to make sure they will hold up to what we need. Additionally we are thinking of including a physical dial to shift between modes of gameplay. 


Challenges: 

There are of course many things that could go wrong in this project, especially with something that has so many moving parts, but I think the biggest challenge will be deciding on eight unique expressions that will control each of the mallets and then training the model to be able to actually distinguish between each of those expressions and recognize a blend of them and react accordingly. Mary has already tested this a little in the early drafts of the code, but we will need to work to nuance and add to her findings so far. 

It will also be difficult to get the mapping for the emo mode down so that a variety of complex emotions will be not only correctly understood, but also correctly expressed through song. I don’t think we would want it to just play on specific song depending on the emotion, but rather we would want it to produce a simple piece of music in a key and intensity that is fitting to the emotion. This may have to be simplified depending on what blockers we run into, but at the moment that is the goal. 

In addition it could be difficult getting all the mallets to react in a speedy fashion to make it clear which facial gestures are sparking each reaction. It could also potentially be difficult to get the mallets to hit the keys in an appropriate way so that they make enough sound but are also not over aggressive or overly tentative and are only hitting one key at a time.

Lastly, we want this to be something that people of all ages and skill levels can use quickly and easily, so we want the “on boarding” for the program to be fast and efficient so designing an aesthetic and simple UI will be important and could be challenging. 

Research: 
	Austism, music, and emotion; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3853405/


