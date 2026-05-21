## 1. Layer 2 foundations
Mục tiêu -> tìm hiểu về:
* thiết bị trong LAN nói chuyện ra sao
* MAC dùng để làm gì
* switch chuyển frame kiểu gì
* IP biến thành MAC thế nào
### 1.1. Data Link Layer
#### 1.1.1. Tổng quan về Data Link Layer
Là tầng thứ 2 trong mô hình OSI, mang
chức năng:
  * Đóng khung (Framing): Chia luồng bit dữ liệu từ tầng Vật lý thành các khối dễ quản lý gọi là Frame.
  * Kiểm soát lỗi (Error Control): Phát hiện và yêu cầu gửi lại các Frame bị mất hoặc bị lỗi trong quá trình truyền qua cáp hoặc sóng.
  * Kiểm soát luồng (Flow Control): Ngăn chặn tình trạng nút gửi truyền dữ liệu quá nhanh khiến nút nhận không thể xử lý kịp.
  * Điều khiển truy cập (Access Control): Xác định thiết bị nào được phép truyền dữ liệu tại một thời điểm nhất định trong các mạng dùng chung.
  
Hai lớp con của Data Link Layer:
  * Logical Link Control (LLC): là lớp con điều khiển liên kết logic, có trách nhiệm giao tiếp với các tầng mạng phía trên, xác định các giao thức lớp mạng sử dụng, đồng thời quản lý kiểm soát lỗi hay luồng dữ liệu.
  * Media Access Control (MAC): là lớp con điều khiển truy cập đường truyền, chịu trách nhiệm tương tác qua lớp physical (lớp 1) chịu trách nhiệm quản lý thời điểm + cách thức truy cập của thiết bị phép truy cập để tránh xung đột.
#### 1.1.2. Topologies
  * Xét theo vật lý:
    * Bus
    * Ring
    * Star
    * Mesh
  * Xét theo logic:
#### 1.1.3. Data Link Frame
### 1.2. Ethernet Switching
#### 1.2.1. Ethernet Frame
  * Preamble (7 bytes): đồng bộ hóa bit giữa bên gửi và bên nhận
  * Start of Frame Delimiter (SFD) (1 Byte): Luôn được thiết lập là 10101011, báo hiệu rằng các bit tiếp theo là điểm bắt đầu của khung (địa chỉ đích)
  * Destination Address (6 Bytes): Chứa địa chỉ MAC của máy nhận dữ liệu.
  * Source Address (6 Bytes): Chứa địa chỉ MAC của máy gửi. Đây luôn là địa chỉ Unicast.
  * Length (2 Bytes): Xác định độ dài của toàn bộ khung. Ethernet giới hạn độ dài dữ liệu tối đa là 1500 Bytes.
  * Data (Payload): Nơi chứa dữ liệu thực tế. Nếu dữ liệu nhỏ hơn 46 bytes, các bit 0 (padding) sẽ được thêm vào để đạt độ dài tối thiểu.
  * Cyclic Redundancy Check (CRC) (4 Bytes): Chứa mã hash 32-bit dùng để phát hiện lỗi. Nếu mã hash bên nhận tính toán khác với mã gửi đi, dữ liệu được coi là đã bị lỗi.
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
   * Nếu tìm thấy trong bảng → chuyển frame đúng đến cổng tương ứng.
   * Nếu không tìm thấy → flood frame ra tất cả các cổng khác.

##### Ví dụ MAC Address Table

| MAC Address | Port |
|---|---|
| 00-1A-2B-3C-4D-5E | Fa0/1 |
| 00-1B-3C-4D-5E-6F | Fa0/2 |

##### Ưu điểm
* Giảm lưu lượng không cần thiết
* Tăng hiệu suất mạng
* Giúp switch chuyển tiếp dữ liệu nhanh hơn

##### Lưu ý
* Các entry trong bảng MAC sẽ tự động bị xóa sau một khoảng thời gian không hoạt động.
* Switch liên tục học MAC Address động.
* Quá trình này gọi là MAC Learning.

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
* Kiểm tra lỗi tốt
* Độ tin cậy cao

**Nhược điểm**
* Độ trễ cao hơn


###### 2. Cut-Through

Ở phương pháp này:
1. Switch đọc Destination MAC Address.
2. Chuyển tiếp frame ngay mà không cần chờ nhận toàn bộ frame.

**Ưu điểm**
* Chuyển tiếp nhanh
* Độ trễ thấp

**Nhược điểm**
* Có thể chuyển tiếp cả frame lỗi


###### 3. Fragment-Free

Là phương pháp kết hợp Switch kiểm tra 64 byte đầu tiên trước khi chuyển tiếp frame.

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
* Là địa chỉ vật lý của card mạng (NIC)
* Hoạt động ở Layer 2
* Dùng trong mạng LAN
* Thường dài 48 bit

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
Mục tiêu -> tìm hiểu về:
* router hoạt động ra sao
* packet đi qua nhiều mạng kiểu gì
* subnetting dùng để chia mạng
* ping/traceroute thực sự làm gì
### 2.1. Network Layer
#### 2.1.1. Network Layer Characteristics
#### 2.1.2. IPv4 Packet
#### 2.1.3. IPv6 Packet
#### 2.1.4. How a Host Routes
#### 2.1.5. Router Routing Tables

### 2.2. IPv4 Addressing
#### 2.2.1. IPv4 Address Structure
IPv4 address là địa chỉ logic dùng để định danh thiết bị trong mạng Layer 3.

IPv4:
- Dài 32 bit
- Gồm 4 octet
- Mỗi octet có giá trị từ `0-255`

Ví dụ:
```
192.168.1.10
```
Dạng nhị phân:
```
11000000.10101000.00000001.00001010
```
Cấu trúc IPv4

IPv4 gồm:

Network portion
Host portion

Ví dụ:

192.168.1.10/24
Network: 192.168.1
Host: 10

CIDR /24 nghĩa là:

24 bit dành cho network
8 bit dành cho host
#### 2.2.2. IPv4 Unicast, Broadcast, and Multicast
##### 2.2.2.1. Unicast

Unicast là truyền dữ liệu:
```
1 -> 1
```
Ví dụ:

PC1 gửi dữ liệu cho PC2

Đây là kiểu giao tiếp phổ biến nhất trên Internet.

##### 2.2.2.2. Broadcast

Broadcast là truyền:
```
1 -> tất cả thiết bị trong subnet
```
Ví dụ:
```
192.168.1.255
```
ARP request thường dùng broadcast:
```
Who has 192.168.1.10?
```
Mọi thiết bị đều phải xử lý broadcast frame.

##### 2.2.2.3. Multicast

Multicast là:
```
1 -> một nhóm thiết bị
```
Không gửi cho tất cả host.

Ví dụ:

Streaming video
Routing protocols
IPTV

Dải multicast:
```
224.0.0.0 - 239.255.255.255
```
#### 2.2.3. Types of IPv4 Addresses
Public IP Address

Public IP là địa chỉ IP được sử dụng trên Internet.

Đặc điểm:
* Duy nhất trên toàn cầu
* Được cấp bởi ISP
* Có thể truy cập từ Internet

Ví dụ:
```
8.8.8.8
1.1.1.1
```
Public IP thường dùng cho:
* Web server
* Router WAN
* Cloud services



### Private IP Address

Private IP được sử dụng trong mạng nội bộ (LAN).

Không thể route trực tiếp ra Internet.

Các dải Private IP:

| Range | CIDR |
|---|---|
| 10.0.0.0 - 10.255.255.255 | /8 |
| 172.16.0.0 - 172.31.255.255 | /12 |
| 192.168.0.0 - 192.168.255.255 | /16 |

Ví dụ:
```
192.168.1.10
```

Private IP thường kết hợp với NAT để truy cập Internet.



### Loopback Address

Loopback address:
```
127.0.0.1
```

Tên gọi:
```
localhost
```

Dùng để:
* Kiểm tra TCP/IP stack
* Test dịch vụ nội bộ
* Kiểm tra card mạng logic

Ping loopback:
```
ping 127.0.0.1
```
Nếu ping loopback lỗi thì hệ điều hành đang gặp vấn đề mạng nội bộ.
### APIPA Address

APIPA:
```
Automatic Private IP Addressing
```

Khi DHCP server không phản hồi, Windows tự động cấp IP:
```
169.254.x.x
```

Ví dụ:
```
169.254.10.20
```

Điều này cho thấy:
* Không nhận được IP từ DHCP
* Có thể lỗi:
  * DHCP server
  * Switch
  * Cable
  * VLAN
#### 2.2.4. Network Segmentation
Network segmentation là việc phân tách mạng lớn thành nhiều mạng nhỏ hơn.
### Mục đích của segmentation

| Lợi ích | Ý nghĩa |
|---|---|
| Giảm broadcast | Tăng hiệu suất |
| Tăng bảo mật | Cô lập thiết bị |
| Dễ quản lý | Chia theo phòng ban |
| Giảm lỗi lan rộng | Ổn định hệ thống |

### Ví dụ segmentation

Một công ty gồm:
- HR
- IT
- Finance

Có thể chia:

| Department | Network |
|---|---|
| HR | 192.168.10.0/24 |
| IT | 192.168.20.0/24 |
| Finance | 192.168.30.0/24 |

Mỗi subnet hoạt động độc lập hơn.

---

### Broadcast Domain

Mỗi subnet là một broadcast domain riêng.

Router sẽ chặn broadcast giữa các subnet.

Điều này giúp:
* Giảm traffic
* Tăng hiệu năng mạng

#### 2.2.5. Subnet an IPv4
Subnetting là quá trình chia một network lớn thành nhiều subnet nhỏ hơn.

### Ví dụ subnetting

Network ban đầu:
```
192.168.1.0/24
```

Yêu cầu: Chia thành 4 subnet


### Bước 1: Mượn bit

Cần 4 subnet:
```
2^2 = 4
```

Mượn 2 bit host.

Prefix mới:
```
/26
```

Subnet mask:
```
255.255.255.192
```

### Bước 2: Xác định block size

```
256 - 192 = 64
```

Block size:
```
64
```

### Bước 3: Tạo subnet

| Subnet | Host Range | Broadcast |
|---|---|---|
| 192.168.1.0/26 | .1 - .62 | .63 |
| 192.168.1.64/26 | .65 - .126 | .127 |
| 192.168.1.128/26 | .129 - .190 | .191 |
| 192.168.1.192/26 | .193 - .254 | .255 |

### Công thức subnetting

#### Số subnet
```
2^n
```

#### Số host
```
2^h - 2
```

Trong đó:
* `n`: số bit mượn
* `h`: số bit host còn lại

Trừ 2 vì:
* 1 network address
* 1 broadcast address
#### 2.2.6. Subnet a /16 and /8 Prefix
### Subnetting mạng /16

Ví dụ:
```
172.16.0.0/16
```

Nếu chia thành `/24`:
** Mượn thêm 8 bit
- Có:
```
2^8 = 256 subnet
```

Mỗi subnet:
```
254 host
```

### Ví dụ subnet

| Subnet | Host Range |
|---|---|
| 172.16.1.0/24 | .1 - .254 |
| 172.16.2.0/24 | .1 - .254 |
| 172.16.3.0/24 | .1 - .254 |

### Subnetting mạng /8

Ví dụ:
```
10.0.0.0/8
```

Host bits:
```
24 bit
```

Tổng host:
```
2^24 - 2
```

Kết quả:
```
16,777,214 host
```

Đây là mạng cực lớn bao gồm:
* Enterprise
* Data center
* Cloud provider

#### 2.2.7. Subnet to Meet Requirements
Subnetting nên dựa trên nhu cầu thực tế.

### Ví dụ yêu cầu

| Department | Hosts Needed |
|---|---|
| IT | 100 |
| HR | 50 |
| Sales | 20 |

### Chọn subnet phù hợp

#### IT

Cần:
```
100 host
```

Tính:
```
2^7 - 2 = 126
```

=> Chọn:
```
/25
```

#### HR

Cần:
```
50 host
```

Tính:
```
2^6 - 2 = 62
```

=> Chọn:
```
/26
```

#### Sales

Cần:
```
20 host
```

Tính:
```
2^5 - 2 = 30
```

=> Chọn:
```
/27
```

### Kết quả

| Department | Prefix | Host Capacity |
|---|---|---|
| IT | /25 | 126 |
| HR | /26 | 62 |
| Sales | /27 | 30 |

#### 2.2.8. Variable Length Subnet Masking
Cho phép sử dụng subnet mask khác nhau trên từng subnet.

### Ưu điểm của VLSM

| Ưu điểm | Ý nghĩa |
|---|---|
| Tiết kiệm IP | Giảm lãng phí |
| Linh hoạt | Phù hợp từng mạng |
| Dễ mở rộng | Thiết kế hiệu quả |

### Ví dụ VLSM

Network:
```
192.168.1.0/24
```

Yêu cầu:
* LAN1: 100 host
* LAN2: 50 host
* LAN3: 10 host

### Chia subnet

| LAN | Prefix | Host Capacity |
|---|---|---|
| LAN1 | /25 | 126 |
| LAN2 | /26 | 62 |
| LAN3 | /28 | 14 |

### Nguyên tắc VLSM

1. Chia subnet lớn nhất trước
2. Chia subnet nhỏ hơn sau
3. Không overlap địa chỉ

Nếu overlap subnet:
* Router sẽ định tuyến sai
* Packet có thể bị drop
#### 2.2.9. Structured Design
Structured design là thiết kế mạng theo cấu trúc rõ ràng và dễ quản lý.

### Mục tiêu

| Mục tiêu | Ý nghĩa |
|---|---|
| Scalability | Dễ mở rộng |
| Redundancy | Có dự phòng |
| Performance | Hiệu suất cao |
| Security | Bảo mật tốt |

### Thiết kế phân tầng Cisco

Cisco khuyến nghị mô hình:
```
Hierarchical Network Design
```

Gồm 3 lớp:

| Layer | Chức năng |
|---|---|
| Access Layer | Kết nối end devices |
| Distribution Layer | Routing và policy |
| Core Layer | Backbone tốc độ cao |

### Access Layer

Kết nối:
* PC
* Printer
* IP Phone
* Access Point

Thường dùng:
* Layer 2 switch

### Distribution Layer

Xử lý:
* Routing
* ACL
* QoS
* VLAN

Đây là lớp trung gian giữa access và core.

### Core Layer

Đặc điểm:
* High speed
* Low latency
* High availability

Core layer là xương sống của hệ thống mạng.

### Nguyên tắc thiết kế tốt thường bao gồm:

* Modular
* Hierarchical
* Fault tolerant
* Easy management
* Scalable
### 2.3. Basic Router Configuration
#### 2.3.1. Configure Initial Router Settings
#### 2.3.2. Configure Interfaces
#### 2.3.3. Configure the Default Gateway
### 2.4. ICMP
ICMP messages
## 3. Transport & Services
Mục tiêu -> tìm hiểu về:
* trình duyệt/web/game hoạt động thế nào
* vì sao TCP chậm hơn UDP
* port dùng để phân biệt dịch vụ
* ứng dụng dùng network ra sao

### 3.1. Transport Layer
#### 3.1.1. Transportation of Data
#### 3.1.2. TCP Overview
#### 3.1.3. UDP Overview
#### 3.1.4. Port Numbers
#### 3.1.5. TCP Communication Process
#### 3.1.6. Reliability and Flow Control .
#### 3.1.7. UDP Communication

### 3.2. Application Layer
#### 3.2.1. Application, Presentation, and Session
#### 3.2.2. Peer-to-Peer
#### 3.2.3. Web and Email Protocols
#### 3.2.4. IP Addressing Services
#### 3.2.5. File Sharing Services
