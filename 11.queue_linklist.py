from link_list_class import DSLienKet


class HangDoi:
    def __init__(self):
        self.danh_sach = DSLienKet()

    def la_rong(self):
        # is empty
        return self.danh_sach.dau == None

    def __str__(self):
        kq = self.danh_sach.in_ds()
        return kq

    def xep_hang(self, gia_tri):
        # enqueue
        self.danh_sach.them_duoi(gia_tri)

    def ra_hang(self):
        # dequeue
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()

            return kq


if __name__ == "__main__":
    hangdoi = HangDoi()
    for i in range(1, 6):
        hangdoi.xep_hang(i)
        print(hangdoi)

    while not hangdoi.la_rong():
        gt = hangdoi.ra_hang()
        print(gt)
        print(hangdoi)
