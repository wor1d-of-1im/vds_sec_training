### 1. Các mô hình mạng phổ biến
#### 1.1. Mạng LAN (Local Area Network)

Lý thuyết:

Mạng cục bộ, phạm vi nhỏ (phòng, tòa nhà)
Tốc độ cao, độ trễ thấp

Cấu trúc:

- Thiết bị (PC, Laptop, Printer) kết nối vào Switch
- Switch kết nối với Router
- Router kết nối ra Internet

#### 1.2. Mạng WAN (Wide Area Network)

Lý thuyết:

- Kết nối nhiều mạng LAN ở phạm vi lớn
- Sử dụng hạ tầng của ISP

Cấu trúc:

- Nhiều mạng (City, Campus, Enterprise, Government)
- Kết nối thông qua ISP
- ISP tạo thành mạng WAN trung gian
#### 1.3. Mạng Internet

Lý thuyết:

- Mạng toàn cầu, kết nối các mạng với nhau
- Hoạt động dựa trên TCP/IP

Cấu trúc:
Mạng nội bộ → Router → ISP → Internet
Trong Internet có các server:
- DNS Server
- Web Server
- Database Server
### 2. Mô hình thiết kế mạng
#### 2.1. Mô hình đơn giản (không xác thực)

Cấu trúc:
Internet → Firewall → Router → Switch

Từ Switch kết nối tới:
- PC
- Printer
- Server
- Wi-Fi (Laptop, Mobile)

Chức năng:

- Firewall: lọc và bảo vệ mạng
- Router: định tuyến
- Switch: kết nối nội bộ
- Access Point: phát Wi-Fi
2.2. Mô hình có xác thực

Cấu trúc:
Internet → Firewall → Core Switch

Kết nối thêm:
- RADIUS Server
- Wireless Controller
- Access Point

Cách hoạt động:

- Người dùng kết nối mạng
- Nhập tài khoản
- RADIUS kiểm tra
- Cho phép hoặc từ chối truy cập
### 3. Các giao thức mạng phổ biến
#### 3.1. ARP (Address Resolution Protocol)
Chuyển đổi địa chỉ IP → MAC
Hoạt động bằng broadcast trong mạng LAN
#### 3.2. DHCP (Dynamic Host Configuration Protocol)
Cấp phát IP tự động
Cung cấp:
- IP
- Subnet mask
- Gateway
- DNS
#### 3.3. Telnet / SSH
Điều khiển thiết bị từ xa
Telnet: không mã hóa
SSH: có mã hóa, an toàn hơn
#### 3.4. DNS / HTTP
DNS: chuyển tên miền → IP
HTTP: truyền dữ liệu web
### 4. Giao thức ARP (chi tiết)
#### 4.1. Reverse ARP (RARP)
Tìm IP dựa trên MAC
Dùng cho thiết bị chưa có IP
#### 4.2. Inverse ARP
Tìm IP từ thông tin kết nối (WAN)
#### 4.3. Cách ARP hoạt động
Thiết bị gửi yêu cầu tìm MAC từ IP
Broadcast trong mạng
Thiết bị đích phản hồi MAC
Lưu vào bảng ARP