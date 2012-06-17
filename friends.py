#Bis ich den Mist mit OOP hinbekomme, erstmal hier meine Library...
#wir tun jetzt einfach so, als ob wir oop haetten.

##Init-Funktion:
## es muss eine Datei friendlist_me.txt vorliegen.
## Freundesliste muss die Freunde mit Newlines trennen...
## erstellt eine Freundeslist anhand eines Namens
## @param me: Mensch, dessen Liste erstellt werden soll.
## return: neu erstellte Freundeliste.
def init(me):
    file="friendlist_"+me+".txt"
    try:
        with open(file,"r") as f:
            friends = f.read().lower().split("\n")
            best_friends = friends[0:2]
        return[friends,best_friends]
    except IOError:
        print "Datei existiert nicht."
        exit()
    
def is_friend(friend, friends):
    if friend in friends:
        return True
    else:
        return False
        
def is_best_friend(friend, best_friends):
    if friend in best_friends:
        return True
    else:
        return False
        
def get_commons_list(lista, listb):
    lista = set(lista)
    listb = set(listb)
    commons_list=list(lista & listb)
    return commons_list

def get_unique_list(lista, listb):
    lista = set(lista)
    listb = set(listb)
    unique_list = list(listb - lista)
    return unique_list