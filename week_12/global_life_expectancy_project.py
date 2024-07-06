country_list = []
country_codes_list = []
year_list = []
life_expectancy_list = [] 

maxlifeglobal = None
maxlifeglobalindex = None

maxlifeglobalcountry = None
maxlifeglobalyear = None

minlifeglobal = None
minlifeglobalindex = None

minlifeglobalcountry = None
minlifeglobalyear = None




YearOfInterestX = int(input('Enter the year of interest: '))

with open('Week12/life-expectancy.txt') as lifedata:
    for line in lifedata:
        splitlifedataline = line.split(',')
        country = splitlifedataline[0]
        country_list.append(country)
        country_code = splitlifedataline[1]
        country_codes_list.append(country_code)
        year = splitlifedataline[2]
        year_list.append(int(year))
        life_expectancy_inyears = float(splitlifedataline[3])
        life_expectancy_list.append(life_expectancy_inyears)
        average_global_lifespan = ((sum(life_expectancy_list)/len(life_expectancy_list)))
        earliestyear = min(year_list)
        latestyear = max(year_list)
        
    maxlifeglobal = max(life_expectancy_list)
    maxlifeglobalindex = life_expectancy_list.index(maxlifeglobal)
    
    maxlifeglobalcountry = country_list[maxlifeglobalindex]
    maxlifeglobalyear = year_list[maxlifeglobalindex]
    
    minlifeglobal = min(life_expectancy_list)
    minlifeglobalindex = life_expectancy_list.index(minlifeglobal)
    
    minlifeglobalcountry = country_list[minlifeglobalindex]
    minlifeglobalyear = year_list[minlifeglobalindex]
        
    #Now to the fun part! I know this script is very *ahem, verbose, but honestly I'm SOOOO freaking glad it works! Yeah Science!#      

    country_list_YOI = []
    country_codes_list_YOI = []
    year_list_YOI = []
    life_expectancy_list_YOI = [] 
    year_list_YOI_indicies = []
    
    average_life_expectancy_YOI = None
    
    max_life_YOI = None
    max_life_YOI_index = None

    max_life_YOI_country = None
    max_life_YOI_year = None

    min_life_YOI = None
    min_life_YOI_index = None

    min_life_YOI_country = None
    min_life_YOI_year = None
    
        
    for indexvalue in zip(year_list, country_codes_list, country_list, life_expectancy_list):
        if indexvalue[0] == YearOfInterestX:
            year_list_YOI.append(indexvalue[0])
            country_codes_list_YOI.append(indexvalue[1])
            country_list_YOI.append(indexvalue[2])
            life_expectancy_list_YOI.append(indexvalue[3])
        
    max_life_YOI = max(life_expectancy_list_YOI)
    max_life_YOI_index = life_expectancy_list_YOI.index(max_life_YOI)
    max_life_YOI_country = country_list_YOI[max_life_YOI_index]
    
    min_life_YOI = min(life_expectancy_list_YOI)
    min_life_YOI_index = life_expectancy_list_YOI.index(min_life_YOI)
    min_life_YOI_country = country_list_YOI[min_life_YOI_index]
    
    average_life_expectancy_YOI = (sum(life_expectancy_list_YOI))/(len(life_expectancy_list_YOI))
        
    print(f'\nThe overall maximum life expectancy is: {maxlifeglobal} years from {maxlifeglobalcountry} in {maxlifeglobalyear:.0f}.')   
    print(f'The overall minimum life expectancy is: {minlifeglobal} years from {minlifeglobalcountry} in {minlifeglobalyear:.0f}.') 
    print(f"\nThe average life expectancy across all time and all countries was {average_global_lifespan:.3f} years.")
    print(f'The earliest year included in our dataset is {earliestyear}.')
    print(f'The most recent year included in our dataset is {latestyear}.')
    
    print(f"\nFor the year {YearOfInterestX}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy_YOI:.3f} years.")
    print(f"The max life expectancy was in {max_life_YOI_country} with {max_life_YOI} years.")
    print(f"The min life expectancy was in {min_life_YOI_country} with {min_life_YOI} years.")
    
    
                    
        
        
        
    
    
            


    
        

    
        