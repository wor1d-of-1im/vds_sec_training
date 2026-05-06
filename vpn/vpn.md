### 1. Mô tả về VPN
#### 1.1. Định nghĩa
Virtual Private Network (VPN) là _mạng ảo_, cho phép, hỗ trợ người dùng thiết lập, truy cập internet tự do. VPN có thể giúp người dùng truy cập một số website mà mạng thường bị chặn, bảo vệ thông tin cá nhân của người dùng tốt hơn.

- Cấu trúc khi không có VPN:

User -> ISP -> Internet -> Website
- Cấu trúc khi có VPN:

User -> VPN server -> Internet -> Website

#### 1.2. Kiểu sử dụng VPN
##### 1.2.1. Client-to-Site (Remote Access) VPN
- Cho phép user kết nối tới một mạng riêng từ xa thông qua máy chủ VPN Server.
- User thông qua tài khoản VPN Client đã xác thực với VPN Server, khởi tạo đường truyền VPN mã hóa từ máy của User đến mạng ở xa. Từ đó việc trao đổi dữ liệu giữa 2 bên được truyền riêng và bảo mật.

Mục đích:
- Truy cập vào mạng riêng từ xa
- Truy cập internet an toàn, hiệu quả
- Đảm bảo thông tin cá nhân hơn trên mạng
##### 1.2.2. Site-to-Site VPN
- Tạo đường dẫn mã hóa giữa 2 mạng ở các vị trí khác nhau
- Điều hướng các packages theo đường dẫn. Các đường dẫn kết nối tới đích dựa vào các giao thức mã hóa, nhằm dảm bảo data không bị lộ ra.

Mục đích:
- Kết nối 2 mạng riêng biệt thành 1 mạng thống nhất
- Mang tính đồng bộ hệ thống