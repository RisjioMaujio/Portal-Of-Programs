import datetime                    
import os  

from tabulate import *
import csv
import pandas as pd
import sys
import os


navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 


    
display=open(r"assets"+navigator_symbol+"series.txt","r")
s=display.read()
print(s)
display.close()



def def_main():
	while True:


		end_option = str(input("\tWhich Type of Series You Want to Genrate { Command Aceepting Only In Limit and Terms } : ")).capitalize()
		

		if(len(end_option)==5):
			if(end_option=="Limit"):
				print("\n" * 10 +"\t\t\t\t\t\t\t\tSeries Genrator Via Limit Is Starting ...."+"\n" * 10)

				print("\tOk , You Have Selected The Series In Limit. Now Give Me Some More Deatils To Genrate Series ")
				print("\n"*5)
				
				
				print("\tLet's Give Me The Starting and Ending Limit ")
				print("\n"*5)
				

				start_terms = int(input("\tEnter The Number From Where you Want to Start Your Series : "))
				print()
				print()
				end_terms = int(input("\tEnter The Number To Where you Want to End Your Series : "))
				print("\n"*5)
				limit(start_terms,end_terms)
				break

			elif (end_option == "Terms"):
				print("\n"*5)
				print("\t Ok You Have Selected The Series Upto Nth Terms. Now Give Me Some More Deatils To Genrate Series ")
				print("\n"*5)
				print("\t Let's Give The Starting Term and Nth Terms that Upto Which Series Will Execute ")			
				print("\n"*5)
			
				start_terms = int(input("\t--> Enter The Number From Which This Series Will  Start Execute : "))
				print()
				end_terms = int(input("\t--> Enter The Nth Terms To Which This Series Will Execute : "))
				print("\n"*5)	
				terms(start_terms,end_terms)			
				break
			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(end_option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 6)
		else:
			print("\n" * 8 +"\t\tYou Have Entered { " + str(end_option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 6)


def coorector(start_terms,end_terms):
	dsp=open(r"assets"+navigator_symbol+"series.txt","r")
	s=dsp.read()
	print(s)
	dsp.close()







def limit(start_terms,end_terms):
	while True:

		dis=open(r"assets"+navigator_symbol+"Datas.txt","r")
		df=dis.read()
		print()
		print(df)
		print("\n"*5)
		operator = str(input("\tEnter The Opertaion Name To which you Want To Repeat That Operator Fucntion in Series : ")).capitalize()
		print("\n"*3)
		if(len(operator)==3):
			if(operator=='Add'):
				print("\tOk You had Choosen Add Operator For You Series Genrator")
				print("\n"*2)
				ladd(start_terms,end_terms)
			elif(operator=='Sub'):
				lsub(start_terms,end_terms)
				
			elif(operator=='Mpt'):
				lmpt(start_terms,end_terms)
			elif(operator=='Div'):
				ldiv(start_terms,end_terms)
			else:
				print("\n" * 10 + "You Have Entered (" + str(operator) + ")"" Which is Inappropriate. Please Try Again ;) "+"\n" * 10)		
		else:
			print("\n" * 10 +"You Have Entered (" + str(operator) + ")"" Which is Inappropriate. Please Try Again ;) "+"\n" * 10)



def terms(start_terms,end_terms):
	while True:

		dis=open(r"assets"+navigator_symbol+"Datas.txt","r")
		df=dis.read()
		print()
		print(df)
		print("\n"*5)
		operator = str(input("\tEnter The Opertaion Name To which you Want To Repeat That Operator Fucntion in Series : ")).capitalize()
		print("\n"*3)
		if(len(operator)==3):
			if(operator=='Add'):
				print("\tOk You had Choosen Add Operator For You Series Genrator")
				print("\n"*2)
				tadd(start_terms,end_terms)
			elif(operator=='Sub'):
				print("\tOk You had Choosen Subtract Operator For You Series Genrator")
				print("\n"*2)				
				tsub(start_terms,end_terms)
				
			elif(operator=='Mpt'):
				print("\tOk You had Choosen Multiply Operator For You Series Genrator")
				print("\n"*2)				
				tmpt(start_terms,end_terms)
			elif(operator=='Div'):
				print("\tOk You had Choosen Division Operator For You Series Genrator")
				print("\n"*2)				

				tdiv(start_terms,end_terms)
			else:
				print("\t" * 10 + "You Have Entered (" + str(operator) + ")"" Which is Inappropriate. Please Try Again ;) "+"\n" * 10)		
		else:
			print("\t" * 10 +"You Have Entered (" + str(operator) + ")"" Which is Inappropriate. Please Try Again ;) "+"\n" * 10)



def ladd(start_terms,end_terms):
	while True:
		a=start_terms
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Add In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			print("\tYour Desiered Series Is :   --->   ")
			print("\n"*3)

			while a<b:

				print(a,end= " , ")
				a=a+rec
			print("\n"*5)	
			def_main()	
		




def tadd(start_terms,end_terms):
	
	

	a=start_terms
	b=end_terms
	print()
	rec = int(input("\tEnter The Number By Which You Want To Continoulsy Add In Your Series : "))
	print("\n"*3)
	c=str(rec)
	if(c.isdigit()==True):
		print("\tYour Desiered Series Is :   --->   ")
		print("\n"*3)

		for i in range(1,b+1):
			print(a,end=" ")
			a=a+rec
		print("\n"*5)	
		def_main()	
		




def lsub(start_terms,end_terms):
	while True:
		a=start_terms
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Subtract In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			print("\tYour Desiered Series Is :   --->   ")
			print("\n"*3)

			while a>b:

				print(a,end= " , ")
				a=a-rec
		print("\n"*5)	
		def_main()	
		


def tsub(start_terms,end_terms):
	while True:
		a=start_terms
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Subtract In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			print("\tYour Desiered Series Is :   --->   ")
			print("\n"*3)

			for i in range(1,b+1):
				print(a,end=" ")
				a=a-rec
			print("\n"*5)	
			def_main()	
		






def lmpt(start_terms,end_terms):
	while True:
		a=start_terms
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Multiply In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			print("\tYour Desiered Series Is :   --->   ")
			print("\n"*3)

			while a<b:

				print(a,end= " , ")
				a=a*rec

			print("\n"*5)	
			def_main()	
		

def tmpt(start_terms,end_terms):
	while True:
		a=start_terms
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Multiply In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			print("\tYour Desiered Series Is :   --->   ")
			print("\n"*3)

			for i in range(1,b+1):
				print(a,end=" , ")

				a=a*rec

			print("\n"*5)	
			def_main()	
		


		
	

def ldiv(start_terms,end_terms):
	while True:
		a=float(start_terms)
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Divide In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			if(rec == 0):
				print("Error Cant be Divide By Zero")
			else:

				print("\tYour Desiered Series Is :   --->   ")
				print("\n"*3)

				while a>b:

					print(a,end= " , ")
					a=a/rec


				print("\n"*5)	
				def_main()	
		



def tdiv(start_terms,end_terms):
	while True:
		a=float(start_terms)
		b=end_terms
		print()
		rec = int(input("\tEnter The Number By Which You Want To Continoulsy Multiply In Your Series : "))
		print("\n"*3)
		c=str(rec)
		if(c.isdigit()==True):
			print("\tYour Desiered Series Is :   --->   ")
			print("\n"*3)

			for i in range(1,b+1):
				print(a,end = " , ")

				a=a/rec
				
			print("\n"*5)	
			def_main()	
		


def_main()


