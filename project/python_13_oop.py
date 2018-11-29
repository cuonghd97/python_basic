class Nguoi:
    def __init__(self, ten='Nguyen Van A', gioi_tinh='Nam', tuoi=18):
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.__tuoi = tuoi

    # string return when use str()
    def __str__(self):
        return "{} - {} - {}".format(self.ten, self.gioi_tinh, self.__tuoi)

    def di(self):
        print('Nguoi di')

    @staticmethod
    def __bay():
        print('bay')


class HocSinh(Nguoi):
    def __init__(self, ten="Hoc sinh A", gioi_tinh='Nu', tuoi='18', truong='Ngo Si Lien', lop="12A9"):
        Nguoi.__init__(self, ten, gioi_tinh, tuoi)
        self.truong = truong
        self.__lop = lop

    def di(self):
        print('Hoc sinh di')

    def hoc(self):
        print('Hoc sinh hoc')


class ConNgua:
    hinh_dang = 'Cao'
    chan = 'Dai'
    bay = True

    def __init__(self, gioi_tinh='Duc'):
        self.gioi_tinh = gioi_tinh

    def chay(self):
        print('Nhanh')

    def __m


class ConLua:
    hinh_dang = 'Thap'
    chan = 'Ngan'
    boi = True

    def __init__(self, gioi_tinh='Cai'):
        self.gioi_tinh = gioi_tinh

    def chay(self):
        print('Cham')


class ConLa(ConNgua, ConLua):
    pass



if __name__ == '__main__':
    ng1 = Nguoi()
    ng1._Nguoi__bay()
    hs1 = HocSinh()
    hs1._Nguoi__bay()
    sv1 =SinhVien()
