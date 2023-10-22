class Bottle:

    def __init__(self):
        self.bottle_capacity = 10

    def showInfoBottle(self, minL, maxL):
        min_liquid_level = float(self.bottle_capacity * (minL / 100))
        max_liquid_level = float(self.bottle_capacity * (maxL / 100))
        for i in range(self.bottle_capacity, 0, -1):
            if min_liquid_level <= i <= max_liquid_level:
                if i:
                    print(" |@@|")
                else:
                    print(" |  |")
            else:
                if max_liquid_level > i:
                    print((" |XX|"))
                else:
                    print(" |  |")
        print("------")

