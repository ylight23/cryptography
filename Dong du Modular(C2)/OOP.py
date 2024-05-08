class Car:
    loaixe="Oto"
    def __init__(self, tenxe, mauxe ,nguyenlieu):
        self.tenxe = tenxe
        self.mauxe=mauxe
        self.nguyenlieu=nguyenlieu
    def mucdich(self):
        print("{} chay bang {}".format(self.tenxe,self.nguyenlieu))
toyota=Car("Toyota","mauden","xang")
lambor=Car("Lambo"," maudo","dầu")    
huyndai=Car("Huyndai","mautrang","diesel")

# print("Toyota la",Car.loaixe)
# print("Lambo la",Car.loaixe)
# print("Huyndai la",Car.loaixe)

# print("{} co mau xe {} chay bang {}".format(toyota.tenxe,toyota.mauxe,toyota.nguyenlieu))
# print("{} co mau xe {} chay bang {}".format(huyndai.tenxe,huyndai.mauxe,huyndai.nguyenlieu))
# print("{} co mau xe {} chay bang {}".format(lambor.tenxe,lambor.mauxe,lambor.nguyenlieu))

# print("{} {} {}".format(huyndai.tenxe,lambor.mauxe,toyota.nguyenlieu))
# print("{}".format(toyota.__class__.loaixe))#dit me 2 cach deu oke
# print("{}".format(Car.loaixe))

class Toyota(Car):
    def __init__(self, tenxe, mauxe, nguyenlieu,giatien):
        super().__init__(tenxe, mauxe, nguyenlieu)
        self.giatien=giatien
    def chayxe(self):
        print("{} dang chay xe".format(self.tenxe))
    def mucdich(self):
        print("{} chay bang {}".format(self.tenxe,self.nguyenlieu))
        print("{} co mau xe la mau {}".format(self.tenxe, self.mauxe))
a=Toyota("Yaris","den","xang","14")
b=Toyota("Vios","do","dau","16")
a.chayxe()
b.mucdich()