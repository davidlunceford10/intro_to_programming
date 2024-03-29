country_list = []
country_codes_list = []
year_list = []
life_expectancy_list = [] 


with open('Week11/life-expectancy.txt') as lifedata:
    for line in lifedata:
        splitlifedataline = line.strip().split(',')
        country = splitlifedataline[0]
        country_list.append(country)
        country_code = splitlifedataline[1]
        country_codes_list.append(country_code)
        year = splitlifedataline[2]
        year_list.append(year)
        life_expectancy_inyears = splitlifedataline[3]
        life_expectancy_list.append(life_expectancy_inyears)

    highest_life_expectancy = max(life_expectancy_list)
    shortest_life_expectancy = min(life_expectancy_list)

YearOfInterestX = int(input('Enter the year of interest: '))

#ALE stands for Average Life Expectancy
ALEForTheYearOfX = None

#MAXLE stands for Maximum Life Expectancy
MAXLEForTheYearOfX = None

#MLE stands for Minimum Life Expectancy
MLEForTheYearOfX = None

if YearOfInterestX == year_list:
    for index in zip(enumerate )

for index in year_list:
    if YearOfInterestX == index:
        


          

    
        
            

            

   


        
        




# year_of_interest = int(input('Enter the year of interest: '))



        
        

        