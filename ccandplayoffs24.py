import random
import time
from rich.console import Console
from rich.text import Text
c = Console()

#dont forget to change to python 3.9.6!

#----------rich download----------
#https://rich.readthedocs.io/en/stable/introduction.html
 

#=========teams============

#alabama, SEC
bamaT = Text("Alabama")
bamaT.stylize("rgb(158,27,50)",0,7)
bamaM = Text("Crimson Tide")
bamaM.stylize("rgb(158,27,50)",0,12)
bama = {"name":bamaT,"lname":"Alabama",
		"masc":bamaM,"lmasc":"Crimson Tide",
		"conf":"SEC","seed":0,
		"stad":"Bryant-Denny Stadium in Tuscaloosa, AL",
		"onum":float(40.5),"dnum":float(34.3)}

#arizona state, B12
asuT = Text("Arizona State")
asuM = Text("Sun Devils")
asuT.stylize("rgb(255,198,39)",0,13)#yellow(dark mode)
asuM.stylize("rgb(255,198,39)",0,10)
#asuT.stylize("rgb(140,29,64)",0,13)#maroon(light mode)
#asuM.stylize("rgb(140,29,64)",0,10)
asu = {"name":asuT,"lname":"Arizona State",
	   "masc":asuM,"lmasc":"Sun Devils",
	   "conf":"B12","seed":17,
	   "stad":"Sun Devil Stadium in Tempe, AZ",
	   "onum":float(31.5),"dnum":float(28.3)}

#army, AAC
armyT = Text("Army")
armyM = Text("Black Knights")
armyT.stylize("rgb(211,188,141)",0,4)#gold(dark mode)
armyM.stylize("rgb(211,188,141)",0,13)
#armyT.stylize("rgb(77,79,79)",0,4)#gray(light mode)
#armyM.stylize("rgb(77,79,79)",0,13)
army = {"name":armyT,"lname":"Army",
		"masc":armyM,"lmasc":"Black Knights",
		"conf":"AAC","seed":15,
		"stad":"Michie Stadium in West Point, NY",
		"onum":float(30.7),"dnum":float(27.0)}

#boise state, MWC
bsuT = Text("Boise State")
bsuM = Text("Broncos")
bsuT.stylize("rgb(0,51,160)",0,11)
bsuM.stylize("rgb(0,51,160)",0,7)
bsu = {"name":bsuT,"lname":"Boise State",
	   "masc":bsuM,"lmasc":"Broncos", 
	   "conf":"MWC","seed":10,
	   "stad":"Albertsons Stadium in Boise, ID",
	   "onum":float(37.0),"dnum":float(25.1)}


#clemson, ACC
clemT = Text("Clemson")
clemM = Text("Tigers")
clemT.stylize("rgb(254,102,0)",0,7)
clemM.stylize("rgb(254,102,0)",0,6)
clem = {"name":clemT,"lname":"Clemson",
		"masc":clemM,"lmasc":"Tigers",
		"conf":"ACC","seed":0,
		"stad":"Memorial Stadium in Clemson, SC",
		"onum":float(34.9),"dnum":float(31.5)}

#georgia, SEC
ugaT = Text("Georgia")
ugaM = Text("Bulldogs")
ugaT.stylize("rgb(186,12,47)",0,7)
ugaM.stylize("rgb(186,12,47)",0,8)
uga = {"name":ugaT,"lname":"Georgia",
	  "masc":ugaM,"lmasc":"Bulldogs",
	  "conf":"SEC","seed":0,
	  "stad":"Sanford Stadium in Athens, GA",
	  "onum":float(39.7),"dnum":float(33.3)}

#indiana, B1G
indT = Text("Indiana")
indM = Text("Hoosiers")
indT.stylize("rgb(153,0,0)",0,7)
indM.stylize("rgb(153,0,0)",0,8)
ind = {"name":indT,"lname":"Indiana",
	   "masc":indM,"lmasc":"Hoosiers",
	   "conf":"B1G","seed":7,
	   "stad":"Indiana Memorial Stadium in Bloomington, IN",
	   "onum":float(36.0),"dnum":float(34.0)}

#iowa state, B12 
isuT = Text("Iowa State")
isuM = Text("Cyclones")
isuT.stylize("rgb(200,16,46)",0,10)
isuM.stylize("rgb(200,16,46)",0,8)
isu = {"name":isuT,"lname":"Iowa State",
	   "masc":isuM,"lmasc":"Cyclones",
	   "conf":"B12","seed":17,
	   "stad":"Jack Trice Stadium Des Moines, IA",
	   "onum":float(30.3),"dnum":float(31.1)}

#miami, ACC
umiaT = Text("Miami")
umiaM = Text("Hurricanes")
umiaT.stylize("rgb(244,114,33)",0,5)
umiaM.stylize("rgb(244,114,33)",0,10)
umia = {"name":umiaT,"lname":"Miami",
		"masc":umiaM,"lmasc":"Hurricanes",
		"conf":"ACC","seed":6,
		"stad":"Hard Rock Stadium in Miami, FL",
		"onum":float(42.0),"dnum":float(27.3)}

#notre dame, independent
ndT = Text("Notre Dame")
ndM = Text("Fighting Irish")
ndT.stylize("rgb(174,145,66)",0,10)#gold(dark mode)
ndM.stylize("rgb(174,145,66)",0,14)
#ndT.stylize("rgb(12,35,64)",0,10)#navy blue(light mode)
#ndM.stylize("rgb(12,35,64)",0,14)
nd = {"name":ndT,"lname":"Notre Dame",
	  "masc":ndM,"lmasc":"Fighting Irish",
	  "conf":"Independent","seed":7,
	  "stad":"Notre Dame Stadium in South Bend, IN",
	  "onum":float(38.6),"dnum":float(36.4)}

#ohio state, B1G
osuT = Text("Ohio State")
osuM = Text("Buckeyes")
osuT.stylize("rgb(187,0,0)",0,10)
osuM.stylize("rgb(187,0,0)",0,8)
osu = {"name":osuT,"lname":"Ohio State",
	   "masc":osuM,"lmasc":"Buckeyes",
	   "conf":"B1G","seed":2,
	   "stad":"Ohio Stadium in Columbus, OH",
	   "onum":float(37.3),"dnum":float(40.8)}

#oregon, B1G
oreT = Text("Oregon")
oreM = Text("Ducks")
oreT.stylize("rgb(21,71,51)",0,6)
oreM.stylize("rgb(21,71,51)",0,5)
ore = {"name":oreT,"lname":"Oregon",
	  "masc":oreM,"lmasc":"Ducks",
	  "conf":"B1G","seed":1,
	  "stad":"Autzen Stadium in Eugene, OR",
	  "onum":float(42.8),"dnum":float(35.9)}

#penn state, B1G
psuT = Text("Penn State")
psuM = Text("Nittany Lions")
psuT.stylize("rgb(30,64,124)",0,10)
psuM.stylize("rgb(30,64,124)",0,13)
psu = {"name":psuT,"lname":"Penn State",
	   "masc":psuM,"lmasc":"Nittany Lions",
	   "conf":"B1G","seed":6,
	   "stad":"Beaver Stadium in State College, PA",
	   "onum":float(36.5),"dnum":float(38.4)}

#smu, ACC
smuT = Text("SMU")
smuM = Text("Mustangs")
smuT.stylize("rgb(53,76,161)",0,3)
smuM.stylize("rgb(53,76,161)",0,8)
smu = {"name":smuT,"lname":"SMU",
	   "masc":smuM,"lmasc":"Mustangs",
	   "conf":"ACC","seed":0,
	   "stad":"Gerald J. Ford Stadium in Dallas, TX",
	   "onum":float(38.7),"dnum":float(31.1)}

#tennessee, SEC
tennT = Text("Tennessee")
tennM = Text("Volunteers")
tennT.stylize("rgb(255,132,0)",0,9)
tennM.stylize("rgb(255,132,0)",0,10)
tenn = {"name":tennT,"lname":"Tennessee",
		"masc":tennM,"lmasc":"Volunteers",
		"conf":"SEC","seed":8,
		"stad":"Neyland Stadium in Knoxville, TN",
		"onum":float(34.8),"dnum":float(38.3)}

#texas, SEC
utxT = Text("Texas")
utxM = Text("Longhorns")
utxT.stylize("rgb(191,86,0)",0,5)
utxM.stylize("rgb(191,86,0)",0,9)
utx = {"name":utxT,"lname":"Texas",
	   "masc":utxM,"lmasc":"Longhorns",
	   "conf":"SEC","seed":2,
	   "stad":"Royal Memorial Stadium in Austin, TX",
	   "onum":float(38.2),"dnum":float(40.0)}

#tulane, AAC
tulnT = Text("Tulane")
tulnM = Text("Green Wave")
tulnT.stylize("rgb(0,103,71)",0,6)
tulnM.stylize("rgb(0,103,71)",0,10)
tuln = {"name":tulnT,"lname":"Tulane",
		"masc":tulnM,"lmasc":"Green Wave",
		"conf":"AAC","seed":0,
		"stad":"Yulman Stadium in New Orleans, LA",
		"onum":float(33.7),"dnum":float(24.2)}

#unlv, MWC
unlvT = Text("UNLV")
unlvM = Text("Rebels")
unlvT.stylize("rgb(207,10,43)",0,4)
unlvM.stylize("rgb(207,10,43)",0,6)
unlv = {"name":unlvT,"lname":"UNLV",
		"masc":unlvM,"lmasc":"Rebels",
		"conf":"MWC","seed":0,
		"stad":"Allegiant Stadium in Las Vegas, NV",
		"onum":float(34.2),"dnum":float(24.0)}

#=========game functions==========

#on campus games (first round of playoffs and non-p4 conf championships)(home team has defensive boost (a sort of home-field advantage))
def oc(ht,at): 
	#lets define our varaibles
	#the good guys
	h_team = ht.get("name")
	h_masc = ht.get("masc")
	h_off = ht.get("onum")**2
	h_def = ht.get("dnum")**2

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
	
	yards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
			 '11','12','13','14','15','16','17','18','19','20',
			 '21','22','23','24','25','26','27','28','29','30',
			 '31','32','33','34','35','36','37','38','39','40',
			 '41','42','43','44','45','46','47','48','49','50',
			 '51','52','53','54','55','56','57','58','59','60',
			 '61','62','63','64','65','66','67','68','69','70',
			 '71','72','73','74','75','76','77','78','79','80',
			 '81','82','83','84','85','86','87','88','89','90',
			 '91','92','93','94','95','96','97','98','99']

	weights = [8,8,8,8,8,8,8,8,8,8,
			   5,5,5,5,5,5,5,5,5,5,
			   4,4,4,4,4,4,4,4,4,4,
			   3,3,3,3,3,3,3,3,3,3,
			   2,2,2,2,2,2,2,2,2,2,
			   1,1,1,1,1,1,1,1,1,1,
			   1,1,1,1,1,1,1,1,1,1,
			   .5,.5,.5,.5,.5,.5,.5,.5,.5,.5,
			   .5,.5,.5,.5,.5,.5,.5,.5,.5,.5,
			   .1,.1,.1,.1,.1,.1,.1,.1,.1]

	c.print(a_team + " " + a_masc + " at " + h_team + " " + h_masc + " has kicked off!")

	while a_poss != 11 and h_poss != 11:
	    #define team possession range
		h_range = round(h_off + a_def,0)
		a_range = round(a_off + h_def*1.1,0)

		#define probability within each range, this determines the outcome of the possession
		h_prob = random.randint(1,h_range) 
		a_prob = random.randint(1,a_range)
		
		time.sleep(1)
		
		if a_poss == 6: 
			c.print(Text("halftime! ") + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)
		elif a_poss == 3:
			c.print(Text("end of first quarter! ") + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)
		elif a_poss == 8:
			c.print(Text("end of third quarter! ") + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)

		#print('possession: %s' % h_poss)

		#--gameplay--

		#defines threshold for touchdown compared to field goal
		#defense has a slight boost to reflect a sort of "home field advantage"
		afg = round((h_def*1.1) + (a_off/3),0)

		if a_prob <= round((h_def*1.1),0):
			#defense gets a stop!
			p_score = 0
			time.sleep(1)
			c.print(a_team + ": turnover!")
			#print("possession probability is %s" % a_prob + " out of " + str(a_range))
		elif round((h_def*1.1),0) < a_prob <= afg:
			#offense is held to a field goal!
			p_score = 3
			time.sleep(1)
			fgy = random.randint(19,60)
			c.print(a_team + ": " + str(fgy)  + " yard field goal!")
			#print("possession probability is %s" % a_prob + " out of " + str(a_range))
		elif a_prob > afg:
			#offense scores a tuddy!
			yardage = random.choices(yards,weights)[0]
			#this is how long the play was for the td for the return statement
			por = random.randint(1,2)
			if por == 1:
				unit = " yard pass"
			elif por == 2:
				unit = " yard run"
			#this is the "when to go for two" logic
			if (a_poss == 8 or a_poss == 9) and ((a_score + 8) == h_score or (a_score + 8) == (h_score + 7) or (a_score + 8) == (h_score - 3) or (a_score + 8) == (h_score + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					c.print(a_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					c.print(a_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
			elif a_poss == 10 and ((a_score + 8) == h_score or (a_score + 8) == (h_score + 7) or (a_score + 8) == (h_score + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					c.print(a_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					c.print(a_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
			else:
				p_score = 7
				time.sleep(1)
				c.print(a_team + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
			#print("possession probability is %s" % a_prob + " out of " + str(a_range))
 
		#counter for possessions, both for repetition and return-ables
		a_poss += 1
		#adds possession score to total score
		a_score += p_score

		#defines threshold for touchdown compared to field goal on scoring drive
		hfg = round(a_def + (h_off/3),0)
		
		if h_prob <= round(a_def,0):
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				c.print(h_team + ": takes a knee!")  
			else:
				#defense gets a stop!
				p_score = 0
				time.sleep(1)
				c.print(h_team + ": turnover!")
			#print("possession probability is %s" % h_prob + " out of " + str(h_range))          
		elif round(a_def,0) < h_prob <= hfg:
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				c.print(h_team + ": takes a knee!")  
			else:
				#this the hail mary logic
				if h_poss == 10 and (a_score - 7) <= h_score < (a_score - 4):
					hailmary = random.randint(1,2)
					if hailmary == 1:
						p_score = 0
						time.sleep(1)
						c.print(h_team + ": turnover on a hail mary!")
					elif hailmary == 2:
						#offense scores a tuddy!
						p_score = 7
						time.sleep(1)
						c.print(h_team + ": TOUCHDOWN on a hail mary!")
				#offense is held to a field goal!
				else:
					p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					c.print(h_team + ": " + str(fgy)  + " yard field goal!")
			#print("possession probability is %s" % h_prob + " out of " + str(h_range))
		elif h_prob > hfg:
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				c.print(h_team + ": takes a knee!")  
			else:
				#offense scores a tuddy!
				#this is how long the play was for the td for the return statement
				yardage = random.choices(yards,weights)[0]
				#this returns whether its a run or a pass at a 50/50 chance of each
				por = random.randint(1,2)
				if por == 1:
					unit = " yard pass"
				elif por == 2:
					unit = " yard run"
				#this is the "when to go for two" logic, twopt is whether the try is good or not
				twopt = random.randint(1,2)
				if (h_poss == 8 or h_poss == 9) and ((h_score + 8) == a_score or (h_score + 8) == (a_score + 7) or (h_score + 8) == (a_score - 3) or (h_score + 8) == (a_score + 3)):
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						c.print(h_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						c.print(h_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
				elif h_poss == 10 and (h_score + 8) == a_score:
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						c.print(h_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						c.print(h_team + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
				else:
					p_score = 7
					time.sleep(1)
					c.print(h_team + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
			#print("possession probability is %s" % h_prob + " out of " + str(h_range))
			 
		#counter for possessions, both for repetition and return-ables
		h_poss += 1
		#adds possession score to total score
		h_score += p_score

		#if h_poss <= 10:
			#c.print(h_team + ' %s' % h_score + ', ' + a_team + ' %s' % a_score)

	oth_p_score = 0
	ota_p_score = 0
	counter = 1

	time.sleep(1)
	if h_score == a_score:
		c.print(Text("end of regulation! ") + h_masc + ' %s' % h_score + ', ' + a_masc + ' %s' % a_score)
		while h_score == a_score and counter < 3:
			#define team possession range
			h_range = round(h_off + a_def,0)
			a_range = round(a_off + h_def*1.1,0)

			#define probability within each range, this determines the outcome of the possession
			h_prob = random.randint(1,h_range) 
			a_prob = random.randint(1,a_range)
			
			otyards = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

			otweights = [5,5,5,5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,2,2,2,2,3]

			time.sleep(1)

			print('OVERTIME %s' % counter)

			#defines threshold for touchdown compared to field goal
			hfg = round(a_def + (h_off/3),0)
			
			if h_prob <= round(a_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				c.print(h_team + ": turnover!")
				#print("possession probability is %s" % h_prob + " out of " + str(h_range))          
			elif round(a_def,0) < h_prob <= hfg:
				#offense is held to a field goal!
				oth_p_score = 3
				time.sleep(1)
				fgy = random.randint(19,60)
				c.print(h_team + ": " + str(fgy)  + " yard field goal!")
				#print("possession probability is %s" % h_prob + " out of " + str(h_range))
			elif h_prob > hfg:
				#offense scores a tuddy!
				oth_p_score = 7
				time.sleep(1)
				yardage = random.choices(otyards,otweights)[0]
				por = random.randint(1,2)
				if por == 1:
					unit = " yard pass"
				elif por == 2:
					unit = " yard run"
				c.print(h_team + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
				#print("possession probability is %s" % h_prob + " out of " + str(h_range))
			
			#defines threshold for touchdown compared to field goal
			#defense has a slight boost to reflect a sort of "home field advantage"
			afg = round((h_def*1.1) + (a_off/3),0)

			if a_prob <= round((h_def*1.1),0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				c.print(a_team + ": turnover!")
				#print("possession probability is %s" % a_prob + " out of " + str(a_range))
			elif round((h_def*1.1),0) < a_prob <= afg:
				#offense is held to a field goal!
				if oth_p_score == 0 or 3:
					ota_p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					c.print(a_team + ": " + str(fgy)  + " yard field goal!")
				elif oth_p_score == 7:
					hailmary = random.randint(1,2)
					if hailmary == 1:
						ota_p_score = 0
						time.sleep(1)
						c.print(a_team + ": turnover on a hail mary!")
					elif hailmary == 2:
						#offense scores a tuddy!
						ota_p_score = 7
						time.sleep(1)
						c.print(a_team + ": TOUCHDOWN on a hail mary!")
				#print("possession probability is %s" % a_prob + " out of " + str(a_range))
			elif a_prob > afg:
				#offense scores a tuddy!
				ota_p_score = 7
				time.sleep(1)
				yardage = random.choices(otyards,otweights)[0]
				por = random.randint(1,2)
				if por == 1:
					unit = " yard pass"
				elif por == 2:
					unit = " yard run"
				c.print(a_team + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
				#print("possession probability is %s" % a_prob + " out of " + str(a_range))       

			h_score += oth_p_score
			a_score += ota_p_score
			counter += 1

			if ota_p_score != oth_p_score: 
				break
		
		while h_score == a_score and counter >= 3:
			#define team possession range
			h_range = round(h_off + a_def,0)
			a_range = round(a_off + h_def*1.1,0)

			#define probability within each range, this determines the outcome of the possession
			h_prob = random.randint(1,h_range) 
			a_prob = random.randint(1,a_range)
			
			time.sleep(1)

			print('OVERTIME %s' % counter)
			
			if h_prob <= round(a_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				c.print(h_team + ": 2-PT CONVERSION FAILED!")
				#print("possession probability is %s" % h_prob + " out of " + str(h_range))          
			else:
				#offense scores a tuddy!
				oth_p_score = 2
				time.sleep(1)
				c.print(h_team + ": 2-PT CONVERSION SUCCESSFUL!")
				#print("possession probability is %s" % h_prob + " out of " + str(h_range))
			

			if a_prob <= round((h_def*1.1),0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				c.print(a_team + ": 2-PT CONVERSION FAILED!")
				#print("possession probability is %s" % a_prob + " out of " + str(a_range))
			else:
				#offense scores a tuddy!
				ota_p_score = 2
				time.sleep(1)
				c.print(a_team + ": 2-PT CONVERSION SUCCESSFUL!")
				#print("possession probability is %s" % a_prob + " out of " + str(a_range))       

			h_score += oth_p_score
			a_score += ota_p_score
			counter += 1

			if ota_p_score != oth_p_score: 
				break


	if h_score > a_score:
		time.sleep(1)
		c.print(h_team + " wins against " + a_team + " " + str(h_score) + " - " + str(a_score) + "!\n")
		time.sleep(5)
		return ht
	elif a_score > h_score:
		time.sleep(1)
		c.print(a_team + " wins against " + h_team + " " + str(a_score) + " - " + str(h_score) + "!\n")
		time.sleep(5)
		return at

#neutral site (non first round game and p4 conf championships)
def ns(t1,t2): 
	#lets define our varaibles

	#the good guys
	team1 = t1.get("name")
	t1m = t1.get("masc")
	t1_off = t1.get("onum")**2
	t1_def = t1.get("dnum")**2


	#the challengers
	team2 = t2.get("name")
	t2m = t2.get("masc")
	t2_off = t2.get("onum")**2
	t2_def = t2.get("dnum")**2

	yards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
			 '11','12','13','14','15','16','17','18','19','20',
			 '21','22','23','24','25','26','27','28','29','30',
			 '31','32','33','34','35','36','37','38','39','40',
			 '41','42','43','44','45','46','47','48','49','50',
			 '51','52','53','54','55','56','57','58','59','60',
			 '61','62','63','64','65','66','67','68','69','70',
			 '71','72','73','74','75','76','77','78','79','80',
			 '81','82','83','84','85','86','87','88','89','90',
			 '91','92','93','94','95','96','97','98','99']

	weights = [8,8,8,8,8,8,8,8,8,8,
			   5,5,5,5,5,5,5,5,5,5,
			   4,4,4,4,4,4,4,4,4,4,
			   3,3,3,3,3,3,3,3,3,3,
			   2,2,2,2,2,2,2,2,2,2,
			   1,1,1,1,1,1,1,1,1,1,
			   1,1,1,1,1,1,1,1,1,1,
			   .5,.5,.5,.5,.5,.5,.5,.5,.5,.5,
			   .5,.5,.5,.5,.5,.5,.5,.5,.5,.5,
			   .1,.1,.1,.1,.1,.1,.1,.1,.1]

	#--TEST AREA--
	p_score = 0

	poss1 = 1
	poss2 = 1
	score1 = 0
	score2 = 0

	c.print(team2 + " " + t2m + " v. " + team1 + " " + t1m + " has kicked off!")

	while poss1 != 11 and poss2 != 11:
		#define team possession range
		t1_range = round(t1_off + t2_def,0)
		t2_range = round(t2_off + t1_def,0)

		#define probability within each range, this determines the outcome of the possession
		t1_prob = random.randint(1,t1_range) 
		t2_prob = random.randint(1,t2_range)
		
		time.sleep(1)
		
		if poss1 == 3:
			c.print(Text("end of first quarter! ") + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)
		if poss1 == 6: 
			c.print(Text("halftime! ") + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)
		if poss1 == 8:
			c.print(Text("end of the third quarter! ") + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)

		#print('possession: %s' % poss1)

		#defines threshold for touchdown compared to field goal
		afg = round(t1_def + (t2_off/3),0)

		if t2_prob <= round(t1_def,0):
			p_score = 0
			time.sleep(1)
			c.print(team2 + ": turnover!")
			#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
		elif round(t1_def,0) < t2_prob <= afg:
			p_score = 3
			time.sleep(1)
			fgy = random.randint(19,55)
			c.print(team2 + ": " + str(fgy)  + " yard field goal!")
			#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
		elif t2_prob >= afg:
			#offense scores a tuddy
			yardage = random.choices(yards,weights)[0]
			por = random.randint(1,2)
			if por == 1:
				unit = " yard pass"
			elif por == 2:
				unit = " yard run"
			if poss2 >= 8 and ((score2 + 8) == score1 or (score2 + 8) == (score1 + 7) or (score2 + 8) == (score1 - 3) or (score2 + 8) == (score1 + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					c.print(team2 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					c.print(team2 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")						
				elif poss2 == 10 and ((score2 + 8) == score1 or (score2 + 8) == (score1 + 7) or (score2 + 8) == (score1 + 3)):
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						c.print(team2 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						c.print(team2 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
			else:
				p_score = 7
				time.sleep(1)
				c.print(team2 + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
			#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
		
		#counter for possessions
		poss2 += 1
		#adds possession score to total score
		score2 += p_score

		#defines threshold for touchdown compared to field goal
		hfg = round(t2_def + (t1_off/3),0)

		if t1_prob <= round(t2_def,0):
			#defense gets a stop!
			if poss1 == 10 and score1 >= (score2 + 1):
				p_score = 0
				time.sleep(1)
				c.print(team1 + ": takes a knee!")  
			else:
				p_score = 0
				time.sleep(1)
				c.print(team1 + ": turnover!")
			#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))          
		elif round(t2_def,0) < t1_prob <= hfg:
			if poss1 == 10 and score1 >= (score2 + 1):
				p_score = 0
				time.sleep(1)
				c.print(team1 + ": takes a knee!")  
			#offense is held to a field goal!
			elif poss1 == 10 and (score2 - 7) <= score1 < (score2 - 4):
				hailmary = random.randint(1,2)
				if hailmary == 1:
					p_score = 0
					time.sleep(1)
					c.print(team1 + ": turnover on a hail mary!")
				elif hailmary == 2:
					#offense scores a tuddy!
					p_score = 7
					time.sleep(1)
					c.print(team1 + ": TOUCHDOWN on a hail mary!")
			else:
				p_score = 3
				time.sleep(1)
				fgy = random.randint(19,55)
				c.print(team1 + ": " + str(fgy)  + " yard field goal!")
			#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
		elif t1_prob >= hfg:
			if poss1 == 10 and score1 >= (score2 + 1):
				p_score = 0
				time.sleep(1)
				c.print(team1 + ": takes a knee!")  
			#offense scores a tuddy!
			else:
				yardage = random.choices(yards,weights)[0]
				por = random.randint(1,2)
				if por == 1:
					unit = " yard pass"
				elif por == 2:
					unit = " yard run"
				#scoring mechanic
				twopt = random.randint(1,2)
				if poss1 >= 8 and ((score1 + 8) == score2 or (score1 + 8) == (score2 + 7) or (score1 + 8) == (score2 - 3) or (score1 + 8) == (score2 + 3)):
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						c.print(team1 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						c.print(team1 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
				elif poss2 == 10 and (score1 + 8) == score2:
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						c.print(team1 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						c.print(team1 + ": TOUCHDOWN on a " + str(yardage) + unit + "! 2-PT CONVERSION FAILS!")
				else:
					p_score = 7
					time.sleep(1)
					c.print(team1 + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
			#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
			 
		#counter for possessions
		poss1 += 1
		#adds possession score to total score
		score1 += p_score


		#if poss1 <= 10:
			#c.print(team1 + ' %s' % score1 + ', ' + team2 + ' %s' % score2)

	oth_p_score = 0
	ota_p_score = 0
	counter = 1
	time.sleep(1)
	if score1 == score2:
		c.print(Text("end of the regulation! ") + t1m + ' %s' % score1 + ', ' + t2m + ' %s' % score2)
		while score1 == score2 and counter < 3:
			#define team possession range
			t1_range = round(t1_off + t2_def,0)
			t2_range = round(t2_off + t1_def*1.1,0)

			#define probability within each range, this determines the outcome of the possession
			t1_prob = random.randint(1,t1_range) 
			t2_prob = random.randint(1,t2_range)
			
			otyards = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

			otweights = [5,5,5,5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,2,2,2,2,3]

			time.sleep(1)

			print('OVERTIME %s' % counter)

			#defines threshold for touchdown compared to field goal
			hfg = round(t2_def + (t1_off/3),0)
			
			if t1_prob <= round(t2_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				c.print(team1 + ": turnover!")
				#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))          
			elif round(t2_def,0) < t1_prob <= hfg:
				#offense is held to a field goal!
				oth_p_score = 3
				time.sleep(1)
				fgy = random.randint(19,60)
				c.print(team1 + ": " + str(fgy)  + " yard field goal!")
				#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
			elif t1_prob > hfg:
				#offense scores a tuddy!
				oth_p_score = 7
				time.sleep(1)
				yardage = random.choices(otyards,otweights)[0]
				por = random.randint(1,2)
				if por == 1:
					unit = " yard pass"
				elif por == 2:
					unit = " yard run"
				c.print(team1 + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
				#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
			

			#defines threshold for touchdown compared to field goal
			afg = round(t1_def + (t2_off/3),0)

			if t2_prob <= round(t1_def,0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				c.print(team2 + ": turnover!")
				#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
			elif round(t1_def,0) < t2_prob <= afg:
				#if team1 is held to a FG or a stop, scoring a FG to tie or win would be reasonable but if youre down a TD, it would be surrender.
				#team2 held team1 to a not TD. 
				if oth_p_score == 0 or 3:
					ota_p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					c.print(team2 + ": " + str(fgy)  + " yard field goal!")
				#if team1 scores a TD and team2 is held to a would-be FG, team2 will throw a 50-50 ball to the endzone
				elif oth_p_score == 7:
					hailmary = random.randint(1,2)
					if hailmary == 1:
						ota_p_score = 0
						time.sleep(1)
						c.print(team2 + ": turnover on a hail mary!")
					elif hailmary == 2:
						ota_p_score = 7
						time.sleep(1)
						c.print(team2 + ": TOUCHDOWN on a hail mary!")
			elif t2_prob > afg:
				#offense scores a tuddy!
				ota_p_score = 7
				time.sleep(1)
				yardage = random.choices(otyards,otweights)[0]
				por = random.randint(1,2)
				if por == 1:
					unit = " yard pass"
				elif por == 2:
					unit = " yard run"
				c.print(team2 + ": TOUCHDOWN on a " + str(yardage) + unit + "!")
				#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))

			score1 += oth_p_score
			score2 += ota_p_score
			counter += 1

			if score1 != score2:
				break
		
		while score1 == score2 and counter >= 3:
			#define team possession range
			t1_range = round(t1_off + t2_def,0)
			t2_range = round(t2_off + t1_def*1.1,0)

			#define probability within each range, this determines the outcome of the possession
			t1_prob = random.randint(1,t1_range) 
			t2_prob = random.randint(1,t2_range)
			
			time.sleep(1)

			print('OVERTIME %s' % counter)

			if t1_prob <= round(t2_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				c.print(team1 + ": 2-PT CONVERSION FAILED!")
				#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))          
			else:
				#offense scores a tuddy!
				oth_p_score = 2
				time.sleep(1)
				c.print(team1 + ": 2-PT CONVERSION SUCCESSFUL!")
				#print("possession probability is %s" % t1_prob + " out of " + str(t1_range))
			

			if t2_prob <= round(t1_def,0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				c.print(team2 + ": 2-PT CONVERSION FAILED!")
				#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))
			else:
				#offense scores a tuddy!
				ota_p_score = 2
				time.sleep(1)
				c.print(team2 + ": 2-PT CONVERSION SUCCESSFUL!")
				#print("possession probability is %s" % t2_prob + " out of " + str(t2_range))

			score1 += oth_p_score
			score2 += ota_p_score
			counter += 1

			if score1 != score2:
				break
		

	if score1 > score2:
		time.sleep(1)
		c.print(team1 + " wins against " + team2 + " " + str(score1) + " - " + str(score2) + "!\n")
		time.sleep(5)
		return t1
		
	elif score2 > score1:
		time.sleep(1)
		c.print(team2 + " wins against " + team1 + " " + str(score2) + " - " + str(score1) + "!\n")
		time.sleep(5)
		return t2

def seed(team):
	print(team["lname"] + " " + team["lmasc"] + ", " + team["conf"])

#==========returnables============
print("\nConference Championships!\n")

print("Dec 6, 8:00p \nMountain West Championship at %s" % bsu["stad"])
time.sleep(2)
mwccg = oc(bsu,unlv)

print("Dec 6, 8:00p \nAAC Championship at %s" % army["stad"])
time.sleep(1)
aaccg = oc(army,tuln)

print("Dec 7, 12:00p \nBig 12 Championship at AT&T Stadium in Arlington, TX")
time.sleep(1)
b12cg = ns(asu,isu)

print("Dec 7, 4:00p \nSEC Championship at Mercedes Benz Stadium in Atlanta, GA")
time.sleep(1)
seccg = ns(utx,uga)
#both teams are gonna make the cfp so the conf title just a question of seeding
if seccg == utx:
	seccgL = uga
elif seccg == uga:
	seccgL = utx

print("Dec 7, 8:00p \nACC Championship at Bank of America Stadium in Charlotte, NC")
time.sleep(1)
acccg = ns(smu,clem)
#smu has clinched a playoff birth but clemson must win to get in
#not all scenarios will have accL in the playoffs
if acccg == smu:
	accL = clem
elif acccg == clem:
	accL = smu

print("Dec 7, 8:00p \nB1G Championship at Lucas Oil Stadium in Indianapolis, IN")
time.sleep(1)
b1gcg = ns(ore,psu)
if b1gcg == ore:
	b1gL = psu
elif b1gcg == psu:
	b1gL = ore

#ranking top seed
if b1gcg == ore:
	firstchamp = ore
	secondchamp = seccg
elif b1gcg == psu and seccg == utx:
	firstchamp = utx
	secondchamp = psu
elif b1gcg == psu and seccg == uga:
	firstchamp = psu
	secondchamp = uga

#assuming smu wins, they will earn the third bye and boise state is stuck with the 4th seed unless clemson tops the mustangs
#boise state is higher ranked than both asu and isu, so, if they win, they will maintian the bye regardless of that outcome 
#rankings sit at smu(9), bsu(10), asu(12), isu(15), clem(19), unlv(20)
#so if bsu are upset by unlv, either isu or asu would take that spot from the mwc champ (both mwc teams are better than both aac teams)
if mwccg == bsu and acccg == smu:
	thirdchamp = acccg
	fourthchamp = mwccg
	fifthchamp = b12cg
elif mwccg == bsu and acccg == clem:
	thirdchamp = mwccg
	fourthchamp = b12cg
	fifthchamp = acccg
elif mwccg == unlv and acccg == smu:
	thirdchamp = acccg
	fourthchamp = b12cg
	fifthchamp = mwccg
elif mwccg == unlv and acccg == clem:
	thirdchamp = b12cg
	fourthchamp = acccg
	fifthchamp = mwccg


#if texas loses the sec champ game, they should still be above nd but the heirarchy is strictly ore > utx > psu > nd > uga
if seccgL == utx and b1gL == psu:
	s5 = utx
	s6 = psu
	s7 = nd
elif seccgL == uga and b1gL == psu:
	s5 = psu
	s6 = nd
	s7 = uga
elif seccgL == utx and b1gL == ore:
	s5 = ore
	s6 = utx
	s7 = nd
elif seccgL == uga and b1gL == ore:
	s5 = ore
	s6 = nd
	s7 = uga

#as previously stated, smu is a lock for the playoff even if they lose to clemson
if accL == smu:
	s10 = smu
	s11 = ind
else:
	s10 = ind
	s11 = bama

c.print(mwccg["name"] + ", " + aaccg["name"] + ", " + b12cg["name"] + ", " + seccg["name"] + ", " + acccg["name"] + ", and " + b1gcg["name"]  + " are the 2024 confernce champions")

time.sleep(1)

# 1: ore, 2: utx, 3: psu, 4: nd, 5: , 6: , 7: , 8: , 9: , 10: , 11: , 12: , 13: ... 16: , 17. , 18.  is the base rankings
s = {"1":firstchamp,
	 "2":secondchamp,
	 "3":thirdchamp,
	 "4":fourthchamp,

	 "5":s5,
	 "6":s6,
	 "7":s7,
	 "8":osu,
	 "9":tenn,
	 "10":s10,
	 "11":s11,
	 "12":fifthchamp}

time.sleep(3)

#---PLAYOFF SEEDINGS---
print("\nPlayoff Seeding:\n")
print("Byes")
seed(s["1"])
seed(s["2"])
seed(s["3"])
seed(s["4"])
print(" ")
print("At-large Bids")
seed(s["5"])
seed(s["6"])
seed(s["7"])
seed(s["8"])
seed(s["9"])
seed(s["10"])
seed(s["11"])
seed(s["12"])


#--PRE-QUARTERS--
#all games on campus

time.sleep(2)
print("\n\nPre-Quarters\n")
time.sleep(5)

#12 at 5
print("Dec 20, 8:00p \n" + s["5"]["stad"])
wof12v5 = oc(s["5"],s["12"])

#11 at 6
print("\nDec 21, 12:00p \n" + s["6"]["stad"])
wof11v6 = oc(s["6"],s["11"])

#10 at 7
print("\nDec 21, 4:00p \n" + s["7"]["stad"])
wof10v7 = oc(s["7"],s["10"])

#9 at 8
print("\nDec 21, 8:00p \n" + s["8"]["stad"])
wof9v8 = oc(s["8"],s["9"])


#--QUARTERS--

#whichever of the four conf champs are closest to the location/tiebreaker goes to higher seed
#for example, oregon is projected to be the one seed, so theyd have first pick of arena, and would go to the rose bowl
#however, if miami and georgia would both want to play in atlanta, uga would get priority over umia becuase georgia is the two seed
#miami would be stuck in nola

#winner of 12/5 plays 4
#winner of 11/6 plays 3
#winner of 10/7 plays 2
#winner of 9/8 plays 1

time.sleep(2)
print("\nQuarterfinals!\n")
time.sleep(8)

#=Fiesta Bowl=
print("Dec 31, 7:30p \nthe Fiesta Bowl in State Farm Stadium in Glendale, AZ")
fb = ns(s["4"],wof12v5)

#=Peach Bowl=
print("Jan 1, 1:00p \nthe Peach Bowl in Mercedes Benz Stadium in Atlanta, GA")
pb = ns(s["3"],wof11v6)

#=Rose Bowl=
print("Jan 1, 5:00p \nthe Rose Bowl in Rose Bowl in Los Angeles, CA")
rb = ns(s["1"],wof9v8)

#=Sugar Bowl=
print("Jan 1, 8:45p \nthe Sugar Bowl in Caesars Superdome in New Orleans, LA")
sb = ns(s["2"],wof10v7)


#--SEMIS--

time.sleep(2)
print("\nSemifinals!\n")
time.sleep(8)

#=Orange Bowl=
#Rose Bowl Champ v Fiesta Bowl Champ
print("Jan 9, 7:30 \nOrange Bowl at Hard Rock Stadium in Miami, FL")
ob = ns(rb,fb)

#=Cotton Bowl=
#Peach Bowl Champ v Sugar Bowl Champ
print("Jan 10, 7:30p \nCotton Bowl at AT&T Stadium in Arlington, TX")
cb = ns(pb,sb)


#--NATIONAL CHAMPIONSHIP--

time.sleep(2)
print("\nNational Championship!\n")
time.sleep(8)

#=National Championship=
#Orange Bowl Champ v Cotton Bowl Champ
print("Jan 20, 7:30p \nNational Championship at Mercedes Benz Stadium in Atlanta, GA")
nc = ns(ob,cb)

if nc == ore:
	print("SCOOOOOOOOOOOOOO! PARTY ON AGATE!")

c.print(Text("the 2025 National Champions are the ") + nc["name"] + " " + nc["masc"] + "!")