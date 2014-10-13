#  Wzorowane na przyk??adzie Rona Zacharskiego
#

from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    """Oblicz odleg??o???? w metryce taks??wkowej mi??dzy dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwr???? -1, gdy zbiory nie maj?? wsp??lnych element??w"""
    print (rating1)
    # TODO: wpisz kod
    klucze1=rating1.keys()
    klucze2=rating2.keys(),
    odleglosc = 0
    for klucz in klucze1:
        if klucz in rating2.keys():
            # print (rating2[klucz])
            odleglosc = odleglosc +abs(rating2[klucz]-rating1[klucz])
        else:
            print(-1)
        pass
    return odleglosc

odlegloscODAniDoHeli = manhattan(users ["Ania"], users ["Hela"])
print ("OD Ani do Heli jest %f" % odlegloscODAniDoHeli )

def computeNearestNeighbor(username, users):
    """dla danego u??ytkownika, zwr???? list?? innych u??ytkownik??w wed??ug blisko??ci preferencji"""
    distances = []
    # TODO: wpisz kod
    return distances

def recommend(username, users):
    """Zwr???? list?? rekomendacji dla u??ytkownika"""
    # znajd?? preferencje najbli??szego s??siada
    # nearest = computeNearestNeighbor(username, users)[0][1]

    # recommendations = []
    # zarekomenduj u??ytkownikowi wykonawc??, kt??rego jeszcze nie oceni??, a zrobi?? to jego najbli??szy s??siada
    # TODO: wpisz kod
    # using the fn sorted for variety - sort is more efficient
    # return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# przyk??ady

print( recommend('Hela', users))
#print( recommend('Celina', users))
