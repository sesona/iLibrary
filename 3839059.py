import pandas as pd

df = pd.read_csv ('SouthAfricaCrimeStats_v2.csv', sep=',')#reads the csv file and stores it into pandas inbuilt dataframe, using the delimter of "," I sperate the columns by the","

def menu():#created the function menu which will act as the user interface
    loop = True #variable used to keep the while loop loading
    while loop == True:
        print("Hello welcome to the South African Crime Stats database \n")
        print("1. Print database ")
        print("2. Report on the amount of crimes that occurred in a user specified province and period.")
        print("3. Report on the total amount of crimes for a user specified station for period full period of 2004 to 2015.")
        print("4. How many incidents involving truck hijacking were reported for the period 2010 -2011?")
        print("5. How many “Arson” incidents occurred in Boitekong and Ngodwana in 2009 – 2010?")
        print("6. Which type of crime had the highest number of incidents in the 2014 – 2015 period?")
        print("7. For which period did Nongoma in KwaZulu Natal have the lowest amount of murdercases?")
        print("8. Which stations in the North West province has 0 cases for Attempted murder for the period 2008 – 2009?")
        print("9. Which period had the highest crime 2005-2006 to 2015-2016")
        print("10.exit")
        print("=========================================================================================== \n")
        menuOP = input("Please enter 1-10: \n") #Told the user to use numbers as inputs instead so its less mistakes
        if(menuOP == "1"):#if the user chooses 1 then it will print the dataframe df
            print(df)
            print("=========================================================================================== \n")

        elif(menuOP == "2"): #If the user to select 2
            user = input("Which Province: ") # takes in the Province the user selected and stores it in the variable user
            user2 = input("Which period,please enter in the format (eg. 2009-2010): \n") #takes in the period the user selected and stores it in the variable user2
            a = (df.loc[df["Province"] == user,user2])#takes the row within Province which the user inputed "user" and with the year "user2"
            a = a.sum(axis = 0,skipna = True) #Adds all values within the row
            print("\n")
            print("=========================================================================================== \n")
            print("The amount of crime taken place at "+user+" in "+user2+" is: "+str(a)+"\n") #prints the  a
            print("=========================================================================================== \n")

        elif(menuOP == "3"): #If the user to select 3
            user = input("Which station: ")#takes in the station and saves it as user
            a = (df[df.Station == user])# takes the row within station and matches it with the users required station
            total = 0
            period = ["2005-2006","2006-2007","2007-2008","2008-2009","2009-2010","2010-2011","2011-2012","2012-2013","2013-2014","2014-2015","2015-2016"]#makes a list with periods headers
            for i in range(0,10):# for loop to go through the list to use the headers name so that it can bring the columns data
                subtotal = (a[period[i]].sum())#adds the total of the column
                print("\n")
                print("The total amount of crimes for period "+str(period[i])+": "+str(subtotal))#Prints the total crime by specific station in that specific period
                total = total+subtotal
            print("=========================================================================================== \n")
            print("Total number of crimes: "+str(total)+"\n")#Prints the total amount of crimes ocurred in that station
            print("=========================================================================================== \n")

        elif(menuOP == "4"):#If the user to select 4
            a = (df.loc[df["Category"] == "Truck hijacking","2010-2011"])#takes the rows which has the category Truck Hijacking and the period of 2010-2011
            a = a.sum(axis = 0,skipna = True)# adds the crimes
            print("=========================================================================================== \n")
            print(str(a)+" Incidents occured involving truck hijacking were reported for the period 2010 -2011 \n")#prints out the crimes
            print("=========================================================================================== \n")

        elif(menuOP == "5"): #If the user to select 5
            a = df.loc[df["Category"]=="Arson"] #takes rows with category Arson
            b = a.loc[(a["Station"] == "Boitekong")|(a["Station"]=="Ngodwana")]#takes the row we called a and indices it with loc takes the rows which has Boitekong or Ngodwana as the stations
            c = b.loc[:,["2009-2010"]]# takes the row we indice it and take the period 2009-2010
            total = 0
            total = c.sum() # adds all the crimes in 2009-2010
            print("=========================================================================================== \n")
            print(total) # prints the total
            print("=========================================================================================== \n")

        elif(menuOP == "6"):#if the user to select 6
            a = df.loc[df["2014-2015"]==max(df["2014-2015"]),"Category"]#takes the row with the max number in the period 2014-2015 year and gets the category of it
            print("=========================================================================================== \n")
            print(a)#prints the category
            print("=========================================================================================== \n")

        elif(menuOP == "7"):#if the user to select 7
            a = df.loc[(df["Station"] == "Nongoma")&(df["Category"] == "Murder")]#takes the row with  station as Nongoma and the category murder
            Dict = {"2005-2006": a["2005-2006"].sum() ,"2006-2007": a["2006-2007"].sum(), "2007-2008":a["2007-2008"].sum(),"2008-2009":a["2008-2009"].sum(), "2009-2010":a["2009-2010"].sum(),"2010-2011":a["2010-2011"].sum(),"2010-2011": a["2010-2011"].sum(),"2011-2012":a["2011-2012"].sum(),"2012-2013":a["2012-2013"].sum(),"2013-2014": a["2013-2014"].sum(),"2014-2015": a["2014-2015"].sum(),"2015-2016": a["2015-2016"].sum()}#add all columns headet as the name for each dict name and its contents the sum of the column
            IndexYear = min(Dict, key=Dict.get)#gets the dict header with the value of the lowest number
            print("=========================================================================================== \n")
            print("\n In "+str(IndexYear)+" Nongoma recorded the lowest amount of murders \n") #prints out the year with the lowest murders
            print("=========================================================================================== \n")

        elif(menuOP == "8"):#if the user to select 8
            a = df.loc[(df["2008-2009"]== 0)&(df["Category"] == "Attempted murder")&(df["Province"] =="North West")]#takes the row with the period 2008-2009 which has 0 has a value in it and the category with attempted murder with the province being North West
            print("=========================================================================================== \n")
            print(a["Station"])# takes the rows we named a and returns only  their stations
            print("=========================================================================================== \n")

        elif(menuOP == "9"):#if the user to select 9
            Dict = {"2005-2006": df["2005-2006"].sum() ,"2006-2007": df["2006-2007"].sum(), "2007-2008":df["2007-2008"].sum(),"2008-2009":df["2008-2009"].sum(), "2009-2010":df["2009-2010"].sum(),"2010-2011":df["2010-2011"].sum(),"2010-2011": df["2010-2011"].sum(),"2011-2012":df["2011-2012"].sum(),"2012-2013":df["2012-2013"].sum(),"2013-2014": df["2013-2014"].sum(),"2014-2015": df["2014-2015"].sum(),"2015-2016": df["2015-2016"].sum()}#Adds all the columns headset of periods as name for each dict and its content contains sum of the column
            IndexYear = max(Dict, key=Dict.get)#gets the dict header with the value with the highest number
            print("=========================================================================================== \n")
            print("\n" +str(IndexYear)+" was the period with the highest amount of crimes from 2005-2006 to 2015-2016 \n")#prints the year
            print("=========================================================================================== \n")

        elif(menuOP == "10"):#if the user to select 10
            print("\n")#print a line gap
            print("Thank you")#print thank you
            break#breaks the while loop




menu()
