### 1. Mô tả về VPN
#### 1.1. VPN là gì
*   **VPN (Virtual Private Network)** là **mạng riêng ảo**, một phương pháp cho phép người dùng kết nối an toàn vào mạng nội bộ của một tổ chức từ bất cứ đâu thông qua môi trường internet.

*   Cấu trúc khi không có VPN: User -> **ISP** -> Internet -> Website
*   Cấu trúc khi có VPN: User -> **VPN server** -> Internet -> Website

#### 1.2. Phân loại:
*   **Remote Access (Client-to-site):** 
    * **Cách thức hoạt động:** Giao thức này cho phép người dùng kết nối vào một mạng riêng từ xa thông qua một máy chủ VPN Server đóng vai trò là điểm tập trung kết nối
    * **Cơ chế bảo mật:** Sau khi tài khoản VPN Client được xác thực, hệ thống sẽ khởi tạo một đường hầm **(tunnel)** mã hóa nối từ máy tính của người dùng đến mạng nội bộ ở xa. Nhờ đường hầm này, mọi dữ liệu trao đổi giữa hai bên được truyền tải riêng tư.
*   **Site-to-Site:** 
    * **Cách thức hoạt động:** Là mô hình tạo ra một đường dẫn mã hóa cố định giữa hai mạng nội bộ nằm ở các vị trí địa lý khác nhau (ví dụ: kết nối giữa trụ sở chính và chi nhánh).
    * **Cơ chế bảo mật:** Hệ thống tự động điều hướng các gói tin (packages) đi qua đường dẫn an toàn này thay vì truyền công khai trên Internet. Các gói tin khi đi qua đường dẫn sẽ dựa vào các giao thức mã hóa để đảm bảo tính toàn vẹn và ngăn chặn việc dữ liệu bị rò rỉ ra ngoài.

### 2. Các giao thức VPN

*   **PPTP (Point to Point Tunneling Protocol):** Là giao thức đường hầm kết nối điểm, sử dụng kết hợp giữa GRE (Generic Routing Encapsulation) [^1] và PPP (Point-to-Point Protocol) [^2] để đóng gói và truyền gói tin. Giao thức này giúp **che giấu địa chỉ IP gốc** của người dùng.
*   **L2TP/IPSec:** 
    *   **L2TP (Layer 2 Tunneling Protocol):** Tạo đường hầm ở tầng 2 (Data Link) nhưng không tự mã hóa.
    *   **IPSec (Internet Protocol Security):** Làm việc ở tầng 3 (Network), cung cấp ba yếu tố quan trọng là **mã hóa, xác thực và đảm bảo tính toàn vẹn** dữ liệu. Khi kết hợp, lưu lượng được mã hóa bằng giao thức ESP [^3] của IPSec.



### 3. Ý nghĩa của việc sử dụng VPN

*   **Tính linh hoạt:** Đáp ứng nhu cầu làm việc từ xa, giúp users không bị gò bó bởi không gian và thời gian.
*   **An toàn dữ liệu:** Bảo mật thông tin khi truyền qua môi trường internet không tin cậy bằng các phương pháp mã hóa hiện đại như Encapsulating Security Payload (ESP) [^3].
*   **Hiệu quả công việc:** Cho phép truy cập vào các máy chủ dữ liệu (Data Center) nội bộ để thực hiện công việc từ bất cứ đâu, giúp tăng năng suất và xử lý sự cố kịp thời.

