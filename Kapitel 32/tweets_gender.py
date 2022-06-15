#----------------------------------------------------
# Dateiname:  tweets_gender.py
# Ein Pool von Prozessen bearbeitet eine große
# Datenmenge. Es wird geprüft, wie oft ein Suchwort WORD
# in den Tweets der Gendergruppe GENDER vorkommt.
#
# Python 3,  mitp Verlag
# Kap. 32
# Michael Weigend 12. 06. 2019
#----------------------------------------------------
from multiprocessing import Pool
from time import time

WORD = "car"
GENDER = ",female,"
ANSWER="""Es wurden insgesamt {} Tweets
dieser Gender-Gruppe untersucht.
Das Wort {} wurde in {:.1f} Prozent aller Tweets dieser
Gender-Gruppe gefunden.
Bearbeitungszeit: {} Sekunden."""

def search(line):
    gender_found, word_found = 0, 0
    if GENDER in line:
        gender_found += 1
        if WORD in line:
            word_found += 1
    return gender_found, word_found

if __name__ == '__main__': 
    f = open("gender-classifier.csv", encoding="utf-8")
    data = f.readlines()
    f.close()
    start = time()
    p = Pool()
    results = p.map(search, data)
    g, w = zip(*results)
    p.close()
    p.join()
    gender_count = sum(g)
    word_count = sum(w)
    print(ANSWER.format(gender_count,
                    WORD,
                    word_count/gender_count * 100,
                    time() - start))
    

    
