import random
import time

#=========teams============

#arizona state, B12
asu = {"name":"Arizona State","masc":"Sun Devils",
	   "conf":"B12","seed":17,
	   "stad":"Sun Devil Stadium in Tempe, AZ",
	   "onum":float(31.5),"dnum":float(28.3)}

#army, AAC
army = {"name":"Army","masc":"Black Knights",
		"conf":"AAC","seed":15,
		"stad":"Michie Stadium in West Point, NY",
		"onum":float(30.7),"dnum":float(27.0)}

#boise state, MWC
bsu = {"name":"Boise State","masc":"Broncos", 
	   "conf":"MWC","seed":10,
	   "stad":"Albertsons Stadium in Boise, ID",
	   "onum":float(37.0),"dnum":float(25.1)}

#clemson, ACC
clem = {"name":"Clemson","masc":"Tigers",
		"conf":"ACC","seed":0,
		"stad":"Memorial Stadium in Clemson, SC",
		"onum":float(34.9),"dnum":float(31.5)}

#georgia, SEC
uga = {"name":"Georgia","masc":"Bulldogs",
	  "conf":"SEC","seed":0,
	  "stad":"Sanford Stadium in Athens, GA",
	  "onum":float(39.7),"dnum":float(33.3)}

#indiana, B1G
ind = {"name":"Indiana","masc":"Hoosiers",
	   "conf":"B1G","seed":7,
	   "stad":"Indiana Memorial Stadium in Bloomington, IN",
	   "onum":float(36.0),"dnum":float(34.0)}

#iowa state, B12 
isu = {"name":"Iowa State","masc":"Cyclones",
	   "conf":"B12","seed":17,
	   "stad":"Jack Trice Stadium Des Moines, IA",
	   "onum":float(30.3),"dnum":float(31.1)}

#miami, ACC
umia = {"name":"Miami","masc":"Hurricanes",
		"conf":"ACC","seed":6,
		"stad":"Hard Rock Stadium in Miami, FL",
		"onum":float(42.0),"dnum":float(27.3)}

#notre dame, independent
nd = {"name":"Notre Dame","masc":"Fighting Irish",
	  "conf":"Independent","seed":7,
	  "stad":"Notre Dame Stadium in South Bend, IN",
	  "onum":float(38.6),"dnum":float(36.4)}

#ohio state, B1G
osu = {"name":"Ohio State","masc":"Buckeyes",
	   "conf":"B1G","seed":2,
	   "stad":"Ohio Stadium in Columbus, OH",
	   "onum":float(37.3),"dnum":float(40.8)}

#oregon, B1G
ore = {"name":"Oregon","masc":"Ducks",
	  "conf":"B1G","seed":1,
	  "stad":"Autzen Stadium in Eugene, OR",
	  "onum":float(42.8),"dnum":float(35.9)}

#penn state, B1G
psu = {"name":"Penn State","masc":"Nittany Lions",
	   "conf":"B1G","seed":6,
	   "stad":"Beaver Stadium in State College, PA",
	   "onum":float(36.5),"dnum":float(38.4)}

#smu, ACC
smu = {"name":"SMU","masc":"Mustangs",
	   "conf":"ACC","seed":0,
	   "stad":"Gerald J. Ford Stadium in Dallas, TX",
	   "onum":float(38.7),"dnum":float(31.1)}

#tennessee, SEC
tenn = {"name":"Tennessee","masc":"Volunteers",
		"conf":"SEC","seed":8,
		"stad":"Neyland Stadium in Knoxville, TN",
		"onum":float(34.8),"dnum":float(38.3)}

#texas, SEC
utx = {"name":"Texas","masc":"Longhorns",
	   "conf":"SEC","seed":2,
	   "stad":"Royal Memorial Stadium in Austin, TX",
	   "onum":float(38.2),"dnum":float(40.0)}

#tulane, AAC
tuln = {"name":"Tulane","masc":"Green Wave",
		"conf":"AAC","seed":0,
		"stad":"Yulman Stadium in New Orleans, LA",
		"onum":float(33.7),"dnum":float(24.2)}

#unlv, MWC
unlv = {"name":"UNLV","masc":"Rebels",
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

	print(f"{a_team} {a_masc} at {h_team} {h_masc} has kicked off!")

	while a_poss != 11 and h_poss != 11:
	    #define team possession range
		h_range = round(h_off + a_def,0)
		a_range = round(a_off + h_def*1.1,0)

		#define probability within each range, this determines the outcome of the possession
		h_prob = random.randint(1,h_range) 
		a_prob = random.randint(1,a_range)
		
		time.sleep(1)
		
		if a_poss == 6: 
			print(f"halftime! {h_masc} {h_score}, {a_masc} {a_score}")
		elif a_poss == 3:
			print(f"end of the first quarter! {h_masc} {h_score}, {a_masc} {a_score}")
		elif a_poss == 8:
			print(f"end of the third quarter! {h_masc} {h_score}, {a_masc} {a_score}")

		#--gameplay--

		#defines threshold for touchdown compared to field goal
		#defense has a slight boost to reflect a sort of "home field advantage"
		afg = round((h_def*1.1) + (a_off/3),0)

		if a_prob <= round((h_def*1.1),0):
			#defense gets a stop!
			p_score = 0
			time.sleep(1)
			print(f"{a_team}: turnover!")
		elif round((h_def*1.1),0) < a_prob <= afg:
			#offense is held to a field goal!
			p_score = 3
			time.sleep(1)
			fgy = random.randint(19,60)
			print(f"{a_team}: {fgy} yard field goal!")
		elif a_prob > afg:
			#offense scores a tuddy!
			yardage = random.choices(yards,weights)[0]
			#this is how long the play was for the td for the return statement
			por = random.randint(1,2)
			if por == 1:
				unit = "yard pass"
			elif por == 2:
				unit = "yard run"
			#this is the "when to go for two" logic
			if (a_poss == 8 or a_poss == 9) and ((a_score + 8) == h_score or (a_score + 8) == (h_score + 7) or (a_score + 8) == (h_score - 3) or (a_score + 8) == (h_score + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
			elif a_poss == 10 and ((a_score + 8) == h_score or (a_score + 8) == (h_score + 7) or (a_score + 8) == (h_score + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
			else:
				p_score = 7
				time.sleep(1)
				print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}!")
 
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
				print(f"{h_team}: takes a knee!")  
			else:
				#defense gets a stop!
				p_score = 0
				time.sleep(1)
				print(f"{h_team}: turnover!")        
		elif round(a_def,0) < h_prob <= hfg:
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				print(f"{h_team}: takes a knee!")  
			else:
				#this the hail mary logic
				if h_poss == 10 and (a_score - 7) <= h_score < (a_score - 4):
					hailmary = random.randint(1,2)
					if hailmary == 1:
						p_score = 0
						time.sleep(1)
						print(f"{h_team}: turnover on a hail mary!")
					elif hailmary == 2:
						#offense scores a tuddy!
						p_score = 7
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a hail mary!")
				#offense is held to a field goal!
				else:
					p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					print(f"{h_team}: {fgy} yard field goal!")
		elif h_prob > hfg:
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				print(f"{h_team}: takes a knee!")  
			else:
				#offense scores a tuddy!
				#this is how long the play was for the td for the return statement
				yardage = random.choices(yards,weights)[0]
				#this returns whether its a run or a pass at a 50/50 chance of each
				por = random.randint(1,2)
				if por == 1:
					unit = "yard pass"
				elif por == 2:
					unit = "yard run"
				#this is the "when to go for two" logic, twopt is whether the try is good or not
				twopt = random.randint(1,2)
				if (h_poss == 8 or h_poss == 9) and ((h_score + 8) == a_score or (h_score + 8) == (a_score + 7) or (h_score + 8) == (a_score - 3) or (h_score + 8) == (a_score + 3)):
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
				elif h_poss == 10 and (h_score + 8) == a_score:
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
				else:
					p_score = 7
					time.sleep(1)
					print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}!")

			 
		#counter for possessions, both for repetition and return-ables
		h_poss += 1
		#adds possession score to total score
		h_score += p_score

	oth_p_score = 0
	ota_p_score = 0
	counter = 1

	time.sleep(1)
	if h_score == a_score:
		print(f"end of regulation! {h_masc} {h_score}, {a_masc} {a_score}")
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

			print(f"OVERTIME {counter}")

			#defines threshold for touchdown compared to field goal
			hfg = round(a_def + (h_off/3),0)
			
			if h_prob <= round(a_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				print(f"{h_team}: turnover!")
        
			elif round(a_def,0) < h_prob <= hfg:
				#offense is held to a field goal!
				oth_p_score = 3
				time.sleep(1)
				fgy = random.randint(19,60)
				print(f"{h_team}: {fgy} yard field goal!")

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
				print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}!")
			
			#defines threshold for touchdown compared to field goal
			#defense has a slight boost to reflect a sort of "home field advantage"
			afg = round((h_def*1.1) + (a_off/3),0)

			if a_prob <= round((h_def*1.1),0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				print(f"{a_team}: turnover!")
			elif round((h_def*1.1),0) < a_prob <= afg:
				#offense is held to a field goal!
				if oth_p_score == 0 or 3:
					ota_p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					print(f"{a_team}: {fgy} yard field goal!")
				elif oth_p_score == 7:
					hailmary = random.randint(1,2)
					if hailmary == 1:
						ota_p_score = 0
						time.sleep(1)
						print(f"{a_team}: turnover on a hail mary!")
					elif hailmary == 2:
						#offense scores a tuddy!
						ota_p_score = 7
						time.sleep(1)
						print(f"{a_team}: TOUCHDOWN on a hail mary!")
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
				print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}!")    

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

			print(f"OVERTIME {counter}")
			
			if h_prob <= round(a_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				print(f"{h_team}: 2-PT CONVERSION FAILED!")        
			else:
				#offense scores a tuddy!
				oth_p_score = 2
				time.sleep(1)
				print(f"{h_team}: 2-PT CONVERSION SUCCESSFUL!")
			

			if a_prob <= round((h_def*1.1),0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				print(f"{a_team}: 2-PT CONVERSION FAILED!")
			else:
				#offense scores a tuddy!
				ota_p_score = 2
				time.sleep(1)
				print(f"{a_team}: 2-PT CONVERSION SUCCESSFUL!")     

			h_score += oth_p_score
			a_score += ota_p_score
			counter += 1

			if ota_p_score != oth_p_score: 
				break


	if h_score > a_score:
		time.sleep(1)
		print(f"{h_team} wins against {a_team} {h_score} - {a_score}!\n")
		time.sleep(5)
		return ht
	elif a_score > h_score:
		time.sleep(1)
		print(f"{a_team} wins against {h_team} {a_score} - {h_score}!\n")
		time.sleep(5)
		return at

#===============================================================================
#neutral site (non first round game and p4 conf championships) 
#===============================================================================
def ns(ht,at): 
	#lets define our varaibles

	#the good guys (h is used for simplicity between the neutral site and on campus games)
	h_team = ht.get("name")
	h_masc = ht.get("masc")
	h_off = ht.get("onum")**2
	h_def = ht.get("dnum")**2


	#the challengers (a is also used for the same reasons)
	a_team = at.get("name")
	a_masc = at.get("masc")
	a_off = at.get("onum")**2
	a_def = at.get("dnum")**2

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

	h_poss = 1
	a_poss = 1
	h_score = 0
	a_score = 0

	print(f"{a_team} {a_masc} v. {h_team} {h_masc} has kicked off!")

	while a_poss != 11 and h_poss != 11:
	    #define team possession range
		h_range = round(h_off + a_def,0)
		a_range = round(a_off + h_def,0)

		#define probability within each range, this determines the outcome of the possession
		h_prob = random.randint(1,h_range) 
		a_prob = random.randint(1,a_range)
		
		time.sleep(1)
		
		if a_poss == 6: 
			print(f"halftime! {h_masc} {h_score}, {a_masc} {a_score}")
		elif a_poss == 3:
			print(f"end of the first quarter! {h_masc} {h_score}, {a_masc} {a_score}")
		elif a_poss == 8:
			print(f"end of the third quarter! {h_masc} {h_score}, {a_masc} {a_score}")

		#--gameplay--

		#defines threshold for touchdown compared to field goal
		#defense has a slight boost to reflect a sort of "home field advantage"
		afg = round((h_def) + (a_off/3),0)

		if a_prob <= round((h_def),0):
			#defense gets a stop!
			p_score = 0
			time.sleep(1)
			print(f"{a_team}: turnover!")
		elif round((h_def),0) < a_prob <= afg:
			#offense is held to a field goal!
			p_score = 3
			time.sleep(1)
			fgy = random.randint(19,60)
			print(f"{a_team}: {fgy} yard field goal!")
		elif a_prob > afg:
			#offense scores a tuddy!
			yardage = random.choices(yards,weights)[0]
			#this is how long the play was for the td for the return statement
			por = random.randint(1,2)
			if por == 1:
				unit = "yard pass"
			elif por == 2:
				unit = "yard run"
			#this is the "when to go for two" logic
			if (a_poss == 8 or a_poss == 9) and ((a_score + 8) == h_score or (a_score + 8) == (h_score + 7) or (a_score + 8) == (h_score - 3) or (a_score + 8) == (h_score + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
			elif a_poss == 10 and ((a_score + 8) == h_score or (a_score + 8) == (h_score + 7) or (a_score + 8) == (h_score + 3)):
				twopt = random.randint(1,2)
				if twopt == 1:
					p_score = 8
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
				elif twopt == 2:
					p_score = 6
					time.sleep(1)
					print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
			else:
				p_score = 7
				time.sleep(1)
				print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}!")
 
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
				print(f"{h_team}: takes a knee!")  
			else:
				#defense gets a stop!
				p_score = 0
				time.sleep(1)
				print(f"{h_team}: turnover!")        
		elif round(a_def,0) < h_prob <= hfg:
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				print(f"{h_team}: takes a knee!")  
			else:
				#this the hail mary logic
				if h_poss == 10 and (a_score - 7) <= h_score < (a_score - 4):
					hailmary = random.randint(1,2)
					if hailmary == 1:
						p_score = 0
						time.sleep(1)
						print(f"{h_team}: turnover on a hail mary!")
					elif hailmary == 2:
						#offense scores a tuddy!
						p_score = 7
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a hail mary!")
				#offense is held to a field goal!
				else:
					p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					print(f"{h_team}: {fgy} yard field goal!")
		elif h_prob > hfg:
			if h_poss == 10 and h_score >= (a_score + 1):
				p_score = 0
				time.sleep(1)
				print(f"{h_team}: takes a knee!")  
			else:
				#offense scores a tuddy!
				#this is how long the play was for the td for the return statement
				yardage = random.choices(yards,weights)[0]
				#this returns whether its a run or a pass at a 50/50 chance of each
				por = random.randint(1,2)
				if por == 1:
					unit = "yard pass"
				elif por == 2:
					unit = "yard run"
				#this is the "when to go for two" logic, twopt is whether the try is good or not
				twopt = random.randint(1,2)
				if (h_poss == 8 or h_poss == 9) and ((h_score + 8) == a_score or (h_score + 8) == (a_score + 7) or (h_score + 8) == (a_score - 3) or (h_score + 8) == (a_score + 3)):
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
				elif h_poss == 10 and (h_score + 8) == a_score:
					if twopt == 1:
						p_score = 8
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION SUCCESSFUL!")
					elif twopt == 2:
						p_score = 6
						time.sleep(1)
						print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}! 2-PT CONVERSION FAILS!")
				else:
					p_score = 7
					time.sleep(1)
					print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}!")

			 
		#counter for possessions, both for repetition and return-ables
		h_poss += 1
		#adds possession score to total score
		h_score += p_score

	oth_p_score = 0
	ota_p_score = 0
	counter = 1

	time.sleep(1)
	if h_score == a_score:
		print(f"end of regulation! {h_masc} {h_score}, {a_masc} {a_score}")
		while h_score == a_score and counter < 3:
			#define team possession range
			h_range = round(h_off + a_def,0)
			a_range = round(a_off + h_def,0)

			#define probability within each range, this determines the outcome of the possession
			h_prob = random.randint(1,h_range) 
			a_prob = random.randint(1,a_range)
			
			otyards = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

			otweights = [5,5,5,5,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,2,2,2,2,3]

			time.sleep(1)

			print(f"OVERTIME {counter}")

			#defines threshold for touchdown compared to field goal
			hfg = round(a_def + (h_off/3),0)
			
			if h_prob <= round(a_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				print(f"{h_team}: turnover!")
        
			elif round(a_def,0) < h_prob <= hfg:
				#offense is held to a field goal!
				oth_p_score = 3
				time.sleep(1)
				fgy = random.randint(19,60)
				print(f"{h_team}: {fgy} yard field goal!")

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
				print(f"{h_team}: TOUCHDOWN on a {yardage} {unit}!")
			
			#defines threshold for touchdown compared to field goal
			#defense has a slight boost to reflect a sort of "home field advantage"
			afg = round((h_def) + (a_off/3),0)

			if a_prob <= round((h_def),0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				print(f"{a_team}: turnover!")
			elif round((h_def),0) < a_prob <= afg:
				#offense is held to a field goal!
				if oth_p_score == 0 or 3:
					ota_p_score = 3
					time.sleep(1)
					fgy = random.randint(19,60)
					print(f"{a_team}: {fgy} yard field goal!")
				elif oth_p_score == 7:
					hailmary = random.randint(1,2)
					if hailmary == 1:
						ota_p_score = 0
						time.sleep(1)
						print(f"{a_team}: turnover on a hail mary!")
					elif hailmary == 2:
						#offense scores a tuddy!
						ota_p_score = 7
						time.sleep(1)
						print(f"{a_team}: TOUCHDOWN on a hail mary!")
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
				print(f"{a_team}: TOUCHDOWN on a {yardage} {unit}!")    

			h_score += oth_p_score
			a_score += ota_p_score
			counter += 1

			if ota_p_score != oth_p_score: 
				break
		
		while h_score == a_score and counter >= 3:
			#define team possession range
			h_range = round(h_off + a_def,0)
			a_range = round(a_off + h_def,0)

			#define probability within each range, this determines the outcome of the possession
			h_prob = random.randint(1,h_range) 
			a_prob = random.randint(1,a_range)
			
			time.sleep(1)

			print(f"OVERTIME {counter}")
			
			if h_prob <= round(a_def,0):
				#defense gets a stop!
				oth_p_score = 0
				time.sleep(1)
				print(f"{h_team}: 2-PT CONVERSION FAILED!")        
			else:
				#offense scores a tuddy!
				oth_p_score = 2
				time.sleep(1)
				print(f"{h_team}: 2-PT CONVERSION SUCCESSFUL!")
			

			if a_prob <= round((h_def),0):
				#defense gets a stop!
				ota_p_score = 0
				time.sleep(1)
				print(f"{a_team}: 2-PT CONVERSION FAILED!")
			else:
				#offense scores a tuddy!
				ota_p_score = 2
				time.sleep(1)
				print(f"{a_team}: 2-PT CONVERSION SUCCESSFUL!")     

			h_score += oth_p_score
			a_score += ota_p_score
			counter += 1

			if ota_p_score != oth_p_score: 
				break


	if h_score > a_score:
		time.sleep(1)
		print(f"{h_team} wins against {a_team} {h_score} - {a_score}!\n")
		time.sleep(5)
		return ht
	elif a_score > h_score:
		time.sleep(1)
		print(f"{a_team} wins against {h_team} {a_score} - {h_score}!\n")
		time.sleep(5)
		return at

def seed(team):
	print(team["name"] + " " + team["masc"] + ", " + team["conf"])

#==========returnables============
print("\nConference Championships!\n")

print(f'Dec 6, 8:00p \nMountain West Championship at {bsu["stad"]}')
time.sleep(2)
mwc = oc(bsu,unlv)

print(f'Dec 6, 8:00p \nAAC Championship at {army["stad"]}')
time.sleep(1)
aac = oc(army,tuln)

print("Dec 7, 12:00p \nBig 12 Championship at AT&T Stadium in Arlington, TX")
time.sleep(1)
b12 = ns(asu,isu)

print("Dec 7, 4:00p \nSEC Championship at Mercedes Benz Stadium in Atlanta, GA")
time.sleep(1)
sec = ns(utx,uga)
#both teams are gonna make the cfp so the conf title just a question of seeding
if sec == utx:
	secL = uga
elif sec == uga:
	secL = utx

print("Dec 7, 8:00p \nACC Championship at Bank of America Stadium in Charlotte, NC")
time.sleep(1)
acc = ns(smu,clem)
#smu has clinched a playoff birth but clemson must win to get in
#not all scenarios will have accL in the playoffs
if acc == smu:
	accL = clem
elif acc == clem:
	accL = smu

print("Dec 7, 8:00p \nB1G Championship at Lucas Oil Stadium in Indianapolis, IN")
time.sleep(1)
b1g = ns(ore,psu)
if b1g == ore:
	b1gL = psu
elif b1g == psu:
	b1gL = ore

#ranking top seed
if b1g == ore:
	firstchamp = ore
	secondchamp = sec
elif b1g == psu and sec == utx:
	firstchamp = utx
	secondchamp = psu
elif b1g == psu and sec == uga:
	firstchamp = psu
	secondchamp = uga

#assuming smu wins, they will earn the third bye and boise state is stuck with the 4th seed
#boise state is higher ranked than both asu and isu
#so, if they win, they will maintian the bye regardless of that outcome 

#rankings sit at smu(9), bsu(10), asu(12), isu(15), clem(19), unlv(20)

#at one point, both tulane and army were in contention for the G5 spot, but they have both fallen out of the top 25
#the aac champ game is irrelevant to the overall sim but i kept it in the code for the sake of completion

#so if bsu are upset by unlv, either isu or asu would take that bye from the bsu
#but since both mwc teams are better than both aac teams, the mwc champ will maintain the auto G5 spot in the playoff

if mwc == bsu and acc == smu:
	thirdchamp = acc
	fourthchamp = mwc
	fifthchamp = b12
elif mwc == bsu and acc == clem:
	thirdchamp = mwc
	fourthchamp = b12
	fifthchamp = acc
elif mwc == unlv and acc == smu:
	thirdchamp = acc
	fourthchamp = b12
	fifthchamp = mwc
elif mwc == unlv and acc == clem:
	thirdchamp = b12
	fourthchamp = acc
	fifthchamp = mwc


#if texas loses the sec champ game, they should still be above nd but the heirarchy is strictly ore > utx > psu > nd > uga

if secL == utx and b1gL == psu:
	s5 = utx
	s6 = psu
	s7 = nd
elif secL == uga and b1gL == psu:
	s5 = psu
	s6 = nd
	s7 = uga
elif secL == utx and b1gL == ore:
	s5 = ore
	s6 = utx
	s7 = nd
elif secL == uga and b1gL == ore:
	s5 = ore
	s6 = nd
	s7 = uga

#as previously stated, smu is a lock for the playoff even if they lose to clemson

if accL == smu:
	s10 = smu
	s11 = ind
else:
	s10 = ind
	s11 = smu

print(f'{mwc["name"]}, {aac["name"]}, {b12["name"]}, {sec["name"]}, {acc["name"]}, and {b1g["name"]} are the 2024 confernce champions!')

print(f"{s5['name']}, {s6['name']}, {s7['name']}, {osu['name']}, {tenn['name']}, {s10['name']}, and {s11['name']} are the at-large bids!")

print(f"{fifthchamp['name']} is the Group of 5 representative!")

time.sleep(1)
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
print(f'Dec 20, 8:00p\n{s["5"]["stad"]}')
wof12v5 = oc(s["5"],s["12"])

#11 at 6
print(f'\nDec 21, 12:00p\n{s["6"]["stad"]}')
wof11v6 = oc(s["6"],s["11"])

#10 at 7
print(f'\nDec 21, 4:00p\n{s["7"]["stad"]}')
wof10v7 = oc(s["7"],s["10"])

#9 at 8
print(f'\nDec 21, 8:00p\n{s["8"]["stad"]}')
wof9v8 = oc(s["8"],s["9"])


#--QUARTERS--

#whichever of the four conf champs are closest to the location/tiebreaker goes to higher seed
#for example, oregon is projected to be the one seed, so theyd have first pick of arena, and would go to the rose bowl
#however, if clemson and georgia would both want to play in atlanta, uga would get priority over clem becuase georgia is the two seed
#clem would be stuck in nola

#winner of 12/5 plays 4
#winner of 11/6 plays 3
#winner of 10/7 plays 2
#winner of 9/8 plays 1

time.sleep(2)
print("\nQuarterfinals!\n")
time.sleep(8)

#=Fiesta Bowl=
print("Dec 31, 7:30p \nthe Fiesta Bowl at State Farm Stadium in Glendale, AZ")
fb = ns(s["4"],wof12v5)

#=Peach Bowl=
print("Jan 1, 1:00p \nthe Peach Bowl at Mercedes Benz Stadium in Atlanta, GA")
pb = ns(s["3"],wof11v6)

#=Rose Bowl=
print("Jan 1, 5:00p \nthe Rose Bowl in Pasadena, CA")
rb = ns(s["1"],wof9v8)

#=Sugar Bowl=
print("Jan 1, 8:45p \nthe Sugar Bowl at Caesars Superdome in New Orleans, LA")
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

print(f'the 2025 National Champions are the {nc["name"]} {nc["masc"]}!')