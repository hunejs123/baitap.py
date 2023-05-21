def them_nhan_vien(danh_sach_nhan_vien):
    ten = input("Nhập tên nhân viên:")
    dia_chi = input("Nhập địa chỉ nhân viên:")
    so_dien_thoai = input("Nhập số điện thoại nhân viên:")
    nhan_vien = {
        "Tên": ten,
        "Địa chỉ": dia_chi,
        "Số điện thoại": so_dien_thoai
    }
    danh_sach_nhan_vien.append(nhan_vien)
    print("thêm nhân viên thành công!")
def xoa_nhan_vien(danh_sach_nhan_vien):
    ten = input("Nhập tên nhân viên cần xóa:")
    for nhan_vien in danh_sach_nhan_vien:
        if nhan_vien["Tên"] == ten:
            danh_sach_nhan_vien.remove(nhan_vien)
            print("xóa nhân viên thành công!")
            return
    print("không tìm thấy nhân viên.")
def cap_nhat_nhan_vien(danh_sach_nhan_vien):
    ten = input("Nhập tên nhân viên cần cập nhật:")
    for nhan_vien in danh_sach_nhan_vien:
        if nhan_vien["Tên"] == ten:
            dia_chi = input("Nhập địa chỉ nhân viên mới:")
            so_dien_thoai = input("Nhập số điện thoại nhân viên mới:")
            nhan_vien["Địa chỉ"] = dia_chi
            nhan_vien["Số điện thoại"] = so_dien_thoai
            print("Cập nhật thông tin nhân viên thành công!")
            return
    print("không tìm thấy nhân viên")
def tim_kiem_nhan_vien(danh_sach_nhan_vien):
    ten = input("Nhập tên nhân viên cần tìm kiếm:")
    for nhan_vien in danh_sach_nhan_vien:
        if nhan_vien["Tên"] == ten:
            print("thông tin nhân viên")
            print(f"Tên: {nhan_vien['Tên']}")
            print(f"Địa chỉ: {nhan_vien['Địa chỉ']}")
            print(f"Số điện thoại:{nhan_vien['Số điện thoại']}")
            return
    print("Không tìm thấy nhân viên")



danh_sach_nhan_vien = []

while True:
    print("-----Menu-----")
    print("a. thêm nhân viên")
    print("b. xóa bỏ nhân viên")
    print("c. cập nhật thông tin nhân viên")
    print("d. tìm kiếm thông tin nhân viên")
    print("e. thoát chương trình")
    choice = input("nhập lựa chọn của bạn:")

    if choice == "a":
        them_nhan_vien(danh_sach_nhan_vien)
    elif choice == "b":
        xoa_nhan_vien(danh_sach_nhan_vien)
    elif choice == "c":
        cap_nhat_nhan_vien(danh_sach_nhan_vien)
    elif choice == "d":
        tim_kiem_nhan_vien(danh_sach_nhan_vien)
    elif choice == "e":
        print("kết thúc chương trình")
        break
    else:
        print("lựa chọn không hợp lệ")