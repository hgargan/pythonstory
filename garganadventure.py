#!/usr/bin/env python

print "You are the Seattle Seahawks. It is the fourth quarter of the Super Bowl, and you have the ball on the 50 yard-line with a minute remaining. Do you decide to throw (1) or run (2)?"

playcall = raw_input(">")

if playcall == "1":
    print "You are a receiver, and unfortunately, you find yourself in double coverage with the ball headed your way. What do you do?"
    print "Attempt to catch the ball (1)"
    print  "Make friends with the defenders and convince them that winning isn't that important (2)"
    receiveraction = raw_input(">")
    
    if receiveraction == "1":
        print "You jump, but to no avail. You see one of the defenders paw the ball down toward the ground."
        print "But you're on the ground! The ball bounces once off your thigh and into your grasp. Good job!"
        
    elif receiveraction == "2":
        print "Success! You have taught your comrades in competition the true meaning of the word."
        print "The three of you shake hands on the sideline as the ball falls harmlessly to the turf, taking a lopsided bounce out of bounds."
    else:
        print "Well, I suppose that's an option too. Unfortuantely, it results in the Patriot interception and victory. You have let America down."
        
elif playcall == "2":
    print "You have options. You, Russell Wilson, are a very mobile quarterback, but you have Marshawn 'Beast Mode' Lynch in your backfield."
    print "Do you (1) keep the ball and scramble for a first down?"
    print "Do you (2) run a play for Marshawn?"
    print "Or would you rather hand the ball off to someone else (3) and see what happens?"
    
    runaction = raw_input (">")
    
    if runaction == "1":
        print "Good move, Russell!"
        print "A passing seahawk, impressed with your guile, swoops down and allows you safe passage to the end zone upon its feathered back. Well done indeed!"
    elif runaction == "2":
        print "Marshawn Lynch, assuming that he might be required to give an interview if he scores a game-winning touchdown, hesitates."
        print "He stares at the ball, cradling it softly, and begins to sing a song his mother used to sing to him."
        print "When Marshawn is singing, he retreats into his own world. The crowd, the flashes, the reporters -- they all vanish."
        print "The Seahawks' star running back sits down on the field, eyes closed, rocking back and forth. Pandemonium ensues. But Marshawn doesn't care."
        print "Today, Marshawn is happy."
    elif runaction == "3":
        print "Well, I suppose the Seahawks DO have other running backs. We haven't heard of them, though."
        print "Neither have the Patriots. The element of surprise works in your favor! Touchdown, Seahawks!"