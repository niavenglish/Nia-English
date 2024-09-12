import datetime

def get_birthdate():
    while True:
        # Allows the user to enter their birthday in the format below
        birthdate_str = input("Enter a birthdate (YYYY-MM-DD), or 'exit' to quit: ")
        #Gives the user the option to exit
        if birthdate_str.lower() == 'exit':
            return None
        
        try:
            birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
            return birthdate #return the bithdate
        except ValueError:
            print("Invalid birthdate format. Please use YYYY-MM-DD.") #Error message incase format is incorrect
#Calculate the user sign based upon the users birthday
def calculate_zodiac_sign(birthdate):
    zodiac_signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini",
                    "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]
    #Calculate the users sign based upon the users birth month
    return zodiac_signs[(birthdate.month - 1) // 2]
#Get the horoscope
def get_horoscope(sign):
    horoscopes = {
        #Each horoscope for each sign
        "Aries": "You will experience new beginnings and opportunities today.",
        "Taurus": "Focus on stability and practical matters in your life.",
        "Gemini": "Communication will be key to your success today.",
        "Cancer": "Embrace your intuition and emotions in your decision-making.",
        "Leo": "Your charisma and leadership qualities will shine today.",
        "Virgo": "Attention to detail will lead to success in your tasks.",
        "Libra": "Balance and harmony will be essential for your day.",
        "Scorpio": "Transformation and self-discovery are highlighted today.",
        "Sagittarius": "Adventure and exploration will bring you joy.",
        "Capricorn": "Your hard work and determination will pay off.",
        "Aquarius": "Innovation and social connections will be rewarding today.",
        "Pisces": "Trust your intuition and creativity in your endeavors."
    }
    
    return horoscopes.get(sign, "Invalid sign.") if sign else "Invalid input."
#Main function
def main():
    print("Welcome to Horoscope Generator!")
    
    while True:
        #Get the birthdate of the user
        birthdate = get_birthdate()
        
        if birthdate is None:
            print("Exiting the program. Goodbye!")
            break
        #Calculate the zodiac for the certain birthdate and get the horoscope for the sign
        sign = calculate_zodiac_sign(birthdate)
        horoscope = get_horoscope(sign)
        #Print the horoscope for the birthdate and zodiac sign
        print(f"The horoscope for {birthdate.strftime('%B %d, %Y')} (zodiac sign: {sign}):")
        print(horoscope)
#Making sure things are being ran the right way
if __name__ == "__main__":
    main() #Main function