### Username enumeration via different responses

![!\[!\\[alt text\\]({13109A32-1318-4719-A077-46C10499FA33}.png)\](images/username_01.png)](images/username_01.png)
Mục tiêu: Tìm được username&password hợp lệ

Đầu tiên, mở Burp truy cập vào bài lab.

Bởi vì bài lab này tập trung vào việc dò tìm tài khoản, do đó mình chỉ tập trung vào phần đăng nhập của nó.
![alt text](images/username_02.png)

![!\[alt text\]({3445B23E-E132-49E4-86DC-312D5A131730}.png)](images/username_03.png)

Thử một tài khoản ngẫu nhiên:
```
Username: abc
Password: password
```
Và tất nhiên, kết quả trả về báo lỗi, cụ thể là sai username.
![!\[alt text\]({54B8E5A5-1A6F-49CB-A8A8-2CBC468FF67C}.png)](images/username_04.png)

Quay lại với burp suite, ta tìm đến phần vừa test tài khoản, và send request tới intruder.
![!\[alt text\]({2402D8AB-CCCA-4B54-94F5-1AEFC004B29E}.png)](images/username_05.png)

Tại intruder, ta thay lần lượt các username vào vị trí mà mình vừa nhập username lúc thử bằng chức năng Sniper attack:
![!\[alt text\]({D3A085C6-3735-4455-AD87-23DF9A69B224}.png)](images/username_06.png)

Sau khi thử, có một username mang Length khác biệt so với các username còn lại, kiểm tra response của nó và ta thấy một thông báo Incorrect password, tức là đã đúng username.
![!\[alt text\]({AA519CE5-9B5C-431A-9E53-0681A024D87E}.png)](images/username_07.png)

Quay lại intruder, ta thay username bằng username hợp lệ vừa tìm được, và tương tự, thử lần lượt các password bằng Sniper attack, nhận được password hợp lệ cho username từ trạng thái nhận được:
![!\[alt text\]({2FD34113-29C0-414B-B532-6F638D284CB4}.png)](images/username_08.png)

Trở lại giao diện bài lab, nhập username và password mới tìm được để hoàn thành bài này.
![!\[alt text\]({F743632A-51A5-46FB-AF6E-13D64388A52D}.png)](images/username_09.png)