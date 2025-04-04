#write functions here, don't add input('') statements here!
def get_day_of_the_week (day):
    
    if 1 <= day <=7:

        if (day == 1):
            result = "Monday"
            return result 
        
        elif (day == 2):
            result = "Tuesday"
            return result
        
        elif (day == 3):
            result = "Wednesday"
            return result
        
        elif (day == 4):
            result = "Thursday"
            return result
        
        elif (day == 5):
            result = "Friday"
            return result
        
        elif (day == 6):
            result = "Saturday"
            return result 
        
        elif (day == 7):
            result = "Sunday"
            return result
        
    else: return "Invalid number"

        