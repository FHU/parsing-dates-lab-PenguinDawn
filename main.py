#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT


#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    #sub
    listing = user_string.split()
    print(listing)
    
    #month here
    dictOfMonth = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    part1 = dictOfMonth[listing[0]]

    #days
    listing2 = listing[1]
    part2 = ""
    if len(listing2) == 3:
        part2 = listing2[0:2]
    elif len(listing2) == 2:
        part2 = "0"
        part2 += listing2[0]

    #year
    part3 = listing[2]

    end = part1 + "/" + part2 + "/" + part3
    return end

    

#Here
if __name__ == '__main__':
    user_str = input()
    while user_str != "-1":
        print(parse_date(user_str))
        user_str = input()
        