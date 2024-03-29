country_list = []
country_codes_list = []
year_list = []
life_expectancy_list = [] 


with open('Week12/life-expectancy.txt') as lifedata:
    for line in lifedata:
        splitlifedataline = line.strip().split(',')
        country = splitlifedataline[0]
        country_list.append(country)
        country_code = splitlifedataline[1]
        country_codes_list.append(country_code)
        year = splitlifedataline[2]
        year_list.append(int(year))
        life_expectancy_inyears = splitlifedataline[3]
        life_expectancy_list.append(life_expectancy_inyears)

highest_life_expectancy = max(life_expectancy_list)
shortest_life_expectancy = min(life_expectancy_list)


YearOfInterestX = int(input('Enter the year of interest: '))


with open("Week12/life-expectancy.txt") as CountryLifeInfo:
    for line in CountryLifeInfo:

        parts = line.split(",")

        country = parts[0].strip()

        CountryCode = parts[1]

        year = int(parts[2])

        LifeExpectancy = float(parts[3])

       
        if year == YearOfInterestX:
            for line in CountryLifeInfo:

            


        
                

                       

            

        