from link_list_class import DSLienKet


class NganXep:
    def __init__(self):
        self.danh_sach = DSLienKet()

    def la_rong(self):
        # is empty
        return self.danh_sach.dau == None

    def __str__(self):
        kq = self.danh_sach.in_ds()
        return kq

    def day_vao(self, gia_tri):
        # push
        self.danh_sach.chen(0, gia_tri)

    def lay_ra(self):
        # pop
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()

            return kq


if __name__ == "__main__":
    nganxep = NganXep()
    for i in range(1, 6):
        nganxep.day_vao(i)
        print(nganxep)

    while not nganxep.la_rong():
        gt = nganxep.lay_ra()
        print(gt)
        print(nganxep)
