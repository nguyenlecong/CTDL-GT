from utils import san_sinh_mang_tang_dan


def tim_nhi_phan(mang, x):
    trai = 0
    phai = len(mang) - 1

    while trai <= phai:
        giua = (trai + phai) // 2

        if mang[giua] == x:
            return giua

        if x < mang[giua]:
            phai = giua - 1
        else:
            trai = giua + 1

    return -1


def main():
    mang = san_sinh_mang_tang_dan(20)
    print(mang)

    x = int(input('Nhap vao mot so nguyen can tim: '))
    vitri = tim_nhi_phan(mang, x)

    if vitri != -1:
        print(f'Gia tri {x} duoc tim thay tai vi tri {vitri}')
    else:
        print(f'Khong tim thay gia tri {x} trong mang')


if __name__ == '__main__':
    main()
