## 1. Layer 2 foundations
### 1.1. Data Link Layer
#### 1.1.1. Tổng quan về Data Link Layer
Là tầng thứ 2 trong mô hình OSI, mang
chức năng:
  + Đóng khung (Framing): Chia luồng bit dữ liệu từ tầng Vật lý thành các khối dễ quản lý gọi là Frame.
  + Kiểm soát lỗi (Error Control): Phát hiện và yêu cầu gửi lại các Frame bị mất hoặc bị lỗi trong quá trình truyền qua cáp hoặc sóng.
  + Kiểm soát luồng (Flow Control): Ngăn chặn tình trạng nút gửi truyền dữ liệu quá nhanh khiến nút nhận không thể xử lý kịp.
  + Điều khiển truy cập (Access Control): Xác định thiết bị nào được phép truyền dữ liệu tại một thời điểm nhất định trong các mạng dùng chung.
  
Hai lớp con của Data Link Layer:
  + Logical Link Control (LLC): là lớp con điều khiển liên kết logic, có trách nhiệm giao tiếp với các tầng mạng phía trên, xác định các giao thức lớp mạng sử dụng, đồng thời quản lý kiểm soát lỗi hay luồng dữ liệu.
  + Media Access Control (MAC): là lớp con điều khiển truy cập đường truyền, chịu trách nhiệm tương tác qua lớp physical (lớp 1) chịu trách nhiệm quản lý thời điểm + cách thức truy cập của thiết bị phép truy cập để tránh xung đột.
#### 1.1.2. Topologies
  + Xét theo vật lý:
    - Bus
    - Ring
    - Star
    - Mesh
    + Xét theo logic:
#### 1.1.3. Data Link Frame
### 1.2. Ethernet Switching
#### 1.2.1. Ethernet Frame
  + Preamble (7 bytes): đồng bộ hóa bit giữa bên gửi và bên nhận
  + Start of Frame Delimiter (SFD) (1 Byte): Luôn được thiết lập là 10101011, báo hiệu rằng các bit tiếp theo là điểm bắt đầu của khung (địa chỉ đích)
  + Destination Address (6 Bytes): Chứa địa chỉ MAC của máy nhận dữ liệu.
  + Source Address (6 Bytes): Chứa địa chỉ MAC của máy gửi. Đây luôn là địa chỉ Unicast.
  + Length (2 Bytes): Xác định độ dài của toàn bộ khung. Ethernet giới hạn độ dài dữ liệu tối đa là 1500 Bytes.
  + Data (Payload): Nơi chứa dữ liệu thực tế. Nếu dữ liệu nhỏ hơn 46 bytes, các bit 0 (padding) sẽ được thêm vào để đạt độ dài tối thiểu.
  + Cyclic Redundancy Check (CRC) (4 Bytes): Chứa mã hash 32-bit dùng để phát hiện lỗi. Nếu mã hash bên nhận tính toán khác với mã gửi đi, dữ liệu được coi là đã bị lỗi.
#### 1.2.2. Ethernet MAC Address
Là địa chỉ vật lý được ISP gán cố định cho cổng mang Ethernet của thiết bị, giúp nhận diện & giao tiếp chính xác với nhau trong cùng một local area network (LAN).
Định dạng: thường bao gồm 12 kí tự hex, chia thành 6 cặp, ngăn cách bởi dấu ```:``` hoặc dấu ```-```
Tính duy nhất: Địa chỉ MAC cố định theo phần cứng.
So sánh với địa chỉ IP: thay vì phụ thuộc vào vị trí mà mạng & thiết bị đang kết nối để định tuyến gói tin, MAC như "cột mốc" để các thiết bị tìm thấy nhau.

#### 1.2.3. The MAC Address Table
#### 1.2.4. Switch Speeds and Forwading Methods
### 1.3. Address Resolution
#### 1.3.1. MAC and IP
#### 1.3.2. ARP
#### 1.3.3. Neighbor Discovery
