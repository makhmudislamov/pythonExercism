

def convert(number):
   
    pling = number % 3
    plang = number % 5
    plong = number % 7

    if pling == 0 and plang == 0 and plong == 0:
        return("PlingPlangPlong")
    elif pling == 0 and plang == 0:
        return("PlingPlang")
    elif plang == 0 and plong == 0:
        return("PlangPlong")
    elif pling == 0 and plong == 0:
        return("PlingPlong")
    elif pling == 0:
        return("Pling")
    elif plang == 0:
        return("Plang")
    elif plong == 0:
        return("Plong")
    else:
        return(str(number))



