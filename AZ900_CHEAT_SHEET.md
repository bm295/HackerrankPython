# AZ-900 — Ghi chú ôn tập

## Tra nhanh theo keyword trong câu hỏi

Keywords giúp tìm phần hướng dẫn phù hợp; luôn đọc yêu cầu và điều kiện trước khi chọn đáp án.

| English keywords / scenario cues | Bài học | Gợi ý suy luận |
| --- | --- | --- |
| hardware failures, data center outages, remain operational, Availability Zones | [AZ900-001](#az900-001) | Cần high availability qua nhiều zone trong cùng region; backup chỉ hỗ trợ khôi phục. |
| cloud arrangement, support infrastructure in a data center | [AZ900-002](#az900-002) | Xác định ai vận hành hạ tầng vật lý và phân biệt cloud deployment model với serverless. |
| Infrastructure as Code, ARM, scripting language, Terraform, repeatability | [AZ900-003](#az900-003) | Phân biệt dịch vụ triển khai, ngôn ngữ khai báo và công cụ IaC. |
| frequently accessed, monthly reports, historical backups, Hot, Cold, Archive | [AZ900-004](#az900-004) | Cân nhắc tần suất đọc, thời gian giữ, phí truy xuất và độ trễ rehydration. |
| distributing traffic, multiple instances, availability zones within a region | [AZ900-005](#az900-005) | Load Balancer chia traffic tới backend khỏe mạnh; kiểm tra cấu hình đa zone và tách biệt autoscale. |
| various formats, Blob, Table, Queue, File, Storage Account | [AZ900-006](#az900-006) | Nhận diện nhóm dịch vụ Azure Storage và phân biệt Table Storage với SQL Database. |
| fully serverless compute, Functions, Virtual Machines, triggers | [AZ900-007](#az900-007) | Functions chạy logic theo trigger; VM là IaaS; Cosmos DB serverless phục vụ database. |
| web tier, 250 GB, dedicated compute, custom domain, SSL | [AZ900-008](#az900-008) | Xác định 250 GB là quota App Service hay dữ liệu ở Azure Storage riêng trước khi chọn tier. |
| consumption-based, pay only, capacity utilized, reservation, fixed-cost serverless | [AZ900-009](#az900-009) | Xác định đơn vị tính phí và phạm vi cam kết; consumption bao gồm nhiều loại tài nguyên. |

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

<a id="az900-003"></a>

## AZ900-003 | Phân biệt ARM, ARM templates, Bicep và Terraform

**Dấu hiệu:** Infrastructure as Code, scripting language, repeatability, manual Portal changes, Terraform providers.

**Nhóm kiến thức:** Describe Azure management and governance → managing and deploying Azure resources → IaC, ARM và ARM templates.

**Liên hệ lý thuyết:** Azure Resource Manager (ARM) là dịch vụ triển khai và quản lý tài nguyên Azure. ARM templates là tệp JSON khai báo tài nguyên và cấu hình. Bicep là ngôn ngữ khai báo cho tài nguyên Azure. Terraform là công cụ IaC hỗ trợ Azure và các nền tảng khác thông qua provider.

**Cách phân tích đáp án:** IaC mô tả hạ tầng bằng mã để triển khai nhất quán và lặp lại được. Thay đổi thông thường đi qua mã cấu hình và quy trình triển khai.

**Bẫy:** Cụm “ARM is a scripting language” nhầm dịch vụ ARM với cách viết cấu hình hạ tầng. Thay đổi tài nguyên trực tiếp qua Portal có thể khiến cấu hình thực tế lệch khỏi mã.

<a id="az900-004"></a>

## AZ900-004 | Chọn Blob Storage access tier theo tần suất và độ trễ

**Dấu hiệu:** Frequently accessed transactions, monthly reports, historical backups, storage cost optimization.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure storage services → storage tiers.

**Liên hệ lý thuyết:** Hot phù hợp dữ liệu truy cập thường xuyên. Cool và Cold giữ dữ liệu online, truy cập nhanh, giảm chi phí lưu nhưng tăng chi phí đọc. Archive dành cho dữ liệu rất ít truy cập và chấp nhận chờ hàng giờ để rehydrate trước khi đọc.

**Cách phân tích đáp án:** Với tổ hợp Hot/Cold/Archive cho giao dịch thường xuyên/báo cáo tháng/backup dài hạn, đây là lựa chọn hợp lý nhất trong các phương án nếu báo cáo được giữ đủ lâu và backup chấp nhận độ trễ khôi phục. Dùng Hot cho backup ít đọc làm tăng chi phí lưu.

**Bẫy:** “Báo cáo tháng” không tự quyết định Cold. Cần xét dung lượng đọc, số lần đọc, thời gian giữ và chi phí giao dịch. Thời gian lưu tối thiểu tính phí thường là Cool 30 ngày, Cold 90 ngày trên tài khoản general-purpose v2, Archive 180 ngày. Xóa hoặc chuyển tier sớm có thể phát sinh phí. Archive yêu cầu rehydration nên không phù hợp yêu cầu đọc ngay.

<a id="az900-005"></a>

## AZ900-005 | Phân phối traffic đa zone bằng Azure Load Balancer

**Dấu hiệu:** Automatically distributing traffic, multiple instances, different availability zones within a region.

**Nhóm kiến thức:** Describe Azure architecture and services → networking → load balancing.

**Liên hệ lý thuyết:** Azure Load Balancer phân phối traffic TCP/UDP ở Layer 4 tới các instance khỏe mạnh trong backend pool. Health probes phát hiện backend lỗi để ngừng gửi kết nối mới đến backend đó.

**Cách phân tích đáp án:** Chọn Load Balancer khi yêu cầu chính là chia traffic giữa nhiều instance. Virtual Network cung cấp mạng riêng và kết nối. Logic Apps tự động hóa workflow và tích hợp. ARM triển khai và quản lý tài nguyên.

**Bẫy:** Muốn chịu lỗi zone cần backend trải qua nhiều zone và frontend zone-redundant phù hợp. Load Balancer không tự tạo thêm VM hoặc tự bố trí backend đa zone. Autoscale tăng/giảm số instance là cơ chế riêng.

<a id="az900-006"></a>

## AZ900-006 | Storage Account và bốn dịch vụ lưu trữ

**Dấu hiệu:** Store data in various formats; Blob, Table, Queue, File Storage.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure storage services → storage accounts.

**Liên hệ lý thuyết:** Storage Account cung cấp namespace và phạm vi quản lý cho dữ liệu Azure Storage. Standard general-purpose v2 hỗ trợ Blob, Table, Queue và Azure Files. Blob lưu object như ảnh, video, backup; Table lưu dữ liệu NoSQL key-value; Queue lưu message cho xử lý bất đồng bộ; Files cung cấp file share.

**Cách phân tích đáp án:** Với danh sách Blob/Table/Queue/File, chọn Azure Storage Account. Azure SQL Database là cơ sở dữ liệu quan hệ; Virtual Machines cung cấp compute; Microsoft Entra ID quản lý danh tính và truy cập.

**Bẫy:** Từ “Table” trong Table Storage chỉ dịch vụ NoSQL, khác bảng quan hệ trong SQL Database. Loại Storage Account quyết định dịch vụ hỗ trợ; các tài khoản premium chuyên dụng không đồng thời hỗ trợ cả bốn dịch vụ.

<a id="az900-007"></a>

## AZ900-007 | Azure Functions và serverless compute

**Dấu hiệu:** Serverless compute, event-driven code, triggers.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure compute → functions.

**Liên hệ lý thuyết:** Azure Functions chạy mã ứng dụng theo trigger như HTTP, timer hoặc message mà người dùng không trực tiếp quản lý máy chủ nền. Azure Virtual Machines là IaaS, khách hàng quản lý hệ điều hành khách và phần mềm.

**Cách phân tích đáp án:** Chọn Functions khi cần serverless compute để thực thi logic ứng dụng. Key Vault quản lý secrets, keys và certificates. Cosmos DB là database và có chế độ serverless. Cần đọc cả từ “compute” và phạm vi “listed”.

**Bẫy:** “Serverless” vẫn sử dụng máy chủ do nhà cung cấp quản lý. Functions có nhiều hosting plan nên cách tính phí và mở rộng phụ thuộc plan. Không suy rộng rằng Functions là dịch vụ serverless duy nhất của Azure.

<a id="az900-008"></a>

## AZ900-008 | App Service plan và dung lượng lưu trữ bên ngoài

**Dấu hiệu:** Web tier, custom domain, SSL, dedicated compute, 250 GB, minimize costs.

**Nhóm kiến thức:** Describe Azure architecture and services → compute → web app hosting.

**Liên hệ lý thuyết:** Basic, Standard và Premium là các tier dedicated compute của App Service. Quota storage của plan và dung lượng Azure Storage riêng là hai phạm vi khác nhau. Bảng quota App Service được kiểm tra ngày 07/11/2026 ghi Basic 10 GB, Standard 50 GB, Premium 250 GB, Shared 1 GB.

**Cách phân tích đáp án:** Nếu chính App Service plan phải cung cấp 250 GB thì chọn Premium trong bốn lựa chọn Shared/Basic/Standard/Premium. Standard không đạt quota đó. Nếu file đặt trong Blob Storage bên ngoài, không dùng 250 GB này để tự động ép chọn Premium; xét riêng yêu cầu compute, TLS và tính năng của web app.

**Bẫy:** Custom domain và SSL không tự buộc chọn Standard hay Premium; cần phân biệt SNI TLS với IP-based TLS. Các quota và tính năng phụ thuộc SKU và phiên bản, cần kiểm tra khi áp dụng. Đề trộn Power Apps Portal với việc chọn App Service plan cần làm rõ mô hình hosting trước khi triển khai thực tế.

<a id="az900-009"></a>

## AZ900-009 | Consumption-based pricing và phạm vi reservation

**Dấu hiệu:** Pay only for data sent, capacity utilized, long-term reservation, serverless fixed cost.

**Nhóm kiến thức:** Describe cloud concepts → consumption-based model và cloud pricing models.

**Liên hệ lý thuyết:** Consumption-based pricing tính phí theo đơn vị sử dụng có thể là thời gian compute, dung lượng lưu, request hoặc data transfer. Giảm lượng tài nguyên tính phí thường giảm chi phí biến đổi. Serverless Consumption tính phí theo hoạt động sử dụng thay vì một tổng phí cố định.

**Cách phân tích đáp án:** Phát biểu chỉ trả data transfer bỏ qua compute và storage nên sai. Phát biểu serverless là fixed-cost consumption cũng sai. Reservation là cam kết kỳ hạn để được giảm giá cho usage phù hợp trong phạm vi đã mua, thay cho đơn giá pay-as-you-go của phần đó.

**Bẫy:** Giảm CPU utilization bên trong VM đang được cấp phát không tự giảm phí compute của VM. Reservation không bao phủ mọi khoản trong hóa đơn; VM reservation vẫn có thể phát sinh phí storage, networking và phần mềm riêng. Các hosting plan serverless khác nhau có cách tính phí khác nhau.
