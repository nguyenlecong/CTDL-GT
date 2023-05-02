import random


def san_sinh_mang(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(-100, 100)
        mang.append(so_ngau_nhien)

    return mang


def tim_tuyen_tinh(mang, x):
    n = len(mang)
    for i in range(n):
        if mang[i] == x:
            return i

    return -1


def main():
    mang = san_sinh_mang(20)
    print(mang)

    x = int(input('Nhap vao mot so nguyen can tim: '))
    vitri = tim_tuyen_tinh(mang, x)

    if vitri != -1:
        print(f'Gia tri {x} duoc tim thay tai vi tri {vitri}')
    else:
        print(f'Khong tim thay gia tri {x} trong mang')


if __name__ == '__main__':
    main()
