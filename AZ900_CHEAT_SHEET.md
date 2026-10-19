# AZ-900 — Ghi chú ôn tập

## Tra nhanh theo keyword trong câu hỏi

Keywords giúp tìm phần hướng dẫn phù hợp; luôn đọc yêu cầu và điều kiện trước khi chọn đáp án.

| English keywords / scenario cues | Bài học | Gợi ý suy luận |
| --- | --- | --- |
| hardware failures, data center outages, remain operational, Availability Zones | [AZ900-001](#az900-001) | Cần high availability qua nhiều zone trong cùng region; backup chỉ hỗ trợ khôi phục. |

<a id="az900-001"></a>

## AZ900-001 | Duy trì hoạt động với Availability Zones

**Dấu hiệu:** Ứng dụng cần remain operational khi có hardware failures hoặc data center outages.

**Nhóm kiến thức:** Describe Azure architecture and services → core architectural components → availability zones.

**Liên hệ lý thuyết:** Availability Zones là các nhóm datacenter tách biệt trong cùng Azure region, có nguồn điện, làm mát và mạng độc lập. Phân bố workload qua nhiều zone giúp duy trì dịch vụ khi một zone gặp sự cố.

**Cách phân tích đáp án:** Chọn Azure Availability Zones cho yêu cầu high availability trước sự cố datacenter. Azure Backup dùng sao lưu và khôi phục; Resource Groups tổ chức, quản lý tài nguyên; Reserved Instances giúp tiết kiệm chi phí theo cam kết sử dụng.

**Bẫy:** Chỉ triển khai vào một zone không tạo khả năng chịu lỗi khi zone đó ngừng hoạt động. Cần cấu hình nhiều zone hoặc dùng dịch vụ zone-redundant phù hợp, bao gồm các dependency của ứng dụng. Khả năng hỗ trợ phụ thuộc region và dịch vụ. Availability Zones không tự bảo vệ trước sự cố toàn region; khi đó cần thiết kế multi-region.
