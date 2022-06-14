#----------------------------------------------------
# Dateiname:  sort.py 
# Sortieren durch direkte Auswahl und
# Testen mit dem Profiler
# 
# Python 3
# Kap. 25
# Michael Weigend 08.06.2019
#----------------------------------------------------

# sort.py
def sort (s):
    """Sortieren durch direkte Auswahl"""
    unsortiert = s[:]
    sortiert = []
    while unsortiert:
        x = min(unsortiert)
        sortiert.append(x)
        unsortiert.remove(x)
    return sortiert
        

if __name__ == "__main__":              #1
    import random, profile
    s = [random.randint(0,1000) for i in range(10000)]

    profile.run("sort(s)")  
