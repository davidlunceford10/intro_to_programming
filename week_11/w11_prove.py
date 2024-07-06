country_list = []
country_codes_list = []
year_list = []
life_expectancy_list = [] 


YearOfInterestX = int(input('Enter the year of interest: '))

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

highest_life_expectancy = max(life_expectancy_list)
shortest_life_expectancy = min(life_expectancy_list)

YearsOfInterest = []
CountriesOfInterest = []
LifeExpectanciesOfInterest = []
minlifeYOI = None
maxlifeYOI = None

for thisline in enumerate(zip(country_list, country_codes_list, year_list, life_expectancy_list)):
    if thisline[2] == YearOfInterestX:
        YearsOfInterest.append(thisline[2])
        CountriesOfInterest.append(thisline[0])
        LifeExpectanciesOfInterest.append(thisline[3])

    for thisnextline in zip(YearsOfInterest, CountriesOfInterest, LifeExpectanciesOfInterest):
        minlifeYOI = min(thisnextline[2])
        minlifecountry = thisnextline[1]
        maxlifeYOI = max(thisnextline[2])
        maxlifecountry = thisnextline[2]
        averageYOIlifeexpectancy = (sum(LifeExpectanciesOfInterest)/len(LifeExpectanciesOfInterest))
        


 




            


       









        



          

    
        
            

            

   


        
        




# year_of_interest = int(input('Enter the year of interest: '))



        
        

        