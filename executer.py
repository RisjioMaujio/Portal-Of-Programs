import datetime                    
import os  
import time
import random as r
import webbrowser
start=time.time()


navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 


def def_mains():
    display=open(r"SeriesGenrator"+navigator_symbol+"assets"+navigator_symbol+"series.txt","r")
    s=display.read()
    print(s)
    display.close()
    while True:


        end_option = str(input("\tWhich Type of Series You Want to Genrate { Command Aceepting Only In Limit and Terms } : ")).capitalize()
        

        if(len(end_option)==5 or len(end_option)==4):
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
                

            elif (end_option == "Terms"):
                print("\n" * 10 +"\t\t\t\t\t\t\t\tSeries Genrator Via Terms Is Starting ...."+"\n" * 10)


                print("\t Ok You Have Selected The Series Upto Nth Terms. Now Give Me Some More Deatils To Genrate Series ")
                print("\n"*5)
                print("\t Let's Give The Starting Term and Nth Terms that Upto Which Series Will Execute ")         
                print("\n"*5)
            
                start_terms = int(input("\t--> Enter The Number From Which This Series Will  Start Execute : "))
                print()
                print()
                end_terms = int(input("\t--> Enter The Nth Terms To Which This Series Will Execute : "))
                print("\n"*5)   
                terms(start_terms,end_terms)            
                

            elif (end_option=="Exit"):
                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Series Genrator")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Portal Of Program ..........")
                
                executer()
                
            else:
                print("\n" * 8 +"\t\tYou Have Entered { " + str(end_option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 6)
        else:
            print("\n" * 8 +"\t\tYou Have Entered { " + str(end_option) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 6)




def limit(start_terms,end_terms):
    while True:

        dis=open(r"SeriesGenrator"+navigator_symbol+"assets"+navigator_symbol+"Datas.txt","r")
        df=dis.read()
        print()
        print(df)
        print("\n"*5)
        operator = str(input("\tEnter The Opertaion Name To which you Want To Repeat That Operator Fucntion in Series : ")).capitalize()
        print("\n"*3)
        if(len(operator)==3 or len(operator)==4):
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

            elif (operator=="Exit"):
                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting from The Series Genrator Via Limit")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Portal Of Program ......")
                
                executer()  
            
            else:
                print("\n" * 10 + "You Have Entered (" + str(operator) + ")"" Which is Inappropriate. Please Try Again ;) "+"\n" * 10)      
        else:
            print("\n" * 10 +"You Have Entered (" + str(operator) + ")"" Which is Inappropriate. Please Try Again ;) "+"\n" * 10)



def terms(start_terms,end_terms):
    while True:

        dis=open(r"SeriesGenrator"+navigator_symbol+"assets"+navigator_symbol+"Datas.txt","r")
        df=dis.read()
        print()
        print(df)
        print("\n"*5)
        operator = str(input("\tEnter The Opertaion Name To which you Want To Repeat That Operator Fucntion in Series : ")).capitalize()
        print("\n"*3)
        if(len(operator)==3 or len(operator)==4):
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


            elif (operator=="Exit"):
                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting from the Series Genrator Via Terms")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Portal of Program .......")
                
                executer()

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
        if(a>b):
            print("\n" * 5 + "\tYou Have Entered The Starting Limit is larger than Ending Limit Which is Inappropriate For Addition Operator . " + "\n\t\t\t"*2 + "\t\t\t\t Please Try Again ;) "+"\n" * 6) 
            print("\n" * 5 +"\t\t\t\t\t\tReturning To Category  Selection of Series Genrator Program")
            print()
            def_mains()
        if(c.isdigit()==True):
            print("\tYour Desiered Series Is :   --->   ")
            print("\n"*3)

            while a<b:

                print(a,end= " , ")
                a=a+rec
            print("\n"*5)   
            def_mains() 
        

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
        def_mains() 
        

def lsub(start_terms,end_terms):
    while True:
        a=start_terms
        b=end_terms
        print()
        rec = int(input("\tEnter The Number By Which You Want To Continoulsy Subtract In Your Series : "))
        print("\n"*3)
        c=str(rec)
        if(a<b):
            print("\n" * 5 + "\tYou Have Entered The Starting Limit Samller than Ending Limit Which is Inappropriate For Subtaction Operator . " + "\n\t\t\t"*2 + "\t\t\t\t Please Try Again ;) "+"\n" * 6) 
            print("\n" * 5 +"\t\t\t\t\t\tReturning To Category  Selection of Series Genrator Program")
            print()
            def_mains()
        if(c.isdigit()==True):
            print("\tYour Desiered Series Is :   --->   ")
            print("\n"*3)

            while a>b:

                print(a,end= " , ")
                a=a-rec
        print("\n"*5)   
        def_mains() 
        

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
            def_mains() 
        

def lmpt(start_terms,end_terms):
    while True:
        a=start_terms
        b=end_terms
        print()
        rec = int(input("\tEnter The Number By Which You Want To Continoulsy Multiply In Your Series : "))
        print("\n"*3)
        c=str(rec)
        if(a>b):
            print("\n" * 5 + "\tYou Have Entered The Starting Limit is larger than Ending Limit Which is Inappropriate For Multiplication Operator . " + "\n\t\t\t"*2 + "\t\t\t\t Please Try Again ;) "+"\n" * 6) 
            print("\n" * 5 +"\t\t\t\t\t\tReturning To Category  Selection of Series Genrator Program")
            print()
            def_mains()
        if(c.isdigit()==True):
            print("\tYour Desiered Series Is :   --->   ")
            print("\n"*3)

            while a<b:

                print(a,end= " , ")
                a=a*rec

            print("\n"*5)   
            def_mains() 
        

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
            def_mains() 
        

def ldiv(start_terms,end_terms):
    while True:
        a=float(start_terms)
        b=end_terms
        print()
        rec = int(input("\tEnter The Number By Which You Want To Continoulsy Divide In Your Series : "))
        print("\n"*3)
        c=str(rec)
        if(a<b):
            print("\n" * 5 + "\tYou Have Entered The Starting Limit Samller than Ending Limit Which is Inappropriate For Division Operator . " + "\n\t\t\t"*2 + "\t\t\t\t Please Try Again ;) "+"\n" * 6) 
            print("\n" * 5 +"\t\t\t\t\t\tReturning To Category  Selection of Series Genrator Program")
            print()
            def_mains()
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
                def_mains() 
        

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
            def_mains() 
        



# Webportal Code Starting




def def_main():
    display=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"website.txt","r")
    s=display.read()
    print(s)
    display.close()



    while True:
        displa=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"category.txt","r")
        s=displa.read()
        print(s)
        displa.close()
        end_option = str(input("\tPlease Type The Category of Website Which You Want to Visit : ")).capitalize()
        print("\n" * 3)
        if(end_option=="Search"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"search.txt","r")
            rp=dis.read()
            print(rp)
            search()
            break
            

        elif(end_option=="Social"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"social.txt","r")
            rp=dis.read()
            print(rp)
            social()
            break           
            

        elif(end_option=="Gservice"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"Gservices.txt","r")
            rp=dis.read()
            
            print(rp)
            gservices()
            break   

        elif(end_option=="Mservice"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"Mservices.txt","r")
            rp=dis.read()

            print(rp)
            mservices() 
            break


        elif(end_option=="Entertainment"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"entertainment.txt","r")
            rp=dis.read()
            print(rp)
            entertainment()
            break
            


        elif(end_option=="Shooping"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"shooping.txt","r")
            rp=dis.read()
            print(rp)   
            shooping()


        elif(end_option=="Fooding"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"fooding.txt","r")
            rp=dis.read()
            print(rp)
            fooding()


        elif(end_option=="Travelling"):
            dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"travelling.txt","r")
            rp=dis.read()
            print(rp)
            travelling()                                            

        elif (end_option=="Exit"):
            print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting from the Portal")
            print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Portal of Program")
            executer()
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting from the Search Engines")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")   
                executer()          





            elif(option=="Bing"):
                print("\tOk You Have Selected " + str(option) + " as Your Search Engine")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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

            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Social Websites")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  


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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
        

            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Shooping Websites")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  


            elif(option=="Flipkart"):
                print("\tOk You Have Selected " + str(option) + " as Your Shooping Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Entertainment Websites")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  



            elif(option=="Hotstar"):
                print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            
                    
                    


            elif(option=="Gaana"):
                print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            
                    
            elif(option=="Saavn"):
                print("\tOk You Have Selected " + str(option) + " as Your Entertainmnet Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The travelling Websites")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  



            elif(option=="Maketrip"):
                print("\tOk You Have Selected " + str(option) + " as Your Travelling Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Fooding Websites")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  



            elif(option=="Swiggy"):
                print("\tOk You Have Selected " + str(option) + " as Your Fooding Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Google Services")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  





            elif(option=="Drive"):
                print("\tOk You Have Selected " + str(option) + " as Your Google Service Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
            
            elif(option=="Exit"):

                print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting From The Microsoft Services")
                print("\n" * 10 +"\t\t\t\t\t\t\t\tReturning To Main Program")
                executer()  



            elif(option=="Onedrive"):
                print("\tOk You Have Selected " + str(option) + " as Your Microsoft Service Website")

                print("\n" * 4)
                print("\t Now Select The Function to be Performed on " + str(option) + " ")
                print("\n"*4)
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
                dis=open(r"Webportal"+navigator_symbol+"assets"+navigator_symbol+"option.txt","r")
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
        
def exiting():

    end=time.time()
    net=round(end-start,1)
    print("\t\t\t\t Ok , You Want To Close The Program \n\n\n"+"\t\t\t\t You Have Spent",net,"Seconds on Portal of Programs"+"\n"*3)
    print("\t\t\t\tThank's For The Time "+"\n"*3)
    print("\t\t\t\t ;) Before closing The Program a Feedback Form Will be Open in Your Browser in Just Few Moments"+"\n"*2)
    print("\t\t\t\t After Opeing The Feedback Form The program Will get Automatic Close")
    webbrowser.open("https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAARX1D3JUMFEzTERZMlEzRkowVkZJUkVSTDZVQzdGMy4u")
    print("\n"*2+"\t\t\t  This Project is Created By : 'Shubham Maurya' ( Risjio Maujio )")
    print("\n"*5)
    print("\t\t\t\t\t\t\t\t\tThank's And Have A Great Day ;) ;) ;) ;) ;) ;) ;) "+"\n"*8)
    exiter=str(input("Press Any Key To Continue : "))
    exit()
    

def runner():
    qwer=open(r"Executer"+navigator_symbol+"details.txt","r")
    s=qwer.read()
    print(s)
    qwer.close()
    while True:
        choice=str(input("\t   Please Type Your Desired Option For Either ' Sign In ' Or ' Sign Up '  : ")).capitalize()
        print("\n"*2)
        if(choice=="Signin"):
            print("\n" * 7 +"\t\t\t\t\t\t\t\tSign In For The Program Is Starting ...."+"\n" * 7)
            signin()
        elif(choice=="Signup"):
            print("\n" * 7 +"\t\t\t\t\t\t\t\tSign Up For The Program Is Starting ...."+"\n" * 7)
            signup()
        elif(choice=="Exit"):
            exiting()
        else:
            print("\n" * 4 +"\t\tYou Have Entered { " + str(choice) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 5)



def signin():
    while True:
        print("\t Please Provide Some Deatils To Validate You Are Existing User")
        print("\n"*4)
        name = str(input("\t Please Provide Your Name That You Have Entered at The Time Of Sign Up Of the Portal of Programs : "))
        print("\n"*2)
        password = str(input("\t Please Provide Your Password That You Have Entered at The Time Of Sign In Of The Portal of Programs : "))
        print("\n"*2)
        otp=''
        for i in range(4):
            otp+=str(r.randint(1,9))
        print("\t\t  The O.T.P. of The Current Session Sign In is : ",otp)
        print("\n"*2)
        otp_taking=str(input("\t Please Type The Above Generated O.T.P. For Moving Forward In Sign In Process : "))
        print("\n"*3)
        if(otp_taking==otp):
            print("\tThe O.T.P. That You Have Entered is Matching To System Genrated O.T.P. ")
            print("\n"*4)

            f = open("User_Data.txt",'r')
            info = f.read()
            info = info.split()
            if(name in info):
                index = info.index(name) + 1
                usr_password = info[index]
 
                if(usr_password == password):
                    print("\n"*2)
                    print("\t\t\t\t\t\t Welcome Back, " + name+" Now You Can Use The Portal Of Programs ")
                    print("\n"*5)
                    print("\t\t\t\t\t\t You Are Redirecting to The Selection Of Program To Which You Want ........ ")
                    executer()
                else:
                    print("\n" * 4 +"\t\tYou Have Entered { " + str(password) + " } "" Which is Wrong For The Entered User Name. Please Try Again ;) "+"\n" * 5)
            else:

                print("\n" * 4 +"\t\tYou Have Entered { " + str(name) + " } "" Which is Not in Database. Please Try Again ;) "+"\n" * 5)
                print("\n"*5)
                print("\t\t\t\t\t\t You Are Redirecting to The Sign In or Sign Up Of Portal of Programs ........  ")
                print("\n"*5)
                runner()


        else:
            print("\n" * 4 +"\t\tYou Have Entered { " + str(otp_taking) + " } "" Which is Not Matching To System Genrated O.T.P. , Please Try Again ;) "+"\n" * 5)


def signup():
    while True:
        print("\t Please Provide Some Deatils To Become a User For The Portal Of Programs")
        print("\n"*4)
        name = str(input("\t Please Provide Your Name That You Want To Entered at The Time Of Sign In Of the Portal Of Programs : "))
        print("\n"*2)
        password = str(input("\t Please Provide Your Name That You Want To Entered at The Time Of Sign In Of Portal of Programs : "))
        print("\n"*2)
        otp=''
        for i in range(4):
            otp+=str(r.randint(1,9))
        print("\t\t  The O.T.P. of The Current Session Sign Up is : ",otp)
        print("\n"*4)
        otp_taking=str(input("\t Please Type The Above Generated O.T.P. For Moving Forward In Sign In Process : "))
        print("\n"*4)
        if(otp_taking==otp):
            print("\tThe O.T.P. That You Have Entered is Matching To System Genrated O.T.P. ")
            print("\n"*4)

            f = open("User_Data.txt",'r')
            info=f.read()
            if(name in info):
                print("\n" * 4 +"\t\tYou Have Entered { " + str(name) + " } "" Which is Which is Avalaible In Database Please Try Again ;) "+"\n" * 5)
                print("\n"*5)
                print("\t\t\t\t\t\t You Are Redirecting to The Sign In or Sign Up Of Portal of Programs ........  ")
                print("\n"*5)

                runner()
            f.close()
            if(name not in info):
                f = open("User_Data.txt",'w')
                info = info + " " +name + " " + password
                f.write(info)
                f.close()

                print("\n"*5)
                print("\t\t\t\t\t\t You Are Redirecting to The Sign In Of Portal of Programs ........  ")
                print("\n"*5)
                signin()

        else:
            print("\n" * 4 +"\t\tYou Have Entered { " + str(otp_taking) + " } "" Which is Not Matching To System Genrated O.T.P. , Please Try Again ;) "+"\n" * 5)



def executer():
    while True:
        qwer=open(r"Executer"+navigator_symbol+"programs.txt","r")
        s=qwer.read()
        print(s)
        qwer.close()

        func=str(input(("\t\tPlease Type The Program Name That You Want To Run : "))).capitalize()
        if(func=="Series"):

            print("\n" * 10 +"\t\t\t\t\t\t\t\tSeries Genrator Is Starting ...."+"\n" * 10)


            print("\n"*5)

            def_mains()

        elif(func=="Portal"):
            print("\n" * 10 +"\t\t\t\t\t\t\t\tWeb Portal Is Starting ...."+"\n" * 10)



            print("\n"*5)
            def_main()
        elif (func=="Exit"):
            print("\n" * 10 +"\t\t\t\t\t\t\t\tYou Are Exiting from the Program"+"\n"*10)
            runner()


        else:

            print("\n" * 8 +"\t\tYou Have Entered { " + str(func) + " } "" Which is Inappropriate. Please Try Again ;) "+"\n" * 8)
        


runner()
