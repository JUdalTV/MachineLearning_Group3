Nhóm 3

Thành viên trong nhóm: 

    Nguyễn Trọng Hạnh Phúc   S158665
    Bùi Minh Thành           S1546365
    Nguyễn Tiến Dũng         49565
    Nguyễn Hoàng Nam         141565
    
Dự án AI - Trích xuất thông tin từ căn cước công dân

Giới thiệu

Dự án này sử dụng các công nghệ và thư viện hiện đại để xây dựng một hệ thống trích xuất thông tin tự động từ hình ảnh căn cước công dân. Hệ thống có thể phát hiện, nhận diện, và trích xuất các trường dữ liệu quan trọng như họ tên, ngày sinh, số căn cước, địa chỉ, v.v. Mục tiêu của dự án là tạo ra một giải pháp hiệu quả và chính xác để hỗ trợ số hóa dữ liệu.
________________________________________

Công nghệ được sử dụng

LabelImg

LabelImg là một công cụ mã nguồn mở để gán nhãn dữ liệu hình ảnh. Trong dự án này, LabelImg được sử dụng để:

•	Cắt và tách các trường thông tin: Hỗ trợ định vị và phân loại các vùng quan trọng trên căn cước công dân, chẳng hạn như họ tên, ngày sinh, số CMND/CCCD, địa chỉ, v.v.

•	Xuất dữ liệu gán nhãn dưới định dạng XML (PASCAL VOC) hoặc YOLO, giúp dễ dàng tích hợp vào quy trình huấn luyện mô hình AI.

Darknet YOLOv4

Darknet YOLOv4 là một framework mã nguồn mở dành cho các tác vụ nhận diện và phát hiện đối tượng trong hình ảnh, với ưu điểm về tốc độ và độ chính xác. Trong dự án này, Darknet YOLOv4 được sử dụng để:

•	Huấn luyện mô hình AI: Dựa trên tập dữ liệu được gán nhãn từ LabelImg, YOLOv4 được sử dụng để huấn luyện mô hình nhằm phát hiện và trích xuất các trường thông tin từ hình ảnh căn cước công dân.

•	Phát hiện đối tượng theo thời gian thực: Mô hình YOLOv4 tích hợp khả năng xử lý nhanh, cho phép trích xuất thông tin từ căn cước công dân một cách hiệu quả trong thời gian thực.

•	Tích hợp dễ dàng: Framework Darknet hỗ trợ đa nền tảng và cung cấp các công cụ mạnh mẽ để tối ưu hóa quá trình huấn luyện và triển khai mô hình.
________________________________________
Thư viện Python được sử dụng

NumPy

NumPy là một thư viện mạnh mẽ hỗ trợ tính toán khoa học và thao tác với mảng dữ liệu. Trong dự án, NumPy được sử dụng để:

•	Xử lý và phân tích dữ liệu hình ảnh dưới dạng mảng số.

•	Tăng hiệu suất khi thực hiện các phép toán ma trận và vector hóa.

OpenCV (cv2)

OpenCV là một thư viện xử lý hình ảnh mã nguồn mở. Dự án sử dụng OpenCV để:

•	Đọc và xử lý các tệp hình ảnh căn cước công dân.

•	Chuyển đổi hình ảnh, áp dụng các bộ lọc, và phát hiện vùng quan tâm (ROI).

Matplotlib

Matplotlib được sử dụng để:

•	Hiển thị hình ảnh, kết quả phân tích, và trực quan hóa quá trình phát hiện.

Pillow (PIL)

Pillow là một thư viện hỗ trợ xử lý và thao tác hình ảnh. Trong dự án, Pillow được dùng để:

•	Thêm chú thích (text) lên hình ảnh bằng công cụ vẽ.

•	Định dạng lại và chuyển đổi ảnh khi cần thiết.

PyTesseract

PyTesseract là một wrapper của Tesseract OCR, dùng để:

•	Trích xuất văn bản từ hình ảnh đã được phát hiện.

•	Hỗ trợ nhận diện ký tự từ các trường thông tin trên căn cước công dân.

Pipeline

Pipeline là thư viện xử lý ngôn ngữ tự nhiên cho tiếng Việt. Trong dự án, Pipeline được sử dụng để:

•	Chuẩn hóa văn bản sau khi trích xuất nhằm cải thiện độ chính xác và thống nhất dữ liệu.

JSON

Thư viện tích hợp trong Python, được sử dụng để:

•	Lưu trữ và truy xuất các dữ liệu đầu ra theo định dạng JSON.

re (Regular Expressions)

Thư viện tích hợp trong Python, hỗ trợ:

•	Xử lý và trích xuất các mẫu thông tin cụ thể như số căn cước, ngày tháng, địa chỉ.
________________________________________
Các công cụ và thư viện khác

•	Zipfile

Được sử dụng để nén hoặc giải nén các tệp dữ liệu.

•	OS

Hỗ trợ tương tác với hệ thống tệp, giúp quản lý và xử lý các thư mục, tệp hình ảnh hiệu quả.
________________________________________
Cách sử dụng
1.	Gán nhãn dữ liệu:
o	Sử dụng LabelImg để gán nhãn các trường thông tin trên ảnh căn cước công dân.
o	Xuất tập dữ liệu gán nhãn dưới định dạng YOLO.
2.	Huấn luyện mô hình:
o	Sử dụng Darknet YOLOv4 để huấn luyện mô hình dựa trên tập dữ liệu gán nhãn.
3.	Trích xuất thông tin:
o	Dùng PyTesseract để trích xuất văn bản từ các vùng được phát hiện.
o	Chuẩn hóa văn bản bằng thư viện Underthesea.
4.	Lưu trữ kết quả:
o	Xuất kết quả trích xuất ra tệp JSON để dễ dàng quản lý và sử dụng.

Link model https://drive.google.com/drive/folders/16BfeUoJAJGI6EQAGpi-8ILy_xccyRArk?usp=sharing
