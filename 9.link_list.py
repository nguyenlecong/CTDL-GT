from link_list_class import Nut, DSLienKet


def main():
    ds = DSLienKet()

    # a- them
    ds.them(12)
    ds.them(10)

    # b - chen
    ds.chen(0, 8)
    ds.chen(1, 15)
    ds.chen(3, 17)

    # c - tim
    vt = ds.tim(99)
    print(vt)
    vt = ds.tim(15)
    print(vt)

    # d - xoa
    ds.xoa(19)
    ds.xoa(15)
    # e - cap nhat
    ds.cap_nhat(6, 23)
    ds.cap_nhat(2, 9)

    # f - xoa het
    ds.xoa_het()

    ds.in_ds()


if __name__ == '__main__':
    main()
