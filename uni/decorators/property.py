

class Snek:
    def __init__(self, val):
        self.value =  val

    @property
    def getvalue(self):
        return self.value

obj = Snek(10)
print(obj.getvalue)

