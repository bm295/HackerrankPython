# AZ-900 — Ghi chú ôn tập

## Tra nhanh theo keyword trong câu hỏi

Keywords giúp tìm phần hướng dẫn phù hợp; luôn đọc yêu cầu và điều kiện trước khi chọn đáp án.

| English keywords / scenario cues | Bài học | Gợi ý suy luận |
| --- | --- | --- |
| hardware failures, data center outages, remain operational, Availability Zones | [AZ900-001](#az900-001) | Cần high availability qua nhiều zone trong cùng region; backup chỉ hỗ trợ khôi phục. |
| cloud arrangement, support infrastructure in a data center | [AZ900-002](#az900-002) | Xác định ai vận hành hạ tầng vật lý và phân biệt cloud deployment model với serverless. |

<a id="az900-001"></a>

## AZ900-001 | Duy trì hoạt động với Availability Zones

**Dấu hiệu:** Ứng dụng cần remain operational khi có hardware failures hoặc data center outages.

**Nhóm kiến thức:** Describe Azure architecture and services → core architectural components → availability zones.

**Liên hệ lý thuyết:** Availability Zones là các nhóm datacenter tách biệt trong cùng Azure region, có nguồn điện, làm mát và mạng độc lập. Phân bố workload qua nhiều zone giúp duy trì dịch vụ khi một zone gặp sự cố.

**Cách phân tích đáp án:** Chọn Azure Availability Zones cho yêu cầu high availability trước sự cố datacenter. Azure Backup dùng sao lưu và khôi phục; Resource Groups tổ chức, quản lý tài nguyên; Reserved Instances giúp tiết kiệm chi phí theo cam kết sử dụng.

**Bẫy:** Chỉ triển khai vào một zone không tạo khả năng chịu lỗi khi zone đó ngừng hoạt động. Cần cấu hình nhiều zone hoặc dùng dịch vụ zone-redundant phù hợp, bao gồm các dependency của ứng dụng. Khả năng hỗ trợ phụ thuộc region và dịch vụ. Availability Zones không tự bảo vệ trước sự cố toàn region; khi đó cần thiết kế multi-region.

<a id="az900-002"></a>

## AZ900-002 | Ai vận hành hạ tầng vật lý trong các cloud model?

**Dấu hiệu:** Cloud arrangement, support infrastructure in a data center.

**Nhóm kiến thức:** Describe cloud concepts → cloud deployment models.

**Liên hệ lý thuyết:** Trong public cloud, nhà cung cấp sở hữu và vận hành hạ tầng vật lý. Private cloud dành riêng cho một tổ chức, có thể đặt tại chỗ hoặc thuê bên thứ ba lưu trữ. Hybrid cloud kết nối môi trường public và private.

**Cách phân tích đáp án:** Khi đề hỏi mô hình triển khai mà khách hàng giao việc vận hành datacenter vật lý cho nhà cung cấp, chọn public cloud. Serverless mô tả cách chạy workload mà khách hàng không trực tiếp quản lý máy chủ.

**Bẫy:** Việc thuê bên thứ ba lưu trữ private cloud không biến môi trường dành riêng đó thành public cloud. Trong public cloud, khách hàng vẫn có trách nhiệm với dữ liệu và quyền truy cập.
