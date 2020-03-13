import random



# Wörter, Sonderzeichen und Zahlen aus denen die Passwörter generiert werden

wort =["hirsch","Hirsch","geweih","Geweih","Hochsitz","hochsitz","Eber","eber","deer","Deer","gold","Gold",
     "Futter","futter","Weide","weide","biber","Biber","Zaun","zaun","reh","Reh","gewehr","Gewehr","Jagd",
     "jagd","Horn","horn","Bock","bock","Hase","hase","Revier","revier","brumpft","Brumpft","Keiler","keiler",
     "Bache","bache","Dachs","dachs","fuchs","Fuchs","flinte","flinte","Eule","eule","Nacht","nacht","Tag","tag"]

sonderzeichen=["!","#","+","-","?","%","&"]

zahl = random.randint(0,9999)

sonderwahl = random.randint(0,6)

wortwahl = random.randint(0,51)

wort2wahl = random.randint(0,51)

# Ausgabe des generierten Passwort

print("Das Passwort ist: ",wort[wortwahl] + sonderzeichen[sonderwahl] + str(zahl) + wort[wort2wahl])

