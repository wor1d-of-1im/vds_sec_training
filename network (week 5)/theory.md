## 1. Layer 2 foundations
Mục tiêu tìm hiểu về:
* thiết bị trong LAN nói chuyện ra sao
* MAC dùng để làm gì
* switch chuyển frame kiểu gì
* IP biến thành MAC thế nào
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
MAC Address Table (hay còn gọi là CAM Table) là bảng được switch sử dụng để lưu trữ địa chỉ MAC và cổng tương ứng của thiết bị. Bảng này giúp switch chuyển tiếp frame một cách hiệu quả trong mạng LAN.

##### Cách MAC Address Table hoạt động

Khi switch nhận được một frame:
1. Switch đọc Source MAC Address.
2. Lưu địa chỉ MAC cùng với cổng nhận vào MAC Address Table.
3. Kiểm tra Destination MAC Address:
   - Nếu tìm thấy trong bảng → chuyển frame đúng đến cổng tương ứng.
   - Nếu không tìm thấy → flood frame ra tất cả các cổng khác.

##### Ví dụ MAC Address Table

| MAC Address | Port |
|---|---|
| 00-1A-2B-3C-4D-5E | Fa0/1 |
| 00-1B-3C-4D-5E-6F | Fa0/2 |

##### Ưu điểm
- Giảm lưu lượng không cần thiết
- Tăng hiệu suất mạng
- Giúp switch chuyển tiếp dữ liệu nhanh hơn

##### Lưu ý
- Các entry trong bảng MAC sẽ tự động bị xóa sau một khoảng thời gian không hoạt động.
- Switch liên tục học MAC Address động.
- Quá trình này gọi là MAC Learning.

#### 1.2.4. Switch Speeds and Forwading Methods
Switch hỗ trợ nhiều tốc độ Ethernet và các phương thức chuyển tiếp frame khác nhau.

##### Các tốc độ switch phổ biến

| Chuẩn Ethernet | Tốc độ |
|---|---|
| Fast Ethernet | 100 Mbps |
| Gigabit Ethernet | 1 Gbps |
| 10 Gigabit Ethernet | 10 Gbps |
| 40 Gigabit Ethernet | 40 Gbps |
| 100 Gigabit Ethernet | 100 Gbps |

Con người tạo ra mạng tốc độ hàng trăm gigabit chỉ để gửi meme nhanh hơn 0.2 giây. Công nghệ thật kỳ diệu.

##### Các phương thức Forwarding

###### 1. Store-and-Forward

Ở phương pháp này:
1. Switch nhận toàn bộ frame.
2. Kiểm tra lỗi bằng FCS/CRC.
3. Chỉ chuyển tiếp frame nếu không có lỗi.

**Ưu điểm**
- Kiểm tra lỗi tốt
- Độ tin cậy cao

**Nhược điểm**
- Độ trễ cao hơn

---

###### 2. Cut-Through

Ở phương pháp này:
1. Switch đọc Destination MAC Address.
2. Chuyển tiếp frame ngay mà không cần chờ nhận toàn bộ frame.

**Ưu điểm**
- Chuyển tiếp nhanh
- Độ trễ thấp

**Nhược điểm**
- Có thể chuyển tiếp cả frame lỗi

---

###### 3. Fragment-Free

Là phương pháp kết hợp:
- Switch kiểm tra 64 byte đầu tiên trước khi chuyển tiếp frame.

##### So sánh các phương pháp

| Phương pháp | Tốc độ | Kiểm tra lỗi |
|---|---|---|
| Store-and-Forward | Chậm hơn | Có |
| Cut-Through | Nhanh hơn | Không |
| Fragment-Free | Trung bình | Một phần |

### 1.3. Address Resolution
Address Resolution là quá trình ánh xạ địa chỉ IP (Layer 3) sang địa chỉ MAC (Layer 2).

#### 1.3.1. MAC and IP
MAC Address và IP Address đều cần thiết trong quá trình truyền dữ liệu mạng.

##### MAC Address
- Là địa chỉ vật lý của card mạng (NIC)
- Hoạt động ở Layer 2
- Dùng trong mạng LAN
- Thường dài 48 bit

Ví dụ:
```
00:1A:2B:3C:4D:5E
```
##### IP Address
* Là địa chỉ logic của thiết bị
* Hoạt động ở Layer 3
* Dùng để định tuyến giữa các mạng

Ví dụ IPv4:
```
192.168.1.10
```
#### 1.3.2. ARP
Quá trình hoạt động của ARP: Thiết bị muốn gửi dữ liệu đến IP -> Kiểm tra ARP Cache -> (Chưa biết MAC) -> gửi ARO Request dạng broadcast -> Thiết bị đích trả lời bằng ARP Reply -> MAC Address được lưu vào ARP Cache

Đặc điểm:
* Chỉ hoạt động với IPv4
* Sử dụng broadcast
* Hoạt động trong mạng LAN
#### 1.3.3. Neighbor Discovery
Là giao thức thay thế ARP trong IPv6.
Chức năng của Neighbor Discovery:
* Phân giải địa chỉ
* Tìm router
* Kiểm tra trùng địa chỉ
* Kiểm tra trạng thái của neighbor
Các loại message của Neighbor Discovery:
* Neighbor Solicitation (NS): Yêu cầu MAC Address
* Neighbor Advertisement (NA): Trả lời MAC Address
* Router Solicitation (RS): Yêu cầu thông tin router
* Router Advertisement (RA): Router gửi thông tin mạng

Quá trình hoạt động:
* Host gửi Neighbor Solicitation.
* Thiết bị đích trả lời bằng Neighbor Advertisement.
* MAC Address được lưu lại.

Ưu điểm của Neighbor Discovery:
* Hiệu quả hơn ARP
* Giảm broadcast
* Hỗ trợ tự động cấu hình IPv6
* Tăng khả năng mở rộng mạng

## 2. Layer 3 & Routing
### 2.1. Netwwork Layer
* IP Packet
* Routing concepts
### 2.2. IPv4 Addressing
#### 2.2.1. IPv4 Address Structure

#### 2.2.2. IPv4 Unicast, Broadcast, and Multicast
#### 2.2.3. Types of IPv4 Addresses
#### 2.2.4. Network Segmentation
#### 2.2.5. Subnet an IPv4
#### 2.2.6. Subnet a /16 and /8 Prefix
#### 2.2.7. Subnet to Meet Requirements
#### 2.2.8. Variable Length Subnet Masking
#### 2.2.9. Structured Design

### 2.3. Basic Router Configuration
#### 2.3.1. Configure Initial Router Settings
#### 2.3.2. Configure Interfaces
#### 2.3.3. Configure the Default Gateway
### 2.4. ICMP
#### 2.4.1. ping
#### 2.4.2. traceroute
#### 2.4.3. ICMP messages