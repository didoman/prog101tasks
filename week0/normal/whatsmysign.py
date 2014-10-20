# what's my sign
import datetime

def what_is_my_sign(day, month):
    aries_startdate = datetime.date(200, 3, 21)
    aries_enddate = datetime.date(200, 4, 20)

    taurus_startdate = datetime.date(200, 4, 21)
    taurus_enddate = datetime.date(200, 5, 21)

    gemini_startdate = datetime.date(200, 5, 22)
    gemini_enddate = datetime.date(200, 6, 21)
    
    cancer_startdate = datetime.date(200, 6, 22)
    cancer_enddate = datetime.date(200, 7, 22)
    
    leo_startdate = datetime.date(200, 7, 23)
    leo_enddate = datetime.date(200, 8, 22)
    
    virgo_startdate = datetime.date(200, 8, 23)
    virgo_enddate = datetime.date(200, 9, 23)
    
    libra_startdate = datetime.date(200, 9, 24)
    libra_enddate = datetime.date(200, 10, 23)
    
    scorpio_startdate = datetime.date(200, 10, 24)
    scorpio_enddate = datetime.date(200, 11, 22)
    
    sagittarius_startdate = datetime.date(200, 11, 23)
    sagittarius_enddate = datetime.date(200, 12, 21)
    
    capricorn_startdate = datetime.date(200, 12, 22)
    capricorn_enddate = datetime.date(200, 1, 20)
    
    aquarius_startdate = datetime.date(200, 1, 21)
    aquarius_enddate = datetime.date(200, 2, 19)
    
    pisces_startdate = datetime.date(200, 2, 20)
    pisces_enddate = datetime.date(200, 3, 20)
    
    birth = datetime.date(200, month, day)

    if birth >= aries_startdate and birth <= aries_enddate:
        print("aries")
    elif birth >= taurus_startdate and birth <= taurus_enddate:
        print("taurus")
    elif birth >= gemini_startdate and birth <= gemini_enddate:
        print("gemini")
    elif birth >= cancer_startdate and birth <= cancer_enddate:
        print("cancer")
    elif birth >= leo_startdate and birth <= leo_enddate:
        print("leo")
    elif birth >= virgo_startdate and birth <= virgo_enddate:
        print("virgo")
    elif birth >= libra_startdate and birth <= libra_enddate:
        print("libra")
    elif birth >= scorpio_startdate and birth <= scorpio_enddate:
        print("scorpio")
    elif birth >= sagittarius_startdate and birth <= sagittarius_enddate:
        print("sagittarius")
    elif birth >= capricorn_startdate and birth <=  datetime.date(200,12,31):
        print("capricorn")
    elif birth >= datetime.date(200,1,1) and birth <= capricorn_enddate:
        print("capricorn")
    elif birth >= aquarius_startdate and birth <= aquarius_enddate:
        print("aquarius")
    elif birth >= pisces_startdate and birth <= pisces_enddate:
        print("pisces")
    else: 
        print("i have no idea, maybe you are mother of dragons")

what_is_my_sign(5, 8)
what_is_my_sign(29, 1)
what_is_my_sign(30, 6)
what_is_my_sign(31, 5)
what_is_my_sign(2, 2)
what_is_my_sign(8, 5)
what_is_my_sign(9, 1)
