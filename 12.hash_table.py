class BangBam:
    def __init__(self, kich_thuoc=10):
        self.danh_sach = [None for _ in range(kich_thuoc)]

    def __str__(self):
        kq = '['
        stt1 = 0
        for x in self.danh_sach:
            stt1 += 1
            if stt1 != 1:
                kq += ', '

            if x is None:
                kq += '[None]'
            else:
                kq += '['
                stt2 = 0
                for e in x:
                    stt2 += 1
                    if stt2 != 1:
                        kq += ', '
                    kq += str(e[0]) + ': ' + str(e[1])
                kq += ']'
        kq += ']'
        return kq

    def bam(self, khoa):
        kich_thuoc = len(self.danh_sach)
        return hash(khoa) % kich_thuoc

    def them(self, khoa, gia_tri):
        chi_muc = self.bam(khoa)
        if self.danh_sach[chi_muc] is None:
            # Them moi
            self.danh_sach[chi_muc] = list()
            self.danh_sach[chi_muc].append([khoa, gia_tri])
        else:
            # Cap nhat
            cap_nhat = False
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    x[1] = gia_tri
                    cap_nhat = True
                    break

            if cap_nhat == False:
                self.danh_sach[chi_muc].append([khoa, chi_muc])

    def lay(self, khoa):
        chi_muc = self.bam(khoa)
        if self.danh_sach[chi_muc] is None:
            return None
        else:
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    return x[1]

    def __setitem__(self, khoa, gia_tri):
        self.them(khoa, gia_tri)

    def __getitem__(self, khoa):
        return self.lay(khoa)


def main():
    bangbam = BangBam(5)
    import random
    for _ in range(15):
        khoa = random.randint(0, 10)
        gia_tri = random.randint(0, 100)
        # bangbam.them(khoa, gia_tri)
        bangbam[khoa] = gia_tri
        print(bangbam)

    khoa = int(input("Nhap vao mot khoa: "))
    # gia_tri = bangbam.lay(khoa)
    gia_tri = bangbam[khoa]
    print(gia_tri)


if __name__ == '__main__':
    main()
