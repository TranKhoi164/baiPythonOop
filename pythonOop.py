class Hinh:
    def __init__(self, s):
        self.s = s
    def chuvi(self):
        return('chu vi:')
    def dientich(self):
        return('dien tich:')
    
class TamGiacDeu(Hinh):
    def chuvi(self):
        return 3*self.s
    def dientich(self):
        return 0.5*(self.s*(3**0.5)*0.5)*self.s
    
class HinhVuong(Hinh):
    def chuvi(self):
        return 4*self.s
    def dientich(self):
        return self.s**2
    
class LucGiacDeu(Hinh):
    def chuvi(self):
        return 6*self.s
    def dientich(self):
        return self.s**2*(3**0.5)*0.25
class NguGiacDeu(Hinh):
    def chuvi(self):
        return 5*self.s
    def dientich(self):
        return (self.s**2*(3**0.5)/4)*5
    

class BatGiacDeu(Hinh):
    def chuvi(self):
        return 8*self.s
    def dientich(self):
        return 2*(1+2**0.5)*self.s**2
    
class HinhTron(Hinh):
    def chuvi(self):
        return 2*3.14*self.s
    def dientich(self):
        return 3.14*self.s**2

class KhoiTru:
    def __int__(self,hinh,h):
        self.hinh = hinh
        self.h = h
    def thetich(self):
        return self.hinh.thetich()*self.h

hinhVuong= HinhVuong(5)
hinhTron = HinhTron(2)
tamGiacDeu = TamGiacDeu(4)
lucGiacDeu = LucGiacDeu(4)
nguGiacDeu = NguGiacDeu(4)
batGiacDeu = BatGiacDeu(4)

print(f'Chu vi hình vuông: {hinhVuong.chuvi()}',f',Diện tích hình vuông: {hinhVuong.dientich()}')
print(f'Chu vi hình tròn: {hinhTron.chuvi()}',f',Diện tích hình tròn: {hinhTron.dientich()}')
print(f'Chu vi tam giác đều: {tamGiacDeu.chuvi()}',f',Diện tích tam giác đều: {tamGiacDeu.dientich()}')
print(f'Chu vi lục giác đều: {lucGiacDeu.chuvi()}',f',Diện tích lục giác đều: {lucGiacDeu.dientich()}')
print(f'Chu vi ngũ giác đều: {nguGiacDeu.chuvi()}',f',Diện tích ngũ giác đều: {nguGiacDeu.dientich()}')
print(f'Chu vi bát giác đều: {batGiacDeu.chuvi()}',f',Diện tích bát giác đều: {batGiacDeu.dientich()}')