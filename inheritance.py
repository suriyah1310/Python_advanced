class Family:
    def son(self):
        print('Son is happy')


class Mother(Family):
    pass


class Daughter(Family):
    def daufriend(self):
        print('Sonia')


output = Mother()
output.son()
daughter1 = Daughter()
daughter1.daufriend()

