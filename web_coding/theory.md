I.
1. Cài đặt và sử dụng BurpSuite
- Cài đặt và làm quen công cụ burpsuite
- Cài đặt proxy cho trình duyệt
- Cài đặt certificate cho các trình duyệt khác nhau
- Các chức năng cơ bản của burpsuite

Cấu trúc HTTP Request/Response
Thành phần của một HTTP Request:
Request Line: chứa method (phương thức mà HTTP Request sử dụng, đa phần thường là GET, POST, ngoài ra còn có HEAD, PUT, DELETE, OPTION, CONNECT); URL (địa chỉ định danh của tài nguyên); HTTP version.
Headers: bổ sung thông tin của HTTP request và client, hoặc body của request; mỗi header là một cặp Tên: Giá trị. Một số header quan trọng: Host, User-Agent, Accept, Cookie, Authorization,...
Message Body: chứa payload được gửi đi, thường được dùng trong các phương thức POST hoặc PUT.

Lưu ý: Sau phần Headers luôn có một blank line, báo hiệu cho server rằng phần này đã kết thúc và Message Body sẽ xuất hiện sau đó (nếu có).

Thành phần của một HTTP Response:
Status Line: chứa HTTP Version, Status Code (mã trạng thái 3 chữ số, thường gặp như 200 (OK), 403 (Forbidden), 404 (Not Found),...)
Headers: thông tin bổ sung về response, server hay dữ liệu được trả về, hình thức khá tương đồng với Header của request. Một số header quan trọng: Content-Type, Server, Set-Cookie,...
Message Body: chứa dữ liệu thực tế mà client yêu cầu.
Lưu ý: Tương tự HTTP Request, sau phần Headers của HTTP Response cũng có blank line ngăn cách Headers với Message Body.

Tìm hiểu và demo các HTTP method trên website thực tế
Các HTTP Header - Tìm hiểu kỹ Host Header
Tìm hiểu kỹ về cookie và các flag của cookie (Trả lời câu hỏi - vì sao website có thể lưu phiên đăng nhập của người dùng)
Status code


Cấu trúc của 1 URL (mẫu URL: https://www.rfc.editor.org/rfc/rfc1738.html)
Giao thức (scheme): https
Mục đích: Quy định cách thức trình duyệt giao tiếp với máy chủ.
Seperator: ://
Tên miền (Domain name/host): www.rfc.editor.org
Port: 443 (port mặc định của https)
Path: /rfc/rfc1738.html
Web Functionality
Encoding Schemes



Câu hỏi:
- Tại sao chúng ta phải dùng BurpSuite để thực hiện pentest web?
BurpSuite là công cụ kiểm thử bảo mật toàn diện có uy tín bậc nhất hiện nay cho việc pentest web, bởi:
BurpSuite cho phép kiểm tra, chặn, sửa đổi (modify) và gửi lại (resend) tất cả lưu lượng truy cập giữa trình duyệt với ứng dụng web.
Đa dạng công cụ, tính năng (ví dụ một số chức năng chính như decoder (mã hoá và giải mã dữ liệu dưới nhiều định dạng khác nhau; proxy server (chặn & chỉnh sửa nội dung các yêu cầu và phản hồi trong khi vẫn đang giao tiếp với ứng dụng web); repeater; comparer…)
Giao diện dễ sử dụng.



- Khi chúng ta đánh giá Ứng dụng Web, có nghĩa là chúng ta đánh giá những gì?
Các yếu tố chúng ta cần khi đánh giá ứng dụng Web:
Mức độ an toàn của web
Hiệu năng (tốc độ, khả năng chịu tải…)
Các tính năng cần hoạt động theo đúng mục đích, yêu cầu
Trải nghiệm từ chính người dùng (UI/UX - User Interface/User Experience)



- Chu trình xử lý của trình duyệt từ khi nhập địa chỉ website trên thanh URL tới khi render toàn bộ nội dung website





II.
Mô tả cấu hình:
           Đối với website thông thường:
Tên miền
Địa chỉ IP
Cổng (Port): thường mặc định là cổng 80 (với HTTP) hoặc cổng 443 (với HTTPS), được bảo mật.
Một website sử dụng 1 tên miền - 1 IP - 1 port (vd: www.google.com)
Một website sử dụng 1 tên miền - 1 IP - nhiều port khác nhau
Nhiều website sử dụng 1 tên miền - 1 IP - nhiều port khác nhau
Nhiều website sử dụng nhiều tên miền - 1 IP - 1 port
Nhiều website sử dụng 1 tên miền - 1 IP - 1 port


Câu hỏi:
-  Web Server là gì? Vai trò và cách thức hoạt động của Web Server? Các loại Web Server thường gặp.
Web Server (máy chủ web) là chương trình mang nhiệm vụ chấp nhận các request từ clients (trình duyệt web) và trả về các response thông qua giao thức (thường là HTTP hoặc HTTPS).

Vai trò của web server:
Xử lý dữ liệu (phục vụ các nội dung một cách trực tiếp các tệp HTML, CSS, JavaScript hay hình ảnh được lưu trữ trên hệ thống)
Đảm bảo tính bảo mật (qua SSL/TLS, xác thực người dùng hay phân quyền truy cập)
Quản lý kết nối linh hoạt (qua TCP/IP, cho phép quản lý tài nguyên để có thể tương tác đồng thời với nhiều nguồn dữ liệu và thiết bị khác nhau)

Cách thức hoạt động:
Nhận request từ client
Xác định tài nguyên được yêu cầu
Truy xuất tài nguyên: tìm tài nguyên tương ứng sẵn có trong hệ thống.
Với nội dung tĩnh (như hình ảnh), trả kết quả trực tiếp cho client; với nội dung động (như PHP, Node.js, …) cần chuyển yêu cầu và dữ liệu tới Web Application để xử lý rồi mới trả kết quả về cho client, và cả hai đều có thể nhận được mã trạng thái nếu không có kết quả tương ứng.

Các loại Web Server thường gặp:
Nginx: là một web server đảm bảo được việc xử lý lưu lượng lớn mà không giảm hiệu suất; có thể hoạt động như reverse proxy và load balancer. Ưu điểm: hiệu suất cao, cấu hình tương đối dễ sử dụng.
Microsoft IIS: ngoài dịch vụ như Web Server, nó còn có thể là FTP Server, thường dùng cho các hệ điều hành Windows Server. Ưu điểm: hỗ trợ ứng dụng của nhà phát triển Microsoft (dễ dàng tích hợp .NET Framework hay SQL Server), Giao diện đồ hoạ dễ sử dụng, tính bảo mật cao (ngăn cản DDoS, quản lý quyền truy cập…)
Apache HTTP Server: thuộc dạng Web Server mã nguồn mở lâu đời và phổ biến nhất. Ưu điểm: cấu hình linh hoạt (hỗ trợ các module mở rộng cho nhiều tính năng khác nhau như bảo mật, cấu hình URL), khả năng hỗ trợ rộng rãi, tương thích trên nhiều hệ điều hành khác nhau.



- Web Application là gì? Vai trò và cách thức hoạt động của Web Application? Các loại Web Application thường gặp.

Web Application (Ứng dụng Web) là một chương trình phần mềm được tạo bằng các ngôn ngữ lập trình (như PHP, Python, Java, Node.js), chạy trên Web Server cho phép người dùng tương tác cũng như thực hiện các chức năng cụ thể (đăng nhập, mua bán hàng, tính toán…) thông qua trình duyệt web mà không cần cài đặt như phần mềm khác vào máy tính.
Vai trò:
Tương tác với người dùng: qua giao diện của web application.
Xử lý logic: thực hiện quy trình (như đăng nhập, tính toán, quản lý CSDL,...)
Tương tác CSDL: Kết nối, truy vấn, xử lý và sao lưu dữ liệu trong CSDL (như MySQL)
Truy cập & cập nhật nhanh chóng: nhờ việc liên kết trực tiếp với Web Server.
Quản lý hoạt động: Theo dõi trạng thái và hoạt động của người dùng (như trạng thái đăng nhập) thông qua Session.
Cách thức hoạt động:
Nhận request được chuyển tiếp từ web server.
Xác thực phiên người dùng.
Tra cứu CSDL để lấy thông tin hồ sơ.
Tạo nội dung động từ thông tin được tiếp nhận.
Trả nội dung động cho web server để hoàn thiện response và gửi về client.
Các loại Web Application thường gặp:
Static web application: nội dung tĩnh, gần như không có hoặc ít tương tác với người dùng ngoài sở hữu, ví dụ như blog cá nhân.
Dynamic web application: nội dung thay đổi theo lượng dữ liệu truy cập và người dùng, ví dụ như các trang mạng xã hội như Facebook, trình phát video Youtube hay Gmail.
Ứng dụng thương mại điện tử: dành riêng cho giao dịch, mua bán trực tuyến, ví dụ như Shopee.
Web Application với CMS (Content Management System): cho phép quản lý và cập nhật nội dung dễ dàng (như WordPress).

- Mối quan hệ giữa Web Server và Web Application, các thức giao tiếp giữa các bên.

