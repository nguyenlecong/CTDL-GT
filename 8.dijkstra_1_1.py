import math


def tao_do_thi_co_huong_tu_tap_tin():
    f = open('do_thi_co_huong.txt')
    so_dinh = int(f.readline().strip())
    cac_canh = f.readlines()
    f.close()

    dt = [[0 for _ in range(so_dinh)] for _ in range(so_dinh)]

    for canh in cac_canh:
        canh = canh.strip()
        ds_gia_tri = canh.split()
        if len(ds_gia_tri) != 3:
            continue

        dong = int(ds_gia_tri[0])
        cot = int(ds_gia_tri[1])
        khoang_cach = int(ds_gia_tri[2])

        dt[dong][cot] = khoang_cach

    return dt


def duong_di(ds_dinh_truoc, dinh_dich):
    ds = [dinh_dich]
    dinh = dinh_dich
    while True:
        dinh = ds_dinh_truoc[dinh]
        if dinh == None:
            break

        ds.insert(0, dinh)

    ds = [str(x) for x in ds]

    return '->'.join(ds)


def khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat):
    nho_nhat = math.inf
    dinh_nho_nhat = math.inf
    for dinh in range(len(ds_khoang_cach)):
        if ds_khoang_cach[dinh] < nho_nhat and ds_dinh_cay_ngan_nhat[dinh] == False:
            nho_nhat = ds_khoang_cach[dinh]
            dinh_nho_nhat = dinh

    return dinh_nho_nhat


def dijkstra(do_thi, dinh_nguon, dinh_dich):
    so_luong_dinh = len(do_thi)
    ds_khoang_cach = [math.inf] * so_luong_dinh
    ds_khoang_cach[dinh_nguon] = 0
    ds_dinh_cay_ngan_nhat = [False] * so_luong_dinh
    ds_dinh_truoc = [None] * so_luong_dinh

    for _ in range(so_luong_dinh):
        x = khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat)
        if x == math.inf:
            print(
                f'Khong co duong di tu dinh {dinh_nguon} den dinh {dinh_dich}')
            return

        ds_dinh_cay_ngan_nhat[x] = True
        if x == dinh_dich:
            print(
                f'Tim thay duong di tu donh {dinh_nguon} den dinh {dinh_dich}')
            duongdi = duong_di(ds_dinh_truoc, dinh_dich)

            noi_dung = f'Tu dinh {dinh_nguon} den dinh {dinh_dich}: '
            noi_dung += duong_di(ds_dinh_truoc, dinh_dich) + ": "
            noi_dung += str(ds_khoang_cach[dinh_dich])
            print(noi_dung)

            return
        else:
            for y in range(so_luong_dinh):
                if do_thi[x][y] > 0 and ds_dinh_cay_ngan_nhat[y] == False and ds_khoang_cach[y] > ds_khoang_cach[x]+do_thi[x][y]:
                    ds_khoang_cach[y] = ds_khoang_cach[x] + do_thi[x][y]
                    ds_dinh_truoc[y] = x


def main():
    do_thi = tao_do_thi_co_huong_tu_tap_tin()
    dinh_nguon = int(input('Nhap dinh nguon: '))
    dinh_dich = int(input('Nhap dinh dich: '))

    if dinh_nguon in range(len(do_thi)) and dinh_dich in range(len(do_thi)):
        dijkstra(do_thi, dinh_nguon, dinh_dich)
    else:
        print('Nhap sai')


if __name__ == '__main__':
    main()
