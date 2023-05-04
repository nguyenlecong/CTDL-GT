class Nut:
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None

    def chen(self, khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return

        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)

        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa)
        else:
            print(f'Bi trung khoa {khoa}')


class CayNhiPhanTimKiem:
    def __init__(self, khoa=None):
        if khoa == None:
            self.goc = None
        else:
            self.goc = Nut(khoa)

    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:
            self.goc.chen(khoa)

    def xoa(self, khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc

        while nut_ht != None:
            if nut_ht.khoa > khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.trai
                cha_con = 'trai'
            elif nut_ht.khoa < khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con = 'phai'
            else:
                # Tim thay
                if nut_cha == None:
                    # Xoa nut goc
                    if nut_ht.trai == None and nut_ht.phai == None:
                        # Xoa nut goc khong co con
                        self.goc = None
                    elif nut_ht.trai == None:
                        # Xoa nut goc chi co con phai
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        # Xoa nut goc chi co con trai
                        self.goc = nut_ht.trai
                    else:
                        # Xoa nut goc co du 2 con
                        # Xoay "trai"
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:
                            tam = tam.trai

                        tam.trai = nut_ht.trai

                elif nut_ht.trai == None and nut_ht.phai == None:
                    # Xoa nut la
                    if cha_con == 'trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                elif nut_ht.trai == None:
                    # Xoa nut chi co con phai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.trai
                elif nut_ht.phai == None:
                    # Xoa nut chi co con trai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai = nut_ht.phai
                else:
                    # Xoa nut co du 2 con
                    # Xoay "trai"
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai

                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else:
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai

                        tam.trai = nut_ht.trai

                    del nut_ht
                    break

    def duyet_trai_phai_nut(self, goc=0):
        # Duyet theo LRN
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc

        if nut_ht == None:
            return []
        else:
            kq = []

            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)

            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)

            kq.append(nut_ht.khoa)

            return kq

    def tim(self, khoa):
        if self.goc == None:
            return

        nut_ht = self.goc
        kq = ''
        while nut_ht != None and nut_ht.khoa != khoa:
            kq += f'{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai

        if nut_ht == None:
            return None
        else:
            kq += f'{nut_ht.khoa}'
            return kq


def main():
    cay = CayNhiPhanTimKiem()

    tap_gia_tri = [66, 46, 84, 11, 81, 99, 36, 77, 83, 87, 100, 86, 85]
    for x in tap_gia_tri:
        cay.chen(x)

    kq = cay.duyet_trai_phai_nut()
    print(kq)

    kq = cay.tim(77)
    print(kq)

    cay.xoa(84)
    kq = cay.duyet_trai_phai_nut()
    print(kq)

    kq = cay.tim(77)
    print(kq)


if __name__ == '__main__':
    main()
