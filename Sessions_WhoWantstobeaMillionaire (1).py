#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Tommas Sessions
#Comp112-01 Final Project: Who Wants to be a Millionaire?
#Many, but not all, of these game questions were adapted from a publicly posted JSON project:
#https://pastebin.com/QRGzxxEy

import random
import turtle
import matplotlib.pyplot as plt

def titlescreen():
#signature: None->None
#no preconditions
#lays out the title screen
    turtle.bgcolor("darkblue")
    turtle.hideturtle()
    turtle.color("white")
    turtle.title("Who Wants to Be a Millionaire")
    turtle.setup(2500,1000,0,0)
    turtle.penup()
    turtle.goto(0,150)
    turtle.write("Welcome to",font=title1,align="center")
    turtle.goto(0,75)
    turtle.write("Who Wants to be a Millionaire!",font=subtitle,align="center")

    #dollar signs
    turtle.speed(10)
    turtle.color("lightgreen")
    turtle.goto(-450,-400)
    turtle.write("$",font=dollarsign,align="center")
    turtle.goto(450,-400)
    turtle.write("$",font=dollarsign,align="center")

    #play button
    turtle.speed(7)
    turtle.color("yellow")
    turtle.pensize(5)
    turtle.goto(-175,-50)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(265)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(115)
    turtle.penup()
    turtle.goto(-150,-125)
    turtle.write("Let's Play!",font=mainmenubutts,align="center")

    #quit button
    turtle.goto(135,-60)
    turtle.pendown()
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(150,-125)
    turtle.write("Quit",font=mainmenubutts,align="center")
    turtle.onscreenclick(mainmenuclick)
    turtle.listen()
    turtle.done()

def mainmenuclick(x,y):
#signature:float,float->None
#no preconditions
#decides whether or not to run the game
    if x>=-290 and x<=-25 and y>=-150 and y<=-50: #play
        print(question_fill())
    elif x>=85 and x<=210 and y>=-135 and y<=-60: #quit
        turtle.bye()

def phoneafriend(question):
#signature: str->None
#no preconditions
#70% chance of your friend giving you the right answer
    x=random.randint(1,100)
    global pafct
    global ftyftyct
    global trimmed
    if ftyftyct<1:
        if x<=70:
            turtle.penup()
            turtle.goto(-25,0)
            turtle.write("Your friend advises you to pick "+str(qbase[question][0]),font=afont,align="center")
        else:
            friend_rec=random.choice(qbase[question][1:])
            turtle.penup()
            turtle.goto(-25,0)
            turtle.write("Your friend advises you to pick "+str(friend_rec),font=afont,align="center")
    else:
        if x<=70:
            turtle.penup()
            turtle.goto(-25,0)
            turtle.write("Your friend advises you to pick "+str(qbase[question][0]),font=afont,align="center")
        else:
            friend_rec=random.choice(trimmed)
            while friend_rec == rightanswers[i]:
                friend_rec == random.choice(trimmed) #pick the wrong answer since the friend is not helpful in this setting
            turtle.penup()
            turtle.goto(-25,0)
            turtle.write("Your friend advises you to pick "+str(friend_rec),font=afont,align="center")
    pafct+=1

def fiftyfifty(i):
#signature: str->None
#no preconditions
#eliminates 2 of the three wrong answers
    global ftyftyct
    global trimmed
    global answers_remaining
    trimmed= list(finalanswers[i]) #starts as all answers
    correct = rightanswers[i]
    a = 0 #number of answers dropped
    while a<2: #only want to remove two answers
        drop=random.choice(trimmed)
        while drop==correct: #pick a random incorrrect answer to pop from available choices.
            drop=random.choice(trimmed)
        trimmed.remove(drop) #removes the first of two answers
        a+=1
    print(trimmed)
    print(rightanswers[i])
    
    answers_remaining = [1,2,3,4] #to be used in ask the audience for a logic interaction
    print(answers_remaining)
    print(finalanswers[i])
    
    if finalanswers[i][0] not in trimmed: #a does not remain
        answers_remaining.remove(1)
        print("ONTO A NOT IN TRIMMED")
        print(finalanswers[i][0])
        print(answers_remaining)
        print('a booted')
        turtle.color("white","darkblue")
        turtle.goto(-400,-50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    if finalanswers[i][1] not in trimmed: #b does not remain
        answers_remaining.remove(2)
        print("ONTO B NOT IN TRIMMED")
        print(finalanswers[i][1])
        print(answers_remaining)
        print('b booted')
        turtle.color("white","darkblue")
        turtle.goto(50,-50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    if finalanswers[i][2] not in trimmed: #c does not remain
        answers_remaining.remove(3)
        print("ONTO C NOT IN TRIMMED")
        print(finalanswers[i][2])
        print('c booted')
        turtle.color("white","darkblue")
        turtle.goto(-400,-200)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    if finalanswers[i][3] not in trimmed: #d does not remain
        answers_remaining.remove(4)
        print("ONTO D NOT IN TRIMMED")
        print(finalanswers[i][3])
        print('d booted')
        turtle.color("white","darkblue")
        turtle.goto(50,-200)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.end_fill()
        turtle.penup()
    ftyftyct+=1

def asktheaudience(question,i):
#signature: str->None
#no preconditions
#75% chance of the audience giving you a correct answer
    global atact
    global ftyftyct
    global answers_remaining
    #graph config
    turtle.penup()
    turtle.goto(-700,150)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(200)
    turtle.penup()
    turtle.goto(-700,150)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(180)
    turtle.penup()
    turtle.goto(-670,120)
    turtle.write("A",font=afont,align="center")
    turtle.goto(-630,120)
    turtle.write("B",font=afont,align="center")
    turtle.goto(-590,120)
    turtle.write("C",font=afont,align="center")
    turtle.goto(-550,120)
    turtle.write("D",font=afont,align="center")
        
    def barplot(height_a, height_b, height_c, height_d):
            #answer a
            turtle.penup()
            turtle.goto(-680,150)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(2*height_a)
            turtle.right(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(2*height_a)
            turtle.left(90)
            
            #answer b
            turtle.penup()
            turtle.goto(-640,150)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(2*height_b)
            turtle.right(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(2*height_b)
            turtle.left(90)
            
            #answer c
            turtle.penup()
            turtle.goto(-600,150)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(2*height_c)
            turtle.right(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(2*height_c)
            turtle.left(90)
            
            #answer d
            turtle.penup()
            turtle.goto(-560,150)
            turtle.pendown()
            turtle.left(90)
            turtle.forward(2*height_d)
            turtle.right(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(2*height_d)
            turtle.left(90)
    
    r=random.randint(0,101)
    
    if ftyftyct < 1:
            
        if r<=75: #audience is helpful
            s=random.randint(40,95)
            t=random.randint(0,100 - s)
            u=random.randint(0,100 - s - t)
            v=100-s-t-u
            
            if finalanswers[i][0]==rightanswers[i]: #a is correct
                barplot(s,t,u,v)
            elif finalanswers[i][1]==rightanswers[i]: #b is correct
                barplot(t,s,u,v)
            elif finalanswers[i][2]==rightanswers[i]: #c is correct
                barplot(t,u,s,v)
            else: #d is correct
                barplot(t,u,v,s)
                
        else: #unhelpful audience
            s=random.randint(0,95)
            t=random.randint(0,100-s)
            u=random.randint(0,100-s-t)
            v=100-s-t-u
        
            barplot(s,t,u,v)
            
        atact+=1 # counter ensures ask the audience is only used once per game.
        
        """ This was a concept for including matplotlib, but I'd like for the whole game to be playable 
        in one screen without return to the launcher to see the graph.
        
        fig,ax = plt.subplots()
        
        if finalanswers[i][0]==rightanswers[i]: #a is correct
            ata.append(0,s)
        elif finalanswers[i][1]==rightanswers[i]: #b is correct
            ata.append(1,s)
        elif finalanswers[i][2]==rightanswers[i]: #c is correct
            ata.append(2,s)
        else:
            ata.append(3,s)
            
        ax.plot(["A","B","C","D"],ata)
        ax.show()
        
        """
    else: #used fifty fifty already, meaning the audience only picks from the two remaining options
        
        if r<=75: #audience is helpful
            s=random.randint(51,95)
            t=random.randint(0,100 - s)
            
            if finalanswers[i][0]==rightanswers[i]: #a is correct
                answers_remaining.remove(1)
                if answers_remaining[0]==2: #b incorrect & the other answer
                    barplot(s,t,0,0)
                elif answers_remaining[0]==3: #c incorrect & the other answer
                    barplot(s,0,t,0)
                elif answers_remaining[0]==4: #d incorrect & the other answer
                    barplot(s,0,0,t)
            elif finalanswers[i][1]==rightanswers[i]: #b is correct
                answers_remaining.remove(2)
                if answers_remaining[0]==1: #a incorrect & the other answer
                    barplot(t,s,0,0)
                elif answers_remaining[0]==3: #c incorrect & the other answer
                    barplot(0,s,t,0)
                elif answers_remaining[0]==4: #d incorrect & the other answer
                    barplot(0,s,0,t)
            elif finalanswers[i][2]==rightanswers[i]: #c is correct
                answers_remaining.remove(3)
                if answers_remaining[0]==1: #a incorrect & the other answer
                    barplot(t,0,s,0)
                elif answers_remaining[0]==2: #b incorrect & the other answer
                    barplot(0,t,s,0)
                elif answers_remaining[0]==4: #d incorrect & the other answer
                    barplot(0,0,s,t)
            else: #d is correct
                answers_remaining.remove(4)
                if answers_remaining[0]==1: #a incorrect & the other answer
                    barplot(t,0,0,s)
                elif answers_remaining[0]==2: #b incorrect & the other answer
                    barplot(0,t,0,s)
                elif answers_remaining[0]==3: #c incorrect & the other answer
                    barplot(0,0,t,s)
                
        else: #unhelpful audience
            s=random.randint(0,95)
            t=random.randint(0,100-s)
            
            if 1 in answers_remaining: #a is one of the answers available
                if 2 in answers_remaining: #a,b are the two choices
                    barplot(s,t,0,0)
                elif 3 in answers_remaining: #a,c are the two choices
                    barplot(s,0,t,0)
                else: #a,d are the two choices
                    barplot(s,0,0,t)
            elif 2 in answers_remaining: #b is one of the answers available
                if 3 in answers_remaining: #b,c are the two choices
                    barplot(0,s,t,0)
                else: #b,d are the two choices.
                    barplot(0,s,0,t)
            else: #c,d is the last possible combination that can't be made from the logic above
                barplot(0,0,s,t)
            
        atact+=1 # counter ensures ask the audience is only used once per game.
    
def questionlayout():
#signature: None->None
#no preconditions
#lays out the empty board for a question
    global i
    turtle.color("white")
    turtle.clear()
    random.shuffle(finalanswers[i])
    turtle.penup()
    turtle.goto(0,200)
    turtle.write("Question "+str(i+1),font=title1,align="center")
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    test=finalquestions[i].split()
    if len(test)>=9:
        testuh=str.join(' ',test[:int(len(test)/2)])
        testlh=str.join(' ',test[int(len(test)/2):])
        turtle.penup()
        turtle.write(testuh,font=qfont,align="center")
        turtle.goto(0,50)
        turtle.write(testlh,font=qfont,align="center")
    else:
        turtle.write(finalquestions[i],font=qfont,align="center")
        turtle.penup()
    # Box A
    turtle.goto(-385,-75)
    turtle.write("A)",font=afont,align="left")
    turtle.goto(-400,-50)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.goto(-250,-110)
    turtle.write(finalanswers[i][0],font=afont,align="center")
        
    # Box B
    turtle.goto(75,-75)
    turtle.write("B)",font=afont,align="left")
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.goto(195,-110)
    turtle.write(finalanswers[i][1],font=afont,align="center")

    # Box C
    turtle.goto(-385,-225)
    turtle.write("C)",font=afont,align="left")
    turtle.goto(-400,-200)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.goto(-250,-260)
    turtle.write(finalanswers[i][2],font=afont,align="center")

    # Box D
    turtle.goto(75,-225)
    turtle.write("D)",font=afont,align="left")
    turtle.goto(50,-200)
    turtle.pendown()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.goto(195,-260)
    turtle.write(finalanswers[i][3],font=afont,align="center")

    # Phone a Friend
    if pafct<1:
        if i > 0:
            turtle.speed(10)
        else:
            pass
        turtle.goto(-700,0)
        turtle.pendown()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.penup()
        turtle.goto(-600,-60)
        turtle.write("Phone a Friend",font=afont,align="center")

    # 50/50
    if ftyftyct<1:
        turtle.goto(-700,-125)
        turtle.pendown()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.penup()
        turtle.goto(-600,-185)
        turtle.write("50/50",font=afont,align="center")

    # Ask the Audience
    if atact<1:
        turtle.goto(-700,-250)
        turtle.pendown()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.penup()
        turtle.goto(-600,-310)
        turtle.write("Ask the Audience",font=afont,align="center")

    # Money Counter
    turtle.penup()
    turtle.goto(700,-320)
    turtle.color("yellow")
    turtle.write('$0',font=afont,align="right")
    
    turtle.goto(700,-290)
    turtle.color("lightgreen")
    turtle.pendown()
    turtle.write('$100',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-260)
    turtle.pendown()
    turtle.write('$200',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-230)
    turtle.pendown()
    turtle.write('$300',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-200)
    turtle.pendown()
    turtle.write('$500',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-170)
    turtle.color("yellow")
    turtle.pendown()
    turtle.write('$1,000',font=afont,align="right") #checkpoint
    turtle.penup()

    turtle.goto(700,-140)
    turtle.color("lightgreen")
    turtle.pendown()
    turtle.write('$2,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-110)
    turtle.pendown()
    turtle.write('$4,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-80)
    turtle.pendown()
    turtle.write('$8,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-50)
    turtle.pendown()
    turtle.write('$16,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,-20)
    turtle.pendown()
    turtle.write('$25,000',font=afont,align="right") #checkpoint
    turtle.penup()

    turtle.goto(700,10)
    turtle.pendown()
    turtle.write('$50,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,40)
    turtle.pendown()
    turtle.write('$100,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,70)
    turtle.pendown()
    turtle.write('$250,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,100)
    turtle.pendown()
    turtle.write('$500,000',font=afont,align="right")
    turtle.penup()

    turtle.goto(700,130)
    turtle.pendown()
    turtle.color("yellow")
    turtle.write('$1,000,000',font=afont,align="right")
    turtle.penup()
    
    # Exit
    turtle.goto(650,375)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.penup()
    turtle.goto(660,355)
    turtle.write("X",font=exfont,align="center")

def aright(i):
#signature: int->None
#no preconditions
#handles a being correct and clicked
    turtle.color("white","lightgreen")
    turtle.penup()
    turtle.goto(-400,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-250,-110)
    turtle.write(finalanswers[i][0],font=afont,align="center")
def awrong(i):
#signature: int->None
#no preconditions
#handles a being incorrect and clicked
    turtle.color("white","orange")
    turtle.penup()
    turtle.goto(-400,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-250,-110)
    turtle.write(finalanswers[i][0],font=afont,align="center")
def bright(i):
#signature: int->None
#no preconditions
#handles b being correct and clicked
    turtle.color("white","lightgreen")
    turtle.penup()
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(195,-110)
    turtle.write(finalanswers[i][1],font=afont,align="center")
def bwrong(i):
#signature: int->None
#no preconditions
#handles b being incorrect and clicked
    turtle.color("white","orange")
    turtle.penup()
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(195,-110)
    turtle.write(finalanswers[i][1],font=afont,align="center")
def cright(i):
#signature: int->None
#no preconditions
#handles c being correct and clicked
    turtle.color("white","lightgreen")
    turtle.penup()
    turtle.goto(-400,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-250,-260)
    turtle.write(finalanswers[i][2],font=afont,align="center")
def cwrong(i):
#signature: int->None
#no preconditions
#handles c being incorrect and clicked
    turtle.color("white","orange")
    turtle.penup()
    turtle.goto(-400,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-250,-260)
    turtle.write(finalanswers[i][2],font=afont,align="center")
def dright(i):
#signature: int->None
#no preconditions
#handles d being correct and clicked
    turtle.color("white","lightgreen")
    turtle.penup()
    turtle.goto(50,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(195,-260)
    turtle.write(finalanswers[i][3],font=afont,align="center")
def dwrong(i):
#signature: int->None
#no preconditions
#handles d being incorrect and clicked
    turtle.color("white","orange")
    turtle.penup()
    turtle.goto(50,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(195,-260)
    turtle.write(finalanswers[i][3],font=afont,align="center")

def endreset(x,y):
#signature: float,float->None
#no preconditions
#guides the player after their crushing defeat
    if x>=-290 and x<=-25 and y>=-150 and y<=-50: #play
        turtle.reset()
        global ftyftyct
        global atact
        global pafct
        global nd
        global qupotential
        global apotential
        global rightanswers
        global finalanswers
        global finalquestions
        ftyftyct=0
        atact=0
        pafct=0
        trimmed=[]
        

        qupotential=[] #list of all possible questions
        apotential=[] #list of all possible answers
        rightanswers=[] #list of right answers

        for question in qbase:
            qupotential.append(question)
            apotential.append(qbase[question])
    
        n=0
        finalquestions=[] #randomly selects 15 questions from the dict to ask player
        finalanswers=[]
        while n<15:
            x=random.randint(1,len(qupotential)-1)
            finalquestions.append(qupotential.pop(x))
            finalanswers.append(apotential.pop(x))
            n+=1

        for item in finalanswers:
            rightanswers.append(item[0])
        
        print(titlescreen())
        
    elif x>=85 and x<=210 and y>=-135 and y<=-60: #quit
        turtle.bye()

def youlose(i):
#signature: None->None
#no preconditions
#tells the player they've lost
    turtle.clear()
    turtle.bgcolor("orange")
    turtle.color("white")
    turtle.penup()
    turtle.goto(0,150)
    turtle.write("You lose!",font=title1,align="center")
    turtle.goto(0,75)
    if i<4:
        dval=0
    elif i>=4 and i<=9:
        dval=1000
    elif i>=10:
        dval=25000
    turtle.write("You made $"+str(dval),font=subtitle,align="center")

    #dollar signs
    turtle.speed(10)
    turtle.color("darkgreen")
    turtle.goto(-450,-400)
    turtle.write("$",font=dollarsign,align="center")
    turtle.goto(450,-400)
    turtle.write("$",font=dollarsign,align="center")

    #menu button
    turtle.speed(7)
    turtle.color("yellow")
    turtle.pensize(5)
    turtle.goto(-175,-50)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(265)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(115)
    turtle.penup()
    turtle.goto(-150,-125)
    turtle.write("Main Menu",font=mainmenubutts,align="center")

    #quit button
    turtle.goto(135,-60)
    turtle.pendown()
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(150,-125)
    turtle.write("Quit",font=mainmenubutts,align="center")
    
    turtle.onscreenclick(endreset)
    turtle.listen()
    turtle.done()

def youwin():
#signature: None->None
#no preconditions
#tells the player they've won a million dollars
    turtle.clear()
    turtle.bgcolor("lightgreen")
    turtle.color("darkgreen")
    turtle.penup()
    turtle.goto(0,150)
    turtle.write("YOU'VE WON A MILLION DOLLARS!",font=subtitle,align="center")
    turtle.goto(0,75)
    turtle.write("CONGRATULATIONS!",font=subtitle,align="center")

    #dollar signs
    turtle.speed(10)
    turtle.color("darkgreen")
    turtle.goto(-450,-400)
    turtle.write("$",font=dollarsign,align="center")
    turtle.goto(450,-400)
    turtle.write("$",font=dollarsign,align="center")

    #menu button
    turtle.speed(7)
    turtle.color("darkgreen")
    turtle.pensize(5)
    turtle.goto(-175,-50)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(265)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(115)
    turtle.penup()
    turtle.goto(-150,-125)
    turtle.write("Main Menu",font=mainmenubutts,align="center")

    #quit button
    turtle.goto(135,-60)
    turtle.pendown()
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(125)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(150,-125)
    turtle.write("Quit",font=mainmenubutts,align="center")
    
    turtle.onscreenclick(endreset)
    turtle.listen()
    turtle.done()
    
def question_fill():
##signature: None->None
#no preconditions
#populates each question
    global i #bring in the question counter
    if i < 15:
        print(questionlayout())
        turtle.goto(700,money_counter[i][0])
        turtle.color("white")
        turtle.pendown()
        turtle.write(money_counter[i][1],font=afont,align="right")
        turtle.penup()
        turtle.onscreenclick(question_check)
        turtle.listen()
        turtle.done()
    else:
        print(youwin())

    
def question_check(x,y):
##signature: float,float -> None
#no preconditions
#determines if a given answer is correct or not
    global i #question counter
    if x>=-400 and x<=-100 and y>=-150 and y<=-50: #clicks a
        if finalanswers[i][0]==rightanswers[i]: #a correct
            print(aright(i))
            i+=1
            print(question_fill())
        else: # a wrong
            print(awrong(i))
            print(youlose(i))
    elif x>=50 and x<=350 and y>=-150 and y<=-50: #clicks b
        if finalanswers[i][1]==rightanswers[i]: #b correct
            print(bright(i))
            i+=1
            print(question_fill())
        else: # b wrong
            print(bwrong(i))
            print(youlose(i))
    elif x>=-400 and x<=-100 and y>=-300 and y<=-200: #clicks c
        if finalanswers[i][2]==rightanswers[i]: #c correct
            print(cright(i))
            i+=1
            print(question_fill())
        else: #c wrong
            print(cwrong(i))
            print(youlose(i))
    elif x>=50 and x<=350 and y>=-300 and y<=-200: #clicks d
        if finalanswers[i][3]==rightanswers[i]: #d correct
            print(dright(i))
            i+=1
            print(question_fill())
        else: #d wrong
            print(dwrong(i))
            print(youlose(i))
    elif x>=-700 and x<=-500 and y>=-100 and y<=0 and pafct<1: #phoneafriend
        print(phoneafriend(finalquestions[i]))
    elif x>=-700 and x<=-500 and y>=-225 and y<=-125 and ftyftyct<1: #50/50
        print(fiftyfifty(i))
    elif x>=-700 and x<=-500 and y>=-350 and y<=-250: #asktheaudience
        print(asktheaudience(finalquestions[i],i))
    elif x>=650 and x<=670 and y>=355 and y<=375: #exit
        turtle.bye()
    else:
        pass

title1=("Times New Roman",120,"bold")
subtitle=("Times New Roman",80,"bold")
dollarsign=("Times New Roman",500,"bold")
mainmenubutts=("Times New Roman",50,"bold")
qfont=("Times New Roman",40,"bold")
afont=("Times New Roman",25,"bold")
exfont=("Times New Roman",20,"bold")
pafct=0 #how many times phone a friend was used, tolerance =1
ftyftyct=0 #how many times fifty fifty was used, tolerance =1
atact=0 #how many times ask the audience was used, tolerance =1

qbase=dict()
qbase['A knish is traditionally stuffed with what filling?']=['potato','creamed corn','lemon custard','raspberry jelly']
qbase['A triptych is a work of art that is painted on how many panels?']=['three','two','five','eight']
qbase["According to Greek mythology, who was Apollo's twin sister?"]=['Artemis','Aphrodite','Venus','Athena']
qbase["Ada Lovelace is credited with being the first person to have made what?"]=["a computer program","a souffle","a brassiere","a mystery novel"]
qbase["Backgammon is a how many player game?"]=["Two","Three","Four","Six"]
qbase["Before he went into coaching, Phil Jackson played for which of the following NBA teams?"]=['New York Knicks','Boston Celtics','Los Angeles Lakers','Philadelphia 76ers']
qbase["Cheddar cheese got its name from a village in what country?"]=["England","France","Switzerland","Denmark"]
qbase["During which war did Francis Scott Key write the words to 'The Star-Spangled Banner'?"]=["War of 1812","American Revolution","Civil War","World War I"]
qbase["Elephant Tusks are made of what material?"]=["ivory","coral","bone","calcium"]
qbase["Excluding wisdom teeth, how many adult teeth do humans have?"]=["28","32","35","40"]
qbase["From what language does the term 'R.S.V.P.' originate?"]=["French","Russian","Italian","Portuguese"]
qbase["How long is a single term in the US Senate?"]=["six years","two years","four years","eight years"]
qbase["How long is the time on an NBA shot clock?"]=["24 seconds","18 seconds","30 seconds","35 seconds"]
qbase["How many keys are on a standard piano?"]=["88","20","54","100"]
qbase["How many spikes are on the Statue of Liberty's crown?"]=["seven","five","nine","thirteen"]
qbase["In 1909, Fredrick Cook claimed to be the first explorer to reach which location?"]=["North Pole","Mount Everest","Bermuda Triangle","Atlantis"]
qbase["In 1960, Nazi official Adolph Eichmann was finally captured in which country?"]=["Argentina","Brazil","East Germany","Paraguay"]
qbase["In an adult human, how long is the large intestine?"]=["one foot","five feet","twelve feet","twenty feet"]
qbase["In Mr. Rogers's theme song, what does he ask you to be?"]=["his neighbor","his friend","his student","all you can be"]
qbase["Which month is the first day of spring in?"]=["March","February","April","May"]
qbase["In what country did Pokemon originate?"]=["Japan","United States","Hungary","Canada"]
qbase["Which industry did John D. Rockefeller make his fortune in during the Gilded Age?"]=["oil","automobile","steel","railroad"]
qbase["Which former US President is found on the $2 bill?"]=["Thomas Jefferson","Franklin Delano Roosevelt","James K. Polk","Harry S. Truman"]
qbase["Modern computer microchips are primarily composed of what element?"]=["Silicon","Sodium","Aluminum","Silver"]
qbase["On a set of jumper cables, what color designates the negative connector?"]=["Black","Red","White","Blue"]
qbase["On Valentine's Day 2000, NASA's NEAR spacecraft began a yearlong orbit of what asteroid?"]=["Eros","Cupid","Aphrodite","Venus"]
qbase["Paper burns at what temperature in Fahrenheit?"]=["451 degrees","98.6 degrees","212 degrees","342 degrees"]
qbase["Stevie Wonder and Michael Jackson have both recorded duets with which former Beatle?"]=["Paul McCartney","John Lennon","George Harrison","Ringo Starr"]
qbase["The Original Apple iMac computer was available in all of the following colors except which?"]=["Kiwi","Tangerine","Strawberry","Grape"]
qbase["The film 'Stand By Me' is based on a novel by what author?"]=["Stephen King","Anne Proulx","Dean Koontz","Frank McCourt"]
qbase["The first commercial radio station was located in what city?"]=["Pittsburgh","Chicago","Austin","Cleveland"]
qbase["The sport of judo comes from what Asian country?"]=["Japan","Vietnam","China","Philippines"]
qbase["Which animal is considered sacred in India?"]=["Cow","Sheep","Cat","Dog"]
qbase["What are the names of Donald Duck's three nephews?"]=["Huey, Dewey, Louie","Quick, Quack, Quock","Alvin, Simon, Theodore","Robbie, Chip, Ernie"]
qbase["Which children's storybook character believes that the sky is falling?"]=["Chicken Little","Curious George","Jack Sprat","Tom Thumb"]
qbase["Which of these U.S. Presidents appeared on the television series 'Laugh-In'?"]=["Richard Nixon","Lyndon Johnson","Jimmy Carter","Gerald Ford"]
qbase["Etiquette dictates that a female subject greeting the queen should do what?"]=["Curtsy","Boo","Wink","High-Five"]
qbase["What city's airport used the code ORD?"]=["Chicago","Orlando","New York City","Portland"]
qbase["Which company makes Oreo cookies?"]=["Nabisco","General Mills","Keebler","Kraft"]
qbase["Which country is the rock group U2 from?"]=["Ireland","England","Belgium","Germany"]
qbase["What do you call three consecutive strikes in bowling?"]=["Turkey","Yahtzee","Mulligan","Ace"]
qbase["What is produced during photosynthesis?"]=["Oxygen","Hydrogen","Nitrogen","Light"]
qbase["What is the colored part of the eye called?"]=["Iris","Pupil","Retina","Cochlea"]
qbase["What is the largest animal ever to live on Earth?"]=["Blue Whale","Giant Squid","Woolly Mammoth","Tyrannosaurus Rex"]
qbase["What is the name of Mario's brother in the 'Super Mario' video games?"]=["Luigi","Louis","Wario","Waluigi"]
qbase["What is the name of the South African political party that was headed by Nelson Mandela?"]=["African National Congress","South African Democrats","Mandela Freedom Party","Inkatha National Assembly"]
qbase["What is the main ingredient in traditional cole slaw?"]=["Cabbage","Lettuce","Spinach","Chicory"]
qbase["Which letters are on the '4' button of a touch-tone telephone?"]=["GHI","JKL","DEF","MNO"]
qbase["What newspaper do Lois Lane and Clark Kent work for?"]=["The Daily Planet","The Bugle","The Metropolis Tribune","The New York Times"]
qbase["Which pro wrestler grapples with Sylvester Stallone in the movie 'Rocky III'?"]=["Hulk Hogan","Dolph Lundgren","Mr. T","Mickey Goldmill"]

trimmed=[] #list of the answer choices after 50/50 aid
answers_remaining = [] #list of the answers' indices + 1 after removal by 50/50 aid
qupotential=[] #list of all possible questions
apotential=[] #list of all possible answers
rightanswers=[] #list of right answers

for question in qbase:
    qupotential.append(question)
    apotential.append(qbase[question])
    
n=0
finalquestions=[]
finalanswers=[]
while n<15: #randomly selects 15 questions from the dict to ask player
    x=random.randint(1,len(qupotential)-1)
    finalquestions.append(qupotential.pop(x))
    finalanswers.append(apotential.pop(x))
    n+=1

for item in finalanswers:
    rightanswers.append(item[0])
    
money_counter = {0:[-320,"$0"],
                 1:[-290,"$100"],
                 2:[-260,"$200"],
                 3:[-230,"$300"],
                 4:[-200,"$500"],
                 5:[-170,"$1,000"],
                 6:[-140,"$2,000"],
                 7:[-110,"$4,000"],
                 8:[-80,"$8,000"],
                 9:[-50,"$16,000"],
                10:[-20,"$25,000"],
                11:[10,"$50,000"],
                12:[40,"$100,000"],
                13:[70,"$250,000"],
                14:[100,"$500,000"]}
#This is a dictionary with key: question index, value as a list of y coordinate of earned money and the earned money in dollar values.

i = 0 #number of questions completed
print(rightanswers)
print(titlescreen())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




