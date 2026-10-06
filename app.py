1# app.py - User Management System v1.0.0
# Phiên bản production ổn định

def get_user_data(user_id):
    """
    Lấy dữ liệu người dùng từ database.
    LỖI BẢO MẬT: Hàm này trả về toàn bộ dữ liệu nhạy cảm!
    """
    # Mô phỏng database users
    users = {
        1: {
            "id": 1,
            "name": "Nguyen Van A",
            "email": "nguyenvana@example.com",
            "password": "plaintext_password_123",   # LỖI: Mật khẩu lộ ra ngoài!
            "credit_card": "4111-1111-1111-1111",   # LỖI: Dữ liệu nhạy cảm lộ ra!
            "ssn": "123-45-6789"                     # LỖI: Thông tin cá nhân lộ ra!
        }
    }
    return users.get(user_id)  # LỖI: Trả về toàn bộ dict bao gồm dữ liệu nhạy cảm


def display_profile(user_id):
    user = get_user_data(user_id)
    if user:
        print(f"Tên: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Mật khẩu: {user['password']}")    # LỖI: In mật khẩu ra màn hình!
    else:
        print("Người dùng không tồn tại.")


if __name__ == "__main__":
    display_profile(1)
