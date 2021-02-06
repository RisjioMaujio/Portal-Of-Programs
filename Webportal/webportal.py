import webbrowser
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


    
display=open(r"assets"+navigator_symbol+"website.txt","r")
s=display.read()
print(s)
display.close()




# commmand=input("enter: ")
# webbrowser.open('https://www.google.com/?#q=' + commmand)
# commmand=input("enter: ")
# webbrowser.open('https://www.bing.com/search?q=' + commmand)
# commmand=input("enter: ")
# webbrowser.open('https://www.youtube.com/results?search_query=' + commmand)
# commmand=input("enter: ")
# webbrowser.open('https://gaana.com/search/' + commmand)





def def_main():
	display=open(r"assets"+navigator_symbol+"website.txt","r")
	s=display.read()
	print(s)
	display.close()



	while True:
		displa=open(r"assets"+navigator_symbol+"category.txt","r")
		s=displa.read()
		print(s)
		displa.close()
		end_option = str(input("\tPlease Type The Category of Website Which You Want to Visit : ")).capitalize()
		print("\n" * 3)
		if(end_option=="Search"):
			dis=open(r"assets"+navigator_symbol+"search.txt","r")
			rp=dis.read()
			print(rp)
			search()
			break
			

		elif(end_option=="Social"):
			dis=open(r"assets"+navigator_symbol+"social.txt","r")
			rp=dis.read()
			print(rp)
			social()
			break			
			

		elif(end_option=="Gservice"):
			dis=open(r"assets"+navigator_symbol+"Gservices.txt","r")
			rp=dis.read()
			
			print(rp)
			gservices()
			break	

		elif(end_option=="Mservice"):
			dis=open(r"assets"+navigator_symbol+"Mservices.txt","r")
			rp=dis.read()

			print(rp)
			mservices()	
			break


		elif(end_option=="Entertainment"):
			dis=open(r"assets"+navigator_symbol+"entertainment.txt","r")
			rp=dis.read()
			print(rp)
			entertainment()
			break
			


		elif(end_option=="Shooping"):
			dis=open(r"assets"+navigator_symbol+"shooping.txt","r")
			rp=dis.read()
			print(rp)	
			shooping()


		elif(end_option=="Fooding"):
			dis=open(r"assets"+navigator_symbol+"fooding.txt","r")
			rp=dis.read()
			print(rp)
			fooding()


		elif(end_option=="Travelling"):
			dis=open(r"assets"+navigator_symbol+"travelling.txt","r")
			rp=dis.read()
			print(rp)
			travelling()											
		
				
		else:
			print("\n" * 8 +"\t\tYou Have Entered { " + str(end_option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)

	



def search():
		while True:
			option=str(input("\t Please Type Your Desired Search Engine Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Google"):
				print("\tOk You Have Selected " + str(option) + " as Your Search Engine")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.google.com/?#q=')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.google.com/?#q=' + commmand)
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()				
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		




			elif(option=="Bing"):
				print("\tOk You Have Selected " + str(option) + " as Your Search Engine")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.bing.com/search?q=')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.bing.com/search?q=' + commmand)	
					print("\n" * 4)
						
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()						
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		
				
				


			elif(option=="Yahoo"):
				print("\tOk You Have Selected " + str(option) + " as Your Search Engine")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://in.yahoo.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://in.search.yahoo.com/search?p=' + commmand)
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()			
				else:
					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		


				
			elif(option=="Ask"):
				print("\tOk You Have Selected " + str(option) + " as Your Search Engine")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.ask.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.ask.com/web?o=0&l=dir&qo=homepageSearchBox&q=' + commmand)			
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:
					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)

	

def social():
		while True:
			option=str(input("\t Please Type Your Desired Social Website Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Facebook"):
				print("\tOk You Have Selected " + str(option) + " as Your Social Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.facebook.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.bing.com/search?q=' + commmand+'%20site:facebook.com&FORM=QBDCRD')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		




			elif(option=="Instagram"):
				print("\tOk You Have Selected " + str(option) + " as Your Social Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.instgram.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.bing.com/search?q=' + commmand+'%20site:instagram.com&FORM=QBDCRD')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		
		
				
				


			elif(option=="Twitter"):
				print("\tOk You Have Selected " + str(option) + " as Your Social Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.twitter.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://twitter.com/search?q='+commmand+'&src=typed_query')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inapprropriate. Please Try Again ;) "+"\n" * 8)
				
			elif(option=="Blog"):
				print("\tOk You Have Selected " + str(option) + " as Your Social Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.blogger.com/about/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.searchblogspot.com/search?q=' + commmand)
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inapprropriate. Please Try Again ;) "+"\n" * 8)
			elif(option=="Pinterest"):
				print("\tOk You Have Selected " + str(option) + " as Your Social Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.pinterest.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.pinterest.com/' + commmand)
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)




			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
	



def shooping():
		while True:
			option=str(input("\t Please Type Your Desired Shooping Website Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Amazon"):
				print("\tOk You Have Selected " + str(option) + " as Your Shooping Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.amazon.in/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.amazon.in/s?k='+commmand+'&ref=nb_sb_noss_2')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		




			elif(option=="Flipkart"):
				print("\tOk You Have Selected " + str(option) + " as Your Shooping Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.flipkart.com/=')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.flipkart.com/search?q=' + commmand)
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		
		
				
				


			elif(option=="Ebay"):
				print("\tOk You Have Selected " + str(option) + " as Your Shooping Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://pages.ebay.in/cod/cod_buyer.html')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=' + commmand)
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:
					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)


				
			elif(option=="Snapdeal"):
				print("\tOk You Have Selected " + str(option) + " as Your Shooping Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.snapdeal.com/')
					print("\n" * 4)
				
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.snapdeal.com/search?keyword=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)







			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		
				




			
def entertainment():
		while True:
			option=str(input("\t Please Type Your Desired Entertainmnet Website Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Youtube"):
				print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.youtube.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.youtube.com/results?search_query=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			elif(option=="Hotstar"):
				print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.hotstar.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.hotstar.com/in/search?q=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			
					
					


			elif(option=="Ganna"):
				print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://gaana.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://gaana.com/search/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			
					
			elif(option=="Savaan"):
				print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.jiosaavn.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.jiosaavn.com/search/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			
			elif(option=="Prime"):
				print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.primevideo.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.primevideo.com/ref=atv_sr_sug_5?_encoding=UTF8&phrase=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			





			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		
					
				



			
def travelling():
		while True:
			option=str(input("\t Please Type Your Desired Travelling Website Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Railyatri"):
				print("\tOk You Have Selected " + str(option) + " as Your Travelling Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.railyatri.in/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type The Correct Train Number To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.railyatri.in/time-table/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			elif(option=="Maketrip"):
				print("\tOk You Have Selected " + str(option) + " as Your Travelling Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.makemytrip.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					print("\t You Had Selected " + str(option) + " Which Is Offering on Site Search  ")
					print("\n" * 4)
					print("\t\t\t\t" + " So " + str(option) + " is Now Redirecting.......")
					webbrowser.open('https://www.makemytrip.com/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			
					
					





			elif(option=="Cleartrip"):
				print("\tOk You Have Selected " + str(option) + " as Your Travelling Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.cleartrip.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					print("\t You Had Selected " + str(option) + " Which Is Offering on Site Search  ")
					print("\n" * 4)
					print("\t\t\t\t" + " So " + str(option) + " is Now Redirecting.......")
					webbrowser.open('https://www.cleartrip.com/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			elif(option=="Irctc"):
				print("\tOk You Have Selected " + str(option) + " as Your Travelling Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.irctc.co.in/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type The Correct Train Number To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					print("\n" * 4)
					print("\t\t\t\tOn " + str(option) + " Real Time Search Works So May Query You Given Not Responds So Redirecting.......")
					webbrowser.open('https://www.irctc.co.in/nget/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)


			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		
					
def fooding():
		while True:
			option=str(input("\t Please Type Your Desired Fooding Website Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Zomato"):
				print("\tOk You Have Selected " + str(option) + " as Your Fooding Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.zomato.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t You Can Give Only 'Restuarnts' Query To Seacrh On As It is Real Time Search Website " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.zomato.com/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			elif(option=="Swiggy"):
				print("\tOk You Have Selected " + str(option) + " as Your Fooding Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.hotstar.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t You Can Give Only 'Restuarnts' Query To Seacrh On As It is Real Time Search Website " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.swiggy.com/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
					
					






			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		

def gservices():
		while True:
			option=str(input("\t Please Type Your Desired Google Service Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Account"):
				print("\tOk You Have Selected " + str(option) + " as Your Google Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('http://accounts.google.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://support.google.com/accounts/search?q=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			elif(option=="Drive"):
				print("\tOk You Have Selected " + str(option) + " as Your Google Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://drive.google.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://drive.google.com/drive/search?q=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			
					
					



			elif(option=="Gmail"):
				print("\tOk You Have Selected " + str(option) + " as Your Google Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('http://mail.google.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://mail.google.com/mail/u/0/#search/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			

			elif(option=="Maps"):
				print("\tOk You Have Selected " + str(option) + " as Your Google Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://maps.google.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.google.com/maps/search/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			elif(option=="Youtube"):
				print("\tOk You Have Selected " + str(option) + " as Your Google Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.youtube.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.youtube.com/results?search_query=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		



		

def mservices():
		while True:
			option=str(input("\t Please Type Your Desired Microsoft Service Name :  ")).capitalize()
			print("\n" * 4)
			if(option=="Account"):
				print("\tOk You Have Selected " + str(option) + " as Your Microsoft Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://accounts.microsoft.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://docs.microsoft.com/en-us/search/?terms=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			elif(option=="Onedrive"):
				print("\tOk You Have Selected " + str(option) + " as Your Microsoft Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://onedrive.live.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://onedrive.live.com/?id=root&cid=C1094D34D4A160D6&qt=search&q=' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			
					
					



			elif(option=="Outlook"):
				print("\tOk You Have Selected " + str(option) + " as Your Microsoft Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://outlook.live.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://outlook.live.com/mail/0/search/' + commmand)
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			

			elif(option=="Maps"):
				print("\tOk You Have Selected " + str(option) + " as Your Microsoft Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.bing.com/maps/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					commmand=str(input("\t Please Type You Desired Query To Seacrh On " + str(option) + "  : ")).capitalize()
					print("\n" * 4)
					print("\t\t\t\t" + str(commmand) + " on " + str(option) + " is Now Searching.......")
					webbrowser.open('https://www.bing.com/search?q=' + commmand+'location')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			
			elif(option=="Office"):
				print("\tOk You Have Selected " + str(option) + " as Your Microsoft Service Website")

				print("\n" * 4)
				print("\t Now Select The Function to be Performed on " + str(option) + " ")
				print("\n"*4)
				dis=open(r"assets"+navigator_symbol+"option.txt","r")
				rp=dis.read()
				print(rp)
				fun=str(input("\t Please Type You Desired Function To be Perform in " + str(option) + "  : ")).capitalize()
				if(fun=="Home"):
					print("\n" * 4)
					print("\t \t     \t  Home Page of " + str(option) + " is Opening ......")
					webbrowser.open('https://www.office.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()

				elif(fun=="Query"):
					print("\n" * 4)
					
					print("\t You Had Selected " + str(option) + " Which Is Offering on Site Search  ")
					print("\n" * 4)
					print("\t\t\t\t" + " So " + str(option) + " is Now Redirecting.......")
					webbrowser.open('https://www.office.com/')
					print("\n" * 4)
					
					print("\t\t\tReturning To Category of Website Selection ")
					def_main()
				else:

					print("\n" * 8 +"\t\tYou Have Entered { " + str(fun) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
			




			else:
				print("\n" * 8 +"\t\tYou Have Entered { " + str(option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
		



def_main()
