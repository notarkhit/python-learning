class Snek:
    count = 2
    @classmethod
    def jump(cls):
        cls.count = cls.count +(cls.count * 2)

print(Snek.count)
Snek.jump()
print(Snek.count)
Snek.jump()
Snek.jump()
print(Snek.count)
