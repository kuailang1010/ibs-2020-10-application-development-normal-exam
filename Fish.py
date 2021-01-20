class Fish:

    def __init__(self, name, weight, color):

        self.name = name
        self.weight = weight
        self.color = color


class Clownfish(Fish):

    def __init__(self, name, weight, color, color_of_stripes):
        super().__init__(name, weight, color)
        self.color_of_stripes = color_of_stripes
        self.fishtype = "Clownfish"

    def status(self):
        return f'{self.name}, weight: {self.weight}, color: {self.color}, color_of_strip: {self.color_of_stripes}'

    def feed(self):
        self.weight += 1


class Tang(Fish):

    def __init__(self, name, weight, color):
        super().__init__(name, weight, color)
        self.fishtype = "Tang"

    def status(self):
        return f'{self.name}, weight: {self.weight}, color: {self.color}, short-term memory loss: true'

    def feed(self):
        self.weight+= 1


class Kong(Fish):

    def __init__(self, name, weight, color):
        super().__init__(self, name, weight, color)
        self.fishtype = "Kong"

    def status(self):
        return f'{self.name}, weight: {self.weight}, color: {self.color}'

    def feed(self):
        self.weight += 2


class Aquarium():

    def __init__(self, fishlist=[]):
        self.fishlist = fishlist

    def addfish(self, fishname):
        self.fishlist.append(fishname)

    def feed(self):

        for fish in self.fishlist:
            if fish.fishtype == "Kong":
                fish.weight += 2

            else:
                fish.weight += 1

    def removefish(self):

        for fish in self.fishlist:
            if fish.weight >= 11:
                self.fishlist.remove(fish)

    def getstatus(self):

        for fish in self.fishlist:
            print(fish.status)









