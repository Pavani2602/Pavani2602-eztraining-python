#project-1-quiz game
q1="""what is the most famous kerala food item ?
a.Idly sambar
b.Fish
c.Erissery
d.Idiyappam """

q2="""who is best dancer in tollywood?
a.Jr ntr
b.Ramcharan
c.Allu Arjun
d.Maheshbabu"""

q3="""who sang neevunte chalu song?
a.Sid sriram
b.Devi sri prasad
c.GV prakash kumar
d.Shankar mahadevan"""

q4="""who is the famous wrestler in WWE?
a.Roman reigns
b.Hulk hogan
c.Steve austin
d.Randy orton"""

q5="""In which year,the government of india announced the demonetisation of 500&1000 notes?
a.Mar 5,2020
b.Jan 8,2019
c.Aug 20,2017
d.Nov 8,2016"""

questions={q1:"d",q2:"c",q3:"a",q4:"a",q5:"d"}
name=input("Hi what is your name")
print("Hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question?(yes/no)")
    if flag1 =="yes":
        continue
    ans=input("what is your answer")
    if ans==questions[i]:
        print("yes,your answer is correct!you got one point")
        score=score+1
        print("your score is: ",score)
    else:
        print("your answer is wrong!you lost one point")
        score=score-1
        print("your score is: ",score)
    flag2=input("Do you want to quit?(yes/no)")
    if flag2=="yes":
        break
print("your total score is",score)
    
        
        
