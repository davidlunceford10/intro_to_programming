country_list = []
country_codes_list = []
year_list = []
life_expectancy_list = [] 


# YearOfInterestX = int(input('Enter the year of interest: '))

with open('Week11/life-expectancy.txt') as lifedata:
    for line in lifedata:
        splitlifedataline = line.strip().split(',')
        country = splitlifedataline[0]
        country_list.append(country)
        country_code = splitlifedataline[1]
        country_codes_list.append(country_code)
        year = splitlifedataline[2]
        year_list.append(float(year))
        life_expectancy_inyears = float(splitlifedataline[3])
        life_expectancy_list.append(life_expectancy_inyears)

for index in enumerate(zip(country_list, country_codes_list, year_list, life_expectancy_list)):
    if life_expectancy_inyears[index] > 
            
            


       





#ALE stands for Average Life Expectancy#
ALEForTheYearOfX = None

#MAXLE stands for Maximum Life Expectancy#
MAXLEForTheYearOfX = None

#MLE stands for Minimum Life Expectancy#
MLEForTheYearOfX = None





        



          

    
        
            

            

   


        
        




# year_of_interest = int(input('Enter the year of interest: '))



        
        

        