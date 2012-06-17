class Freundesliste(object):
    def __init__(self):
        self.__friends = []
        self.__best_friends = []
    def zusammenbauen(self, me):
        listenname= "friendlist_"+me+".txt"
        with open(listenname,"r") as f:
            self.__friends=f.read().lower().split("\n")
            self.__best_friends=self.__friends[0:2]
    def add_friend(self,friend):
        if friend in self.__friend :
            return False
        else:
            self.__friends=__friends.append(friend)
            return True
    def add_best_friend(self,friend):
        if friend.lower() in self.__best_friends:
            return False
        else:
            self.__best_friends = __best_friends.append(friend.lower())
            return True
    def get_friends(self):
        return self.__friends
    def get_best_friends(self):
        return self.__best_friends
    def is_friend(self,friend):
        if friend in self.__friends:
            return True
            