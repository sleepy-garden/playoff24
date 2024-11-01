import random
import time

#==teams==

#army, AAC
army = {"name":"Army","masc":"Black Knights",
        "conf":"AAC","seed":0,
        "stad":"Michie Stadium in West Point, NY",
        "onum":float(32.8),"dnum":float(26.3),}

#boise state, MWC
bsu = {"name":"Boise State","masc":"Broncos", 
       "conf":"MWC","seed":12,
       "stad":"Albertsons Stadium in Boise, ID",
       "onum":float(36.5),"dnum":float(22.0)}

#BYU, B12
byu = {"name":"BYU","masc":"Cougars",
       "conf":"B12","seed":11,
       "stad":"LaVell Edwards Stadium in Provo, UT",
       "onum":float(33.9),"dnum":float(28.0)}

#clemson, ACC
clem = {"name":"Clemson","masc":"Tigers",
        "conf":"ACC","seed":3,
        "stad":"Memorial Stadium in Clemson, SC",
        "onum":float(38.3),"dnum":float(30.2)}

#georgia, SEC
uga= {"name":"Georgia","masc":"Bulldogs",
      "conf":"SEC","seed":2,
      "stad":"Sanford Stadium in Athens, GA",
      "onum":float(39.7),"dnum":float(35.5)}

#iowa state, B12
isu = {"name":"Iowa State","masc":"Cyclones",
       "conf":"B12","seed":4,
       "stad":"Jack Trice Stadium in Des Moines, IA",
       "onum":float(30.1),"dnum":float(33.1)}

#indiana, B1G
ind = {"name":"Indiana","masc":"Hoosiers",
       "conf":"B1G","seed":0,
       "stad":"Indiana Memorial Stadium in Bloomington, IN",
       "onum":float(35.8),"dnum":float(32.2)}

#miami, ACC
umia = {"name":"Miami","masc":"Hurricanes",
        "conf":"ACC","seed":7,
        "stad":"Hard Rock Stadium in Miami, FL",
        "onum":float(43.8),"dnum":float(29.1)}

#notre dame, independent
nd = {"name":"Notre Dame","masc":"Fighting Irish",
      "conf":"Independent","seed":0,
      "stad":"Notre Dame Stadium in South Bend, IN",
      "onum":float(36.7),"dnum":float(37.1)}

#ohio state, B1G
tosu = {"name":"Ohio State","masc":"Buckeyes",
        "conf":"B1G","seed":5,
        "stad":"Ohio Stadium in Columbus, OH",
        "onum":float(38.7),"dnum":float(38.9)}

#oregon, B1G
uo = {"name":"Oregon","masc":"Ducks",
      "conf":"B1G","seed":1,
      "stad":"Autzen Stadium in Eugene, OR",
      "onum":float(43.2),"dnum":float(33.4)}

#penn state, B1G
psu = {"name":"Penn State","masc":"Nittany Lions",
       "conf":"B1G","seed":8,
       "stad":"Beaver Stadium in State College, PA",
       "onum":float(36.2),"dnum":float(37.7)}

#tennessee, SEC
tenn = {"name":"Tennessee","masc":"Volunteers",
        "conf":"SEC","seed":9,
        "stad":"Neyland Stadium in Knoxville, TN",
        "onum":float(33.8),"dnum":float(37.7)}

#texas, SEC
utx = {"name":"Texas","masc":"Longhorns",
       "conf":"SEC","seed":6,
       "stad":"Royal Memorial Stadium in Austin, TX",
       "onum":float(40.6),"dnum":float(38.0)}

#texas a&m, SEC
tamu = {"name":"Texas A&M","masc":"Aggies",
        "conf":"SEC","seed":10,
        "stad":"Kyle Field in College Station, TX",
        "onum":float(35.5),"dnum":float(34.1)}

#==games==

#first round games (on campus)
def fr(ht,at): 
    #lets define our varaibles

    #the good guys
    h_team = ht.get("name")
    h_masc = ht.get("masc")
    h_off = ht.get("onum")**2
    h_def = ht.get("dnum")**2
    rest = 1

    #the arena
    loc = ht.get("stad")

    #the challengers
    a_team = at.get("name")
    a_masc = at.get("masc")
    a_off = at.get("onum")**2
    a_def = at.get("dnum")**2


    #--TEST AREA--
    p_score = 0

    h_poss = 1
    a_poss = 1
    h_score = 0
    a_score = 0
    
    print(a_team + " " + a_masc + " at " + h_team + " " + h_masc + " has kicked off!")

    while h_poss != 11 and a_poss != 11:
        #define team possession range
        h_range = round(h_off + a_def,0)
        a_range = round(a_off + h_def*1.1,0)

        #define probability within each range, this determines the outcome of the possession
        h_prob = random.randint(1,h_range) 
        a_prob = random.randint(1,a_range)
        
        time.sleep(rest)
        
        if h_poss == 6: 
            print("halftime! " + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)
        elif h_poss == 3:
            print("end of first quarter! " + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)
        elif h_poss == 8:
            print("end of third quarter! " + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)

        #print('possession: %s' % h_poss)

        #defines threshold for touchdown compared to field goal
        hfg = round(a_def + (h_off/3),0)
        
        if h_prob <= round(a_def,0):
            #defense gets a stop!
            p_score = 0
            time.sleep(rest)
            print(h_team + ": turnover! no points scored")
            #print("possession probability is %s" % h_prob + " out of " + str(h_range))          
        elif round(a_def,0) < h_prob <= hfg:
            #offense is held to a field goal!
            p_score = 3
            time.sleep(rest)
            print(h_team + ": field goal! 3 points!")
            #print("possession probability is %s" % h_prob + " out of " + str(h_range))
        elif h_prob > hfg:
            #offense scores a tuddy!
            p_score = 7
            time.sleep(rest)
            print(h_team + ": TOUCHDOWN! 7 points!")
            #print("possession probability is %s" % h_prob + " out of " + str(h_range))
             
        #counter for possessions
        h_poss += 1
        #adds possession score to total score
        h_score += p_score

        #defines threshold for touchdown compared to field goal
        #defense has a slight boost to reflect a sort of "home field advantage"
        afg = round((h_def*1.1) + (a_off/3),0)

        if a_prob <= round((h_def*1.1),0):
            #defense gets a stop!
            p_score = 0
            time.sleep(rest)
            print(a_team + ": turnover! no points scored")
            #print("possession probability is %s" % a_prob + " out of " + str(a_range))
        elif round((h_def*1.1),0) < a_prob <= afg:
            #offense is held to a field goal!
            p_score = 3
            time.sleep(rest)
            print(a_team + ": field goal! 3 points!")
            #print("possession probability is %s" % a_prob + " out of " + str(a_range))
        elif a_prob > afg:
            #offense scores a tuddy!
            p_score = 7
            time.sleep(rest)
            print(a_team + ": TOUCHDOWN! 7 points!")
            #print("possession probability is %s" % a_prob + " out of " + str(a_range))
        
        a_poss += 1
        a_score += p_score

        #if h_poss <= 10:
            #c.print(h_team + ' %s' % h_score + ', ' + a_team + ' %s' % a_score)

    oth_p_score = 0
    ota_p_score = 0
    counter = 1

    if h_score == a_score:
        while h_score == a_score:
            #define team possession range
            h_range = round(h_off + a_def,0)
            a_range = round(a_off + h_def*1.1,0)

            #define probability within each range, this determines the outcome of the possession
            h_prob = random.randint(1,h_range) 
            a_prob = random.randint(1,a_range)
            
            time.sleep(rest)

            print('OVERTIME %s' % counter)

            #defines threshold for touchdown compared to field goal
            hfg = round(a_def + (h_off/3),0)
            
            if h_prob <= round(a_def,0):
                #defense gets a stop!
                oth_p_score = 0
                time.sleep(rest)
                print(h_team + ": turnover! no points scored")
                #print("possession probability is %s" % h_prob + " out of " + str(h_range))          
            elif round(a_def,0) < h_prob <= hfg:
                #offense is held to a field goal!
                oth_p_score = 3
                time.sleep(rest)
                print(h_team + ": field goal! 3 points!")
                #print("possession probability is %s" % h_prob + " out of " + str(h_range))
            elif h_prob > hfg:
                #offense scores a tuddy!
                oth_p_score = 7
                time.sleep(rest)
                print(h_team + ": TOUCHDOWN! 7 points!")
                #print("possession probability is %s" % h_prob + " out of " + str(h_range))
            
            #defines threshold for touchdown compared to field goal
            #defense has a slight boost to reflect a sort of "home field advantage"
            afg = round((h_def*1.1) + (a_off/3),0)

            if a_prob <= round((h_def*1.1),0):
                #defense gets a stop!
                ota_p_score = 0
                time.sleep(rest)
                print(a_team + ": turnover! no points scored")
                #print("possession probability is %s" % a_prob + " out of " + str(a_range))
            elif round((h_def*1.1),0) < a_prob <= afg:
                #offense is held to a field goal!
                ota_p_score = 3
                time.sleep(rest)
                print(a_team + ": field goal! 3 points!")
                #print("possession probability is %s" % a_prob + " out of " + str(a_range))
            elif a_prob > afg:
                #offense scores a tuddy!
                ota_p_score = 7
                time.sleep(rest)
                print(a_team + ": TOUCHDOWN! 7 points!")
                #print("possession probability is %s" % a_prob + " out of " + str(a_range))       

            h_score += oth_p_score
            a_score += ota_p_score
            counter += 1

            if ota_p_score > oth_p_score: 
                print(a_team + " wins against " + h_team + " " + str(a_score) + " - " + str(h_score) + " at " + loc + "\n")
                time.sleep(5)
                return at
        
            elif oth_p_score > ota_p_score:
                print(h_team + " wins against " + a_team + " " + str(h_score) + " - " + str(a_score) + " at " + loc + "\n")
                time.sleep(5)
                return ht


    if h_score > a_score:
        print(h_team + " wins against " + a_team + " " + str(h_score) + " - " + str(a_score) + " at " + loc + "\n")
        time.sleep(5)
        return ht
    elif a_score > h_score:
        print(a_team + " wins against " + h_team + " " + str(a_score) + " - " + str(h_score) + " at " + loc + "\n")
        time.sleep(5)
        return at

#non first round game
def ns(t1,t2,bowl): 
    #lets define our varaibles

    #the good guys
    team1 = t1.get("name")
    t1m = t1.get("masc")
    t1_off = t1.get("onum")**2
    t1_def = t1.get("dnum")**2
    rest = 1

    #the challengers
    team2 = t2.get("name")
    t2m = t2.get("masc")
    t2_off = t2.get("onum")**2
    t2_def = t2.get("dnum")**2


    #--TEST AREA--
    p_score = 0

    poss1 = 1
    poss2 = 1
    score1 = 0
    score2 = 0

    print(team2 + " " + t2m + " v. " + team1 + " " + t1m + " at the " + bowl + " has kicked off!")

    while poss1 != 11 and poss2 != 11:
        #define team possession range
        t1_range = round(t1_off + t2_def,0)
        t2_range = round(t2_off + t1_def,0)

        #define probability within each range, this determines the outcome of the possession
        t1_prob = random.randint(1,t1_range) 
        t2_prob = random.randint(1,t2_range)
        
        time.sleep(rest)
        
        if poss1 == 3:
            print("end of first quarter! " + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)
        if poss1 == 6: 
            print("halftime! " + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)
        if poss1 == 8:
            print("end of the third quarter! " + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)

        #print('possession: %s' % poss1)

        #defines threshold for touchdown compared to field goal
        hfg = round(t2_def + (t1_off/3),0)

        if t1_prob <= round(t2_def,0):
            #defense gets a stop!
            p_score = 0
            time.sleep(rest)
            print(team1 + ": turnover! no points scored")
            #print("possession probability is %s" % t1_prob + " out of " + str(t1_range))          
        elif round(t2_def,0) < t1_prob <= hfg:
            #offense is held to a field goal!
            p_score = 3
            time.sleep(rest)
            print(team1 + ": field goal! 3 points!")
            #print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
        elif t1_prob >= hfg:
            #offense scores a tuddy!
            p_score = 7
            time.sleep(rest)
            print(team1 + ": TOUCHDOWN! 7 points!")
            #print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
             
        #counter for possessions
        poss1 += 1
        #adds possession score to total score
        score1 += p_score

        #defines threshold for touchdown compared to field goal
        afg = round(t1_def + (t2_off/3),0)

        if t2_prob <= round(t1_def,0):
            p_score = 0
            time.sleep(rest)
            print(team2 + ": turnover! no points scored")
            #print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
        elif round(t1_def,0) < t2_prob <= afg:
            p_score = 3
            time.sleep(rest)
            print(team2 + ": field goal! 3 points!")
            #print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
        elif t2_prob >= afg:
            p_score = 7
            time.sleep(rest)
            print(team2 + ": TOUCHDOWN! 7 points!")
            #print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
        
        poss2 += 1
        score2 += p_score

        #if poss1 <= 10:
            #c.print(team1 + ' %s' % score1 + ', ' + team2 + ' %s' % score2)

    oth_p_score = 0
    ota_p_score = 0
    counter = 1

    if score1 == score2:
        while score1 == score2:
            #define team possession range
            t1_range = round(t1_off + t2_def,0)
            t2_range = round(t2_off + t1_def*1.1,0)

            #define probability within each range, this determines the outcome of the possession
            t1_prob = random.randint(1,t1_range) 
            t2_prob = random.randint(1,t2_range)
            
            time.sleep(rest)

            print('OVERTIME %s' % counter)

            #defines threshold for touchdown compared to field goal
            hfg = round(t2_def + (t1_off/3),0)
            
            if t1_prob <= round(t2_def,0):
                #defense gets a stop!
                oth_p_score = 0
                time.sleep(rest)
                print(team1 + ": turnover! no points scored")
                #print("possession probability is %s" % t1_prob + " out of " + str(t1_range))          
            elif round(t2_def,0) < t1_prob <= hfg:
                #offense is held to a field goal!
                oth_p_score = 3
                time.sleep(rest)
                print(team1 + ": field goal! 3 points!")
                #print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
            elif t1_prob > hfg:
                #offense scores a tuddy!
                oth_p_score = 7
                time.sleep(rest)
                print(team1 + ": TOUCHDOWN! 7 points!")
                #print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
            

            #defines threshold for touchdown compared to field goal
        
            afg = round(t1_def + (t2_off/3),0)

            if t2_prob <= round(t1_def,0):
                #defense gets a stop!
                ota_p_score = 0
                time.sleep(rest)
                print(team2 + ": turnover! no points scored")
                #print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
            elif round(t1_def,0) < t2_prob <= afg:
                #offense is held to a field goal!
                ota_p_score = 3
                time.sleep(rest)
                print(team2 + ": field goal! 3 points!")
                #print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
            elif t2_prob > afg:
                #offense scores a tuddy!
                ota_p_score = 7
                time.sleep(rest)
                print(team2 + ": TOUCHDOWN! 7 points!")
                #print("possession probability is %s" % t2_prob + " out of " + str(t2_range))

            score1 += oth_p_score
            score2 += ota_p_score
            counter += 1

            if score1 > score2:
                print(team1 + " wins against " + team2 + " " + str(score1) + " - " + str(score2) + " at the " + bowl + "\n")
                time.sleep(5)
                return t1
            elif score2 > score1:
                print(team2 + " wins against " + team1 + " " + str(score2) + " - " + str(score1) + " at the " + bowl + "\n")
                time.sleep(5)
                return t2


    if score1 > score2:
        print(team1 + " wins against " + team2 + " " + str(score1) + " - " + str(score2) + " at the " + bowl + "\n")
        time.sleep(5)
        return t1
        
    elif score2 > score1:
        print(team2 + " wins against " + team1 + " " + str(score2) + " - " + str(score1) + " at the " + bowl + "\n")
        time.sleep(5)
        return t2


#==returnables==

#---PLAYOFF SEEDINGS---
print("\nseeding:\n")
print("1: " + uo["name"] + " " + uo["masc"] + ", " + uo["conf"])
print("2: " + uga["name"] + " " + uga["masc"] + ", " + uga["conf"])
print("3: " + clem["name"] + " " + clem["masc"] + ", " + clem["conf"])
print("4: " + byu["name"] + " " + byu["masc"] + ", " + byu["conf"] + "\n")
print("5: " + tosu["name"] + " " + tosu["masc"] + ", " + tosu["conf"])
print("6: " + utx["name"] + " " + utx["masc"] + ", " + utx["conf"])
print("7: " + umia["name"] + " " + umia["masc"] + ", " + umia["conf"])
print("8: " + psu["name"] + " " + psu["masc"] + ", " + psu["conf"])
print("9: " + tenn["name"] + " " + tenn["masc"] + ", " + tenn["conf"])
print("10: " + tamu["name"] + " " + tamu["masc"] + ", " + tamu["conf"])
print("11: " + isu["name"] + " " + isu["masc"] + ", " + isu["conf"])
print("12: " + bsu["name"] + " " + bsu["masc"] + ", " + bsu["conf"]+ "\n")

#--PRE-QUARTERS--
#all games on campus

time.sleep(5)
print("\nPre-Quarters\n")
time.sleep(5)

#12 at 5
#Dec 20, 8:00
wof12v5 = fr(tosu,bsu)

#11 at 6
#Dec 21, 12:00
wof11v6 = fr(utx,isu)

#10 at 7
#Dec 21, 4:00
wof10v7 = fr(umia,tamu)

#9 at 8
#Dec 21, 8:00
wof9v8 = fr(psu,tenn)

#--QUARTERS--

#whichever of the four conf champs are closest to the location/tiebreaker goes to higher seed
#for example, oregon is projected to be the one seed, so theyd have first pick of arena, and would go to the rose bowl
#however, if clemson and georgia would both want to play in atlanta, uga would get priority over clemson becuase georgia is the two seed
#clemson would be stuck in nola

#winner of 12/5 plays 4
#winner of 11/6 plays 3
#winner of 10/7 plays 2
#winner of 9/8 plays 1

time.sleep(2)
print("\nQuarterfinals!\n")
time.sleep(8)

#=Fiesta Bowl=
fbt = "Fiesta Bowl in State Farm Stadium in Glendale, AZ"
#Dec 31, 7:30
fb = ns(byu,wof12v5,fbt)

#=Peach Bowl=
pbt = "Peach Bowl in Mercedes Benz Stadium in Atlanta, GA"
#Jan 1, 1:00
pb = ns(uga,wof10v7,pbt)

#=Rose Bowl=
rbt = "Rose Bowl in Rose Bowl in Los Angeles, CA"
#Jan 1, 5:00
rb = ns(uo,wof9v8,rbt)

#=Sugar Bowl=
sbt = "Sugar Bowl in Caesars Superdome in New Orleans, LA"
#Jan 1, 8:45
sb = ns(clem,wof11v6,sbt)

#--SEMIS--
time.sleep(2)
print("\nSemifinals!\n")
time.sleep(8)

#=Orange Bowl=
obt = "Orange Bowl at Hard Rock Stadium in Miami, FL"
#Rose Bowl Champ v Fiesta Bowl Champ
#Jan 9, 7:30
ob = ns(rb,fb,obt)

#=Cotton Bowl=
cbt = "Cotton Bowl at AT&T Stadium in Arlington, TX"
#Peach Bowl Champ v Sugar Bowl Champ
#Jan 10, 7:30
cb = ns(pb,sb,cbt)

#--NATIONAL CHAMPIONSHIP--

time.sleep(2)
print("\nNational Chamionship!\n")
time.sleep(8)

#=National Championship=
nct = "National Championship at Mercedes Benz Stadium in Atlanta, GA"
#Orange Bowl Champ v Cotton Bowl Champ
#Jan 20, 7:30
nc = ns(ob,cb,nct)
    
print("the 2025 National Champions are the " + nc["name"] + " " + nc["masc"] + "!")