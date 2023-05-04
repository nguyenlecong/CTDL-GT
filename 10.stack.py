class NganXep:
    def __init__(self):
        self.danh_sach = []

    def la_rong(self):
        # is empty
        return len(self.danh_sach) == 0

    def __str__(self):
        kq = 'Ngan Xep ['
        stt = 0
        for x in self.danh_sach:
            stt += 1
            if stt == 1:
                kq += str(x)
            else:
                kq += ' -> ' + str(x)
        kq = kq + ']'

        return kq

    def day_vao(self, gia_tri):
        # push
        self.danh_sach.insert(0, gia_tri)

    def lay_ra(self):
        # pop
        if self.la_rong():
            return None
        else:
            return self.danh_sach.pop(0)


if __name__ == "__main__":
    nganxep = NganXep()
    for i in range(1, 6):
        nganxep.day_vao(i)
        print(nganxep)

    while not nganxep.la_rong():
        gt = nganxep.lay_ra()
        print(gt)
        print(nganxep)
