import friends as f
##########################
# 1.1: 
# Eigene Liste frei waehlbar(vgl Funktion initialize)
#
# 1.1.1: 
# add_friend und add_best_friend durch append()-Methoden ersetzt.
# Sauberer Code ist sauber.
#
# 1.2:
# Struktur umgebaut: Sind nun 2 verschiedene Funktionen
##########################

def initialize():
    print "[Vorbereitung...]"
    me=raw_input("Wie heisst du?")
    print"[Lade Freundesliste friendlist_"+me+".txt"
    init_list=f.init(me)
    print["...geladen!"]
    return init_list


print "\n"
print "[Hauptmenue]"
print "Was willst du wissen?"
print "Wie viele Freunde habe ich?(0)" 
print "Ist ____ ein Freund von mir?(1)"
print "Vergleiche mich mit ____ (2)"
input = int(raw_input("Gebe deine Auswahl (zwischen 0 und 2) ein."))
menu(init_list, input)

#%TODO%: Think about cooler Structure.
def menu(init_list, input):
    if input == 0:
        print "Du hast derzeit %s Freunde"%(len(init_list[0]))
        print "Davon gehhoeren %s zu deinen besten Freunden."%(len(init_list[1]))
    
    else if input == 1:
        person=raw_input("Gib den Namen der Person ein...")
        person= person.lower()
        if f.is_friend(person, init_list[0]):
            print person+" ist ein Freund von dir."
            if f.is_best_friend(person, init_list[1]):
                print person+"ist auch ein bester Freund."
        else:
            print person+" ist kein Freund von dir."
            if raw_input("Willst du ihn hinzufuegen?").lower().startswith("j"):
                init_list[0].append(person)#=f.add_friend(person,init_list[0])
                # print "Freund hinzugefuegt. Du hast nun %s Freunde." %(len(init_list[0]))
                # print "Davon sind %s beste Freunde."%(len(init_list[1]))
                if raw_input("Ist "+person+" auch ein bester Freund?").lower().startswith("j")
                    init_list[1].append(person)#=f.add_friend(person, init_list[1])
                print "Freund hinzugefuegt. Du hast nun %s Freunde." %(len(init_list[0]))
                print "Davon sind %s beste Freunde."%(len(init_list[1]))
                else:
                    main(init_list)
            else:
                main(init_list)

    else if input == 2:
    
        name=raw_input("Gib bitte den Namen ein...")
        name_list=f.init(name)
        common_friends=f.get_commons_list(init_list[0],name_list[0])
        common_friends_best=f.get_commons_list(init_list[1],name_list[0])
        print name+"hat %s Freunde, Du hast %s Feunde."%(len(init_list[0]),len(name_list[0]))
        print "Ihr habt %s Freunde gemeinsam."%(len(common_friends))
        print "%s deiner Freunde sind beste Freunde von "+Person %(len(common_friends_best))
        print "Folgende Freunde von "+Person+" sind noch keine Freunde von dir:"
        print f.get_unique_list(name_list[0],init_list[0])