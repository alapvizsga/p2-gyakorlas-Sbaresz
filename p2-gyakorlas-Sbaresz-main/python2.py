#--------------------------
'''
    A parosok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páros számait tartalmazza.
'''



#--------------------------
''' 
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''
def osszeg(a):
    if ([] == a):
        return 0
    
    osszeg = 0 
    for szam in a:
        osszeg += szam
    
    return osszeg


#--------------------------
'''
    A benne_van_a_stringben nevű függvény.
    első paraméterként egy stringet kap,
    második paraméterként egy betüt.
    Visszatérési értéke True, ha  a betü benne van a stringben.
    A visszatérési érték False, ha  a betü nics benne a stringben.
'''



#--------------------------
'''
    A kereses_a_listaban nevű függvény.
    Első bemeneti paraméter egy lista,
    második bemeneti paraméter egy szám.
    A visszatérési érték a paraméterként megadott szám
        első előfordulási helye a listában.
    
    A visszatérési érték None, ha a szám nics benne a listában.
'''



#--------------------------
''' 
    Az utolso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér az adott string utolso karakterével.
    
    Üres string esetén None a visszatérési érték.
'''



#--------------------------
'''
    A benne_van_a_listaban nevű függvény,
    első paraméterként egy listát kap,
    második paraméterként egy számot.
    A visszatérési érték True, ha  a szám benne van a listában.
    A visszatérési érték False, ha  a szám nics benne a listában.
    
    Üres lista esetén a visszatérési érték False.
'''



#--------------------------
''' 
    A parosok_szama  nevű függvény,
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
''' 
    A legnagyobb  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legnagyobb számával.
    Üres lista esetén None a visszatérési érték.

    A feladat megoldása során nem használhatod a max függvényt!
'''



#--------------------------
'''
    A kereses_a_stringben nevű függvény,
    első paraméterként egy sztringet kap,
    második paraméterként egy betüt.
    Visszatérési érték a paraméterként megadott betü
        első előfordulási helye a stringben. 
    
    A visszatérési érték None, ha a betü nics benne a stringben.
'''



#--------------------------
''' 
    A pozitivok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista pozitív számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
''' 
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def elso_karakter(szoveg):
    if(szoveg == ""):
        return None
    
    return szoveg[0]



#--------------------------
'''
    A paratlanok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páratlan számait tartalmazza.
'''



#--------------------------
''' 
    A legkisebb nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legkisebb számával.
    Üres lista esetén None a visszatérési érték.
    
    A feladat megoldása során nem használhatod a min() függvényt!
'''



#--------------------------
''' 
    A negativok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista negativ számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
''' 
    A pozitivok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        pozitiv számait tartalmazza. 
'''
def negativok_kivalogatasa(lista):
    neg = []
    for szam in lista:
        if (szam < 0):
            neg.append(szam)
        
    return neg


#--------------------------
'''
    A faktorialis nevű függvény,
    visszatér a paraméterként megkapott szám faktoriálisával.
'''



#--------------------------
''' 
    A szorzat  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak szorzatával.
    
    Üres lista esetén 1 a visszatérési érték.
'''



#--------------------------
''' 
    A lista_atlag nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak átlagával.
'''
def lista_atlag(lista):
    if(lista == []):
        return 0

    osszeg  = 0
    for szam in lista:
        osszeg += szam

    return osszeg / len(lista)

#--------------------------
'''
    A negativok_kivalogatasa nevű függvény,
    visszatér egy listával, 
      amely a paraméterként átadott számokat tartalmazó lista
      negatív számait tartalmazza.
'''



#--------------------------
''' 
    A paratlanok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#======================================================================================================================/home/tanulok/stemar9559/Asztal/feladatszarok/2025 márc/p2-gyakorlas-Sbaresz-main