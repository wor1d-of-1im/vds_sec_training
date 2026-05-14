* component

   * Command line interface(CLI): cho phép người dùng trực tiếp thao tác lệnh (commands) trên terminal, tương tác trực tiếp với hệ điều hành (Operator System)

   * Graphical User Interface(GUI): cho phép người dùng sử dụng giao diện đồ họa để tương tác với hệ điều hành, đồng thời trên giao diện có nhiều menu để đơn giản hóa thao tác.
* envs (Environment Variables (biến môi trường)): là các biến được hệ điều hành lưu trữ nhằm cung cấp thông tin cấu hình cho chương trình và tiến trình (process). Ví dụ như PATH, HOME, USER, giúp chương trình biết nơi tìm executable hoặc thư mục người dùng.
* ownership and permission
   * ownership
      * user: tức người tạo ra file tức là chủ của file (owner)
      * group: một user-group có thể có nhiều users, đồng thời tất cả các users trong cùng một group sẽ có quyền truy cập (permission access) vào file như nhau.
      * other: là user khác có quyền truy cập vào tệp, không phải owner, cũng không thuộc user-group nào sở hữu tệp.
   * permission
      * read (r or 4): cho phép mở, đọc và liệt kê nội dung tập tin/thư mục (file/folder).
      * write (w or 2): cho phép sửa đổi nội dung bao gồm thêm, xóa, đổi tên tập tin hoặc các tệp tin trong thư mục.
      * execute (x or 1): cho phép chạy/thực thi chương trình.
* shebang
    * Không phải comment, nằm ở dòng đầu của script, nhằm thông báo cho OS về trình thông dịch (interpreter) được sử dụng
* conditions: được sử dụng để kiểm tra điều kiện đúng/sai trong script hoặc chương trình, từ đó quyết định luồng thực thi.
* regex (Regular Expression): là biểu thức chính quy dùng để tìm kiếm, kiểm tra hoặc xử lý chuỗi văn bản theo mẫu (pattern); regex thường được dùng trong tìm kiếm dữ liệu, validate input và filtering text.
