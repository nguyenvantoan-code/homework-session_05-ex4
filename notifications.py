# notifications.py - Tính năng thông báo (ĐANG PHÁT TRIỂN - chưa hoàn thiện)
# Feature này đang được phát triển cho v2.0.0, KHÔNG THỂ DEPLOY ngay

import smtplib  # Chưa cấu hình xong SMTP server

def send_email_notification(user_id, message):
    """
    Gửi thông báo email cho người dùng.
    TODO: Chưa xử lý lỗi kết nối SMTP
    TODO: Chưa có template email
    TODO: Chưa có queue hàng đợi
    """
    # WARNING: Đây là code WIP (Work In Progress), chưa production-ready!
    print(f"[WIP] Gửi email tới user {user_id}: {message}")
    # raise NotImplementedError("Chức năng này chưa hoàn thiện!")


def send_push_notification(user_id, title, body):
    """
    TODO: Tích hợp Firebase Cloud Messaging - chưa xong
    """
    print(f"[WIP] Push notification tới user {user_id}: {title} - {body}")
