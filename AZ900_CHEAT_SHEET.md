# AZ-900 — Ghi chú ôn tập

## Tra nhanh theo keyword trong câu hỏi

Keywords giúp tìm phần hướng dẫn phù hợp; luôn đọc yêu cầu và điều kiện trước khi chọn đáp án.

| English keywords / scenario cues | Bài học | Gợi ý suy luận |
| --- | --- | --- |
| hardware failures, data center outages, remain operational, Availability Zones | [AZ900-001](#az900-001) | Cần high availability qua nhiều zone trong cùng region; backup chỉ hỗ trợ khôi phục. |
| cloud arrangement, support infrastructure in a data center | [AZ900-002](#az900-002) | Xác định ai vận hành hạ tầng vật lý và phân biệt cloud deployment model với serverless. |
| Infrastructure as Code, declarative templates, ARM, Bicep, Terraform, repeatability | [AZ900-003](#az900-003) | Phân biệt dịch vụ triển khai, ngôn ngữ khai báo và công cụ IaC. |
| frequently accessed, monthly reports, historical backups, Hot, Cold, Archive | [AZ900-004](#az900-004) | Cân nhắc tần suất đọc, thời gian giữ, phí truy xuất và độ trễ rehydration. |
| distributing traffic, multiple instances, availability zones within a region | [AZ900-005](#az900-005) | Load Balancer chia traffic tới backend khỏe mạnh; kiểm tra cấu hình đa zone và tách biệt autoscale. |
| various formats, Blob, Table, Queue, File, Storage Account | [AZ900-006](#az900-006) | Nhận diện nhóm dịch vụ Azure Storage và phân biệt Table Storage với SQL Database. |
| fully serverless compute, Functions, triggers, storage account, language, event-driven scaling | [AZ900-007](#az900-007) | Phân biệt hạ tầng máy chủ với storage, trigger và cách scale theo hosting plan. |
| web tier, 250 GB, dedicated compute, custom domain, SSL | [AZ900-008](#az900-008) | Xác định 250 GB là quota App Service hay dữ liệu ở Azure Storage riêng trước khi chọn tier. |
| consumption-based, pay only, capacity utilized, reservation, fixed-cost serverless | [AZ900-009](#az900-009) | Xác định đơn vị tính phí và phạm vi cam kết; consumption bao gồm nhiều loại tài nguyên. |
| sovereign region, national cloud, China, East US, Germany | [AZ900-010](#az900-010) | Phân biệt loại cloud với đơn vị vận hành; kiểm tra thông tin Azure Germany cũ. |
| varying traffic, lunchtime peaks, schedule, VM Scale Sets, Availability Sets | [AZ900-011](#az900-011) | Tải biến động cần autoscale bằng VMSS; Availability Sets xử lý phân tán lỗi và bảo trì. |
| numerous subscriptions, business units, governance, delegate management | [AZ900-012](#az900-012) | Management Groups tạo scope trên subscription để tổ chức và kế thừa Policy/RBAC. |
| Azure Policy, organizational standards, compliance, audit, deny | [AZ900-013](#az900-013) | Kiểm tra cấu hình theo quy tắc và effect; phân biệt Policy với RBAC, chi phí và monitoring. |
| Azure CLI, list all VMs, az vm list | [AZ900-014](#az900-014) | az + nhóm vm + thao tác list; kiểm tra subscription và resource-group scope. |
| telemetry, performance and health, alerts, user experiences, NOT use | [AZ900-015](#az900-015) | Monitor là nền tảng, Log Analytics truy vấn logs, Application Insights là APM; DevOps phục vụ phát triển. |
| Advisor, recommendations, cost saving, reliability, real-time monitoring | [AZ900-016](#az900-016) | Advisor đề xuất tối ưu; Monitor theo dõi telemetry và cảnh báo. |
| match Region, Availability Zone, Fault Domain, Georedundancy | [AZ900-017](#az900-017) | Phân biệt phạm vi địa lý, zone độc lập, phần cứng chung và sao chép liên region. |
| direct OS control, specialized software, isolated environment, Web Apps, consistent application performance | [AZ900-018](#az900-018) | So sánh quyền kiểm soát guest OS, hạ tầng được quản lý và mức cô lập. |
| service incidents, outages, status updates, incident details, maintenance | [AZ900-019](#az900-019) | Service Health thông báo sự cố nền tảng; Monitor phân tích telemetry workload. |
| centralized monitoring, alerts, automated response, unified console, Azure Portal | [AZ900-020](#az900-020) | Monitor xử lý telemetry, alerts và hành động tích hợp; Portal là giao diện web quản lý tài nguyên. |
| TCO calculator, cost savings, on-premises versus Azure, first step | [AZ900-021](#az900-021) | TCO so sánh tổng chi phí; Pricing calculator ước tính chi phí dịch vụ Azure. |
| containers dependencies, Docker, full OS, microservices hosting, independent scaling, Kubernetes, AKS | [AZ900-022](#az900-022) | Container image đóng gói mã và dependencies. Kubernetes điều phối container, còn AKS cung cấp Kubernetes được quản lý trên Azure. |
| slow performance, delayed response, latency, initial concern | [AZ900-023](#az900-023) | Latency mô tả độ trễ; cần đo để tìm nguyên nhân chậm. |
| regulated workloads, move to Azure, retain existing infrastructure, hybrid | [AZ900-024](#az900-024) | Hybrid phù hợp khi kết hợp public với private/on-premises theo yêu cầu workload. |
| spare capacity, tolerate interruptions, batch, commit in advance, Spot, Reservations | [AZ900-025](#az900-025) | Spot dùng công suất dư có thể bị thu hồi; Reservations giảm giá theo cam kết thời hạn. |
| resource locks, accidental deletion, modification, shared resource group, ReadOnly, CanNotDelete | [AZ900-026](#az900-026) | Locks bảo vệ thao tác quản lý; RBAC xác định quyền theo danh tính. |
| first required step, trial account, resource group, multiple regions, nested groups | [AZ900-027](#az900-027) | Subscription chứa Resource Group. Nhóm có thể chứa tài nguyên ở nhiều region. |
| reliability, predictability, unpredictable costs, business continuity, compliance | [AZ900-028](#az900-028) | Predictability là dự báo performance/cost; compliance thuộc security/governance. |
| large amounts of unstructured data, documents, images, videos, backups | [AZ900-029](#az900-029) | Chọn Blob cho object storage; Files khi cần file share SMB/NFS. |
| Public Preview, support, SLA, General Availability | [AZ900-030](#az900-030) | Kiểm tra điều khoản của tính năng. Public Preview thường không có SLA. |
| Azure Security Center, Microsoft Defender for Cloud, security posture, regulatory compliance, potential threats | [AZ900-031](#az900-031) | Đánh giá cấu hình, khoảng trống tuân thủ và khả năng bảo vệ workload trước mối đe dọa. |
| region-wide failure, unplanned outage, disaster recovery, elasticity and scalability | [AZ900-032](#az900-032) | Lập kế hoạch khôi phục tại region khác và kiểm tra công suất region đích. |
| remote workers, Windows virtual desktop, personalized access, RemoteApp | [AZ900-033](#az900-033) | Chọn AVD khi cần cung cấp desktop Windows hoặc ứng dụng từ xa cho người dùng. |
| isolated network environments, departments, segmentation, VNet, subnet | [AZ900-034](#az900-034) | VNet riêng tạo ranh giới mạng. Subnet chia mạng và có thể áp quy tắc lọc lưu lượng. |
| data discovery, cataloging, data governance, lineage, Azure Purview | [AZ900-035](#az900-035) | Dùng Purview để thu thập metadata và tìm kiếm tài sản dữ liệu. |
| end-of-quarter traffic spike, variable demand, manage cost, elasticity | [AZ900-036](#az900-036) | Tăng công suất khi tải lên và giảm khi tải hạ để tránh giữ công suất dư. |
| Azure pricing factors, datacenter location, VM size, inter-region bandwidth, ingress, egress | [AZ900-037](#az900-037) | Tách giá tài nguyên theo region và SKU khỏi phí truyền dữ liệu liên vùng. |
| large file set, on-premises server, Azure Storage, efficient transfer, AzCopy | [AZ900-038](#az900-038) | Sao chép trực tiếp dùng AzCopy. Data Factory phù hợp pipeline, File Sync phù hợp đồng bộ file share. |
| centralized management, hybrid infrastructure, multicloud Kubernetes, Azure Arc, compliance | [AZ900-039](#az900-039) | Azure Arc mở rộng quản lý Azure tới tài nguyên bên ngoài Azure để quản trị tập trung. |
| complex calculations, large datasets, VM resource configuration, CPU cores and memory | [AZ900-040](#az900-040) | Chọn vCPU và RAM theo nhu cầu tính toán và dữ liệu đang xử lý. |
| Microsoft 365, Blob Storage, SaaS, PaaS, IaaS, service models | [AZ900-041](#az900-041) | Phân loại từng dịch vụ theo trách nhiệm quản lý. Microsoft 365 là SaaS, Blob Storage là PaaS. |
| regional outage, region pairs, data residency, geo-replication | [AZ900-042](#az900-042) | Chọn vị trí dữ liệu phù hợp và cấu hình replication cùng kế hoạch khôi phục theo dịch vụ. |
| public endpoints, private endpoints, private IP, VNet, enabled by default | [AZ900-043](#az900-043) | Private endpoint phải tạo/cấu hình; giảm phơi bày Internet nhưng cần kiểm soát public network access riêng. |
| ExpressRoute, on-premises datacenter, private dedicated connection, bypass public internet | [AZ900-044](#az900-044) | ExpressRoute kết nối riêng tới Azure; private connectivity không đồng nghĩa mã hóa mặc định. |


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

**Dấu hiệu:** Infrastructure as Code, declarative templates, ARM or Bicep, infrastructure components, scripting language, repeatability, manual Portal changes, Terraform providers.

**Nhóm kiến thức:** Describe Azure management and governance → managing and deploying Azure resources → IaC, ARM và ARM templates.

**Liên hệ lý thuyết:** Azure Resource Manager (ARM) là dịch vụ triển khai và quản lý tài nguyên Azure. ARM templates là tệp JSON khai báo tài nguyên và cấu hình. Bicep là ngôn ngữ khai báo được chuyển thành ARM template JSON khi triển khai. Terraform là công cụ IaC hỗ trợ Azure và các nền tảng khác thông qua provider.

**Cách phân tích đáp án:** IaC mô tả hạ tầng bằng mã để triển khai nhất quán và lặp lại được. Thay đổi thông thường đi qua mã cấu hình và quy trình triển khai.

**Bẫy:** Khi đáp án gọi ARM templates là “scripts”, hiểu chính xác là tệp JSON dùng cú pháp khai báo trạng thái mong muốn; ARM xử lý triển khai và dependency. Templates hỗ trợ nhiều loại tài nguyên, không chỉ VM. Cụm “ARM is a scripting language” nhầm dịch vụ ARM với cách viết cấu hình hạ tầng. Thay đổi tài nguyên trực tiếp qua Portal có thể khiến cấu hình thực tế lệch khỏi mã.

**Ví dụ AKS:** Dùng ARM template hoặc Bicep để tạo cụm AKS như một tài nguyên Azure. Dùng Kubernetes manifest để khai báo các đối tượng chạy bên trong cụm, chẳng hạn Deployment và Service.

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

**Dấu hiệu:** Serverless compute, event-driven code, HTTP trigger, short tasks, minimal management overhead.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure compute → functions.

**Liên hệ lý thuyết:** Azure Functions chạy mã ứng dụng theo trigger như HTTP, timer hoặc message mà người dùng không trực tiếp quản lý máy chủ nền. Azure Virtual Machines là IaaS, khách hàng quản lý hệ điều hành khách và phần mềm.

**Cách phân tích đáp án:** Chọn Functions khi cần serverless compute để thực thi logic ứng dụng. Key Vault quản lý secrets, keys và certificates. Cosmos DB là database và có chế độ serverless. Cần đọc cả từ “compute” và phạm vi “listed”.

**Bẫy:** “Serverless” vẫn sử dụng máy chủ do nhà cung cấp quản lý. Function app vẫn cần quyền truy cập Azure Storage account mặc định. Azure Functions hỗ trợ nhiều ngôn ngữ như C#, JavaScript và Python ở cấp nền tảng. Một function app chọn runtime ngôn ngữ khi cấu hình. Flex Consumption hỗ trợ mở rộng theo tải sự kiện, còn cách scale và tính phí phụ thuộc hosting plan. Azure cũng có các dịch vụ serverless khác.

**Tình huống HTTP:** Với API hoặc webhook nhẹ xử lý ngắn, dùng HTTP trigger để gọi hàm khi có request và trả kết quả trực tiếp. Flex Consumption tự điều chỉnh số instance theo tải HTTP và hỗ trợ giữ instance luôn sẵn sàng khi cần giảm độ trễ khởi động.

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

**Đối chiếu key của đề:** Ảnh kết quả LinkedIn cho tổ hợp C,D, trong khi A cũng sai rõ ràng vì từ only giới hạn chi phí vào truyền dữ liệu. C thiếu phạm vi: chỉ phần usage được reservation bao phủ mới thay đơn giá PAYG; phần ngoài phạm vi vẫn tính riêng. Vì đề yêu cầu đúng hai lựa chọn nhưng có nhiều phát biểu sai theo cách đọc rộng, ghi nhận câu mơ hồ và loại khỏi đánh giá domain. Không khẳng định A,D hay C,D là tổ hợp duy nhất đúng về kỹ thuật.

**Bẫy:** Giảm CPU utilization bên trong VM đang được cấp phát không tự giảm phí compute của VM. Reservation không bao phủ mọi khoản trong hóa đơn; VM reservation vẫn có thể phát sinh phí storage, networking và phần mềm riêng. Các hosting plan serverless khác nhau có cách tính phí khác nhau.

<a id="az900-010"></a>

## AZ900-010 | Sovereign cloud, region public và đơn vị vận hành

**Dấu hiệu:** Sovereign region, national cloud, Azure China, US Government, East US, Azure Germany.

**Nhóm kiến thức:** Describe Azure architecture and services → core architectural components → regions và sovereign clouds.

**Liên hệ lý thuyết:** Sovereign/national cloud là môi trường Azure tách biệt để đáp ứng yêu cầu chủ quyền dữ liệu và tuân thủ. Azure Government và Azure China thuộc nhóm này; Azure China do 21Vianet vận hành. East US là region của Azure public cloud.

**Cách phân tích đáp án:** Nếu hỏi lựa chọn nào không thuộc sovereign cloud, East US phù hợp. Nếu hỏi Microsoft không trực tiếp vận hành môi trường nào, Azure China phù hợp vì 21Vianet vận hành. Phải phân biệt hai tiêu chí.

**Bẫy:** Câu hỏi dùng “Microsoft does not manage sovereign region” mơ hồ giữa phân loại cloud và đơn vị vận hành. Azure Germany sovereign cloud cũ đã đóng ngày 29/10/2021; các region public hiện tại ở Đức là phạm vi khác. Không dùng câu cũ có các mơ hồ này để đánh giá readiness.

<a id="az900-011"></a>

## AZ900-011 | VM Scale Sets và Availability Sets

**Dấu hiệu:** Varying traffic, lunchtime peaks, scheduled scaling, efficient resource management, scalable and fault-tolerant.

**Nhóm kiến thức:** Describe Azure architecture and services → compute → VM Scale Sets và availability options.

**Liên hệ lý thuyết:** Virtual Machine Scale Sets quản lý một nhóm VM và hỗ trợ autoscale theo metric hoặc lịch. Availability Sets phân bố VM qua fault domains và update domains để giảm nguy cơ nhiều VM cùng gián đoạn vì lỗi hạ tầng hoặc bảo trì.

**Cách phân tích đáp án:** Khi đề vừa cần high availability vừa cần tăng giảm số VM theo tải, chọn VM Scale Sets. Có thể đặt lịch tăng VM trước giờ cao điểm và giảm khi tải thấp. Azure Virtual Desktop cung cấp desktop/ứng dụng từ xa. VM riêng lẻ cần thêm cơ chế quản lý và mở rộng.

**Bẫy:** Availability Sets không tự tăng giảm số lượng VM theo nhu cầu. VMSS cần cấu hình autoscale và triển khai nhiều instance, kết hợp load balancing và bố trí fault domain/zone phù hợp để đạt mục tiêu chịu lỗi. Scale Sets không tự đồng bộ dữ liệu ứng dụng giữa các VM.

<a id="az900-012"></a>

## AZ900-012 | Management Groups quản lý nhiều subscription

**Dấu hiệu:** Numerous subscriptions, multiple business units, organize resources, enforce policies, delegate management.

**Nhóm kiến thức:** Describe Azure architecture and services → core architectural components → management groups và resource hierarchy. Có liên quan governance và access control.

**Liên hệ lý thuyết:** Management Groups tổ chức các subscription thành cây phân cấp, cung cấp scope phía trên subscription. Azure Policy assignments và Azure RBAC role assignments đặt tại management group được kế thừa xuống các scope con theo cơ chế tương ứng.

**Cách phân tích đáp án:** Chọn Management Groups khi cần quản trị và phân quyền thống nhất trên nhiều subscription. Azure Policy định nghĩa và đánh giá/áp điều kiện tuân thủ; Management Groups cung cấp cấu trúc và scope để áp dụng. ARM templates khai báo triển khai hạ tầng; Functions thực thi mã theo trigger.

**Bẫy:** Resource Group nằm trong một subscription. Management Group chứa subscription và management group con, không trực tiếp chứa VM hay resource group. Management Groups tự nó không định nghĩa mọi quy tắc hoặc cấp quyền; cần cấu hình Policy và RBAC tại scope phù hợp.

<a id="az900-013"></a>

## AZ900-013 | Mục đích của Azure Policy

**Dấu hiệu:** Organizational standards, compliance, enforce rules, allowed locations, required tags.

**Nhóm kiến thức:** Describe Azure management and governance → governance and compliance → Azure Policy.

**Liên hệ lý thuyết:** Azure Policy đánh giá cấu hình tài nguyên theo quy tắc tổ chức và áp dụng hành vi tương ứng với policy effect. Ví dụ giới hạn region được phép, kiểm tra tag hoặc cấu hình bảo mật.

**Cách phân tích đáp án:** Chọn tiêu chuẩn tổ chức và compliance khi hỏi mục đích chính. Cost Management theo dõi và phân tích chi phí; CI/CD tự động hóa phát triển và triển khai; Azure Monitor thu thập telemetry và cảnh báo. Policy có thể hỗ trợ kiểm soát chi phí qua giới hạn SKU nhưng mục đích rộng hơn là governance.

**Bẫy:** Audit chỉ ghi nhận trạng thái tuân thủ; Deny chặn yêu cầu không phù hợp. Tài nguyên hiện hữu không tự được sửa bởi mọi policy; remediation phụ thuộc effect và cấu hình. RBAC kiểm soát ai được làm gì, Policy kiểm tra cấu hình tài nguyên có đáp ứng quy tắc hay không. Có thể gán Policy tại Management Group để áp xuống nhiều subscription.

<a id="az900-014"></a>

## AZ900-014 | Liệt kê VM bằng Azure CLI

**Dấu hiệu:** Azure CLI, list all virtual machines, subscription.

**Nhóm kiến thức:** Describe Azure management and governance → managing and deploying resources → Azure CLI.

**Liên hệ lý thuyết:** Azure CLI hiện tại dùng tiền tố `az`. Lệnh `az vm list` liệt kê VM trong subscription được chọn, với phạm vi chịu ảnh hưởng của tùy chọn và cấu hình mặc định.

**Cách phân tích đáp án:** Cấu trúc là `az <nhóm lệnh> <thao tác>`; VM dùng nhóm `vm`, liệt kê dùng `list`. Có thể thêm `--output table` để hiển thị bảng, `--subscription <ID>` để chọn subscription, hoặc `--resource-group <tên>` để giới hạn một resource group. PowerShell dùng `Get-AzVM`.

**Bẫy:** `azure vm list` thuộc cú pháp CLI cũ. `azure list vm` và `az list virtualmachines` không phải cú pháp hiện tại để liệt kê VM. Một lệnh không mặc nhiên quét mọi subscription; kết quả phụ thuộc quyền truy cập và subscription đang chọn.

<a id="az900-015"></a>

## AZ900-015 | Monitor, Log Analytics, Application Insights và Azure DevOps

**Dấu hiệu:** Performance and health, telemetry, alerts, user experiences, NOT use.

**Nhóm kiến thức:** Describe Azure management and governance → monitoring tools → Azure Monitor, Log Analytics và Application Insights.

**Liên hệ lý thuyết:** Azure Monitor thu thập, phân tích và phản ứng với telemetry. Log Analytics là công cụ truy vấn log bằng KQL trong Azure Monitor. Application Insights là tính năng APM của Azure Monitor, theo dõi request, lỗi, dependency, hiệu năng và trải nghiệm người dùng.

**Cách phân tích đáp án:** Nếu hỏi dịch vụ không phù hợp làm công cụ chính cho giám sát runtime, chọn Azure DevOps trong nhóm lựa chọn này. Azure DevOps cung cấp công cụ quản lý mã nguồn, công việc và CI/CD. Ba lựa chọn còn lại là các phần của hệ sinh thái monitoring, có vai trò bổ trợ.

**Bẫy:** Azure DevOps có thể tích hợp alerts hoặc dùng dữ liệu monitoring trong quy trình triển khai; điều đó không biến nó thành công cụ APM chính. Telemetry cần được thu thập và cấu hình phù hợp; không mặc nhiên có toàn bộ log, trace và dữ liệu người dùng ngay khi tạo tài nguyên.

<a id="az900-016"></a>

## AZ900-016 | Azure Advisor và Azure Monitor

**Dấu hiệu:** NOT a purpose of Advisor, real-time performance monitoring, optimization recommendations, cost-saving opportunities, reliability.

**Nhóm kiến thức:** Describe Azure management and governance → monitoring tools → Azure Advisor.

**Liên hệ lý thuyết:** Advisor phân tích cấu hình tài nguyên và usage telemetry để đưa khuyến nghị cá nhân hóa theo best practices. Năm nhóm khuyến nghị là Reliability, Security, Performance, Cost và Operational excellence.

**Cách phân tích đáp án:** Chọn real-time performance monitoring khi hỏi chức năng không thuộc mục đích chính của Advisor. Azure Monitor phục vụ thu thập telemetry, phân tích và cảnh báo. Advisor đưa đề xuất tối ưu hiệu năng, giảm chi phí và cải thiện độ tin cậy dựa trên dữ liệu và cấu hình.

**Bẫy:** Advisor dùng telemetry không có nghĩa nó là công cụ dashboard/alert giám sát thời gian thực. Nhóm Performance của Advisor nói về khuyến nghị cải thiện. Khuyến nghị reliability cần được xem xét và triển khai phù hợp để mang lại hiệu quả.

<a id="az900-017"></a>

## AZ900-017 | Region, Zone, Fault Domain và Georedundancy

**Dấu hiệu:** Match datacenter concepts; common power source and network switch; different geographic regions.

**Nhóm kiến thức:** Describe Azure architecture and services → core architectural components.

**Liên hệ lý thuyết:** Region là khu vực triển khai gồm các datacenter kết nối với nhau. Availability Zone là nhóm datacenter tách biệt trong cùng region với điện, mạng và làm mát độc lập. Fault Domain nhóm phần cứng dùng chung nguồn điện và network switch. Georedundancy tạo bản sao tại các region khác nhau.

**Cách phân tích đáp án:** Với bốn mô tả theo thứ tự cô lập zone, chung điện/switch, khu vực địa lý và sao chép liên region, ghép Availability Zone → Fault Domain → Region → Georedundancy.

**Bẫy:** Availability Zone không phải một phần bên trong một datacenter. Lợi ích fault domain có được khi phân bố instance qua nhiều domain. Geo replication và failover phụ thuộc dịch vụ và cấu hình, không mặc nhiên đồng bộ tức thời hay không mất dữ liệu.

<a id="az900-018"></a>

## AZ900-018 | Chọn VM khi cần kiểm soát hệ điều hành

**Dấu hiệu:** Direct control over operating system, specialized software installations, complex computations, isolated hosting.

**Nhóm kiến thức:** Describe Azure architecture and services → compute → Virtual Machines, containers và Web Apps.

**Liên hệ lý thuyết:** Azure VM cung cấp guest OS có thể cấu hình, cài phần mềm và vá lỗi theo nhu cầu. Microsoft quản lý phần cứng vật lý. Khách hàng quản lý guest OS và ứng dụng. Azure Web Apps (App Service) là PaaS, Microsoft quản lý hạ tầng và hệ điều hành nền để khách hàng tập trung triển khai ứng dụng.

**Cách phân tích đáp án:** Yêu cầu kiểm soát trực tiếp OS và cài phần mềm chuyên dụng hướng tới VM. Functions chạy mã theo trigger. ACI chạy container trên hạ tầng được quản lý. AKS điều phối container, có khả năng cấu hình node nhưng không phải lựa chọn đơn giản nhất khi đề chỉ yêu cầu môi trường OS riêng.

**Bẫy:** Từ isolated hoặc sensitive data không đủ để chọn VM. Container ở chế độ cô lập tiến trình thường dùng chung kernel của host, còn VM có kernel riêng. Image giúp môi trường chạy nhất quán. Hiệu năng còn phụ thuộc CPU, RAM và tải thực tế. VM không mặc nhiên cấp host vật lý độc quyền hay bảo đảm tuân thủ tài chính; cần cấu hình bảo mật và vận hành phù hợp.

<a id="az900-019"></a>

## AZ900-019 | Service Health và Monitor

**Dấu hiệu:** Azure service incidents, outages, service status updates, incident details, planned maintenance.

**Nhóm kiến thức:** Describe Azure management and governance → monitoring tools → Azure Service Health.

**Liên hệ lý thuyết:** Service Health cung cấp thông tin sự cố dịch vụ Azure, bảo trì và advisories liên quan đến subscription, region và dịch vụ đang dùng. Có thể cấu hình alert để nhận thông báo. Monitor thu thập metrics, logs và telemetry của workload để phân tích và cảnh báo.

**Cách phân tích đáp án:** Sự cố nền tảng được Azure công bố hướng tới Service Health. CPU cao, lỗi request hay độ trễ ứng dụng hướng tới Monitor/Application Insights. ARM triển khai và quản lý tài nguyên; Traffic Manager định tuyến DNS giữa các endpoint.

**Bẫy:** Service Health alerts dùng cơ chế Azure Monitor alerts, nhưng nguồn thông tin sự cố nền tảng trong câu hỏi là Service Health. Resource Health theo dõi tài nguyên cụ thể; Azure Status cung cấp thông tin công khai về sự cố diện rộng. Cập nhật Service Health gần thời gian thực khi Microsoft phát hiện và xác nhận vấn đề.

<a id="az900-020"></a>

## AZ900-020 | Phân biệt Azure Monitor và Azure Portal

**Dấu hiệu:** Centralized monitoring, telemetry, alerts, automated response, unified web console, graphical interface.

**Nhóm kiến thức:** Describe Azure management and governance → monitoring tools và resource management tools.

**Liên hệ lý thuyết:** Azure Monitor thu thập và phân tích metrics, logs, traces để theo dõi sức khỏe, hiệu năng của ứng dụng và hạ tầng. Alert rules phát hiện điều kiện; action groups gửi thông báo hoặc kích hoạt workflow, webhook, runbook và các hành động tích hợp. Azure Portal là giao diện web hợp nhất để tạo, quản lý tài nguyên và truy cập các tính năng Monitor cùng nhiều dịch vụ khác.

**Cách phân tích đáp án:** Với câu hỏi dịch vụ giám sát tập trung và automation vận hành, chọn Azure Monitor trong bộ VM/Entra ID/Portal/Monitor. Key LinkedIn câu 14 xác nhận Monitor; lời giải Portal trước đây đã được sửa. Khi đề hỏi giao diện web/GUI để tạo hoặc quản lý tài nguyên, chọn Azure Portal. VM cung cấp compute; Entra ID cung cấp quản lý danh tính và truy cập.

**Bẫy:** Portal hiển thị màn hình của Monitor nhưng không thay thế dịch vụ thu thập telemetry, đánh giá alerts và kích hoạt hành động. Từ management riêng lẻ không đủ quyết định; đọc mục tiêu cụ thể. Monitor không phải công cụ quản lý mọi thao tác provisioning; automation tổng quát có thể dùng Azure Automation, ARM hoặc CLI/PowerShell.

**Chọn theo cách thao tác:** Azure Portal phù hợp khi cần giao diện web để tạo VM, cấu hình load balancer và xem hiệu năng qua Azure Monitor hoặc Application Insights. Azure CLI và Azure PowerShell cũng có thể triển khai và truy xuất dữ liệu giám sát khi cần lệnh hoặc script.

<a id="az900-021"></a>

## AZ900-021 | TCO calculator và Pricing calculator

**Dấu hiệu:** First step, cost savings, on-premises versus Azure, conversion and implementation costs.

**Nhóm kiến thức:** Describe Azure management and governance → cost management → cost estimation tools. TCO là kiến thức bổ trợ theo tài liệu luyện thi.

**Liên hệ lý thuyết:** TCO Calculator trong đề cũ so sánh tổng chi phí sở hữu hạ tầng on-premises với triển khai tương đương trên Azure để ước tính tiết kiệm. Pricing Calculator ước tính chi phí theo cấu hình và lượng dùng của từng dịch vụ, rồi cộng nhiều dịch vụ trong cùng một dự toán. Khi lập business case di chuyển hiện nay, Microsoft hướng dẫn dùng Azure Migrate Business Case để phân tích TCO/ROI.

**Cách phân tích đáp án:** Đề xuất dùng TCO làm bước đầu đánh giá lợi ích chi phí chuyển từ on-premises sang Azure là phù hợp. Đầu ra hỗ trợ business case và phụ thuộc dữ liệu, giả định nhập vào.

**Bẫy:** TCO không thay thế dự toán đầy đủ cho refactor, chuyển dữ liệu, đào tạo, nhân công triển khai hay so sánh mọi cloud vendor. Nếu yêu cầu chỉ là báo giá dịch vụ Azure dự kiến thì xét Pricing calculator. Đọc kỹ phạm vi “first step” khi chấm Yes/No. Khi đề đối chiếu hai calculator, tiêu chí phân biệt là dự toán tiêu thụ Azure so với so sánh tổng chi phí sở hữu giữa hai phương án. Mức độ chi tiết hay số lượng dịch vụ không phải tiêu chí phân biệt.

<a id="az900-022"></a>

## AZ900-022 | Container, Docker và Kubernetes

**Dấu hiệu:** Package dependencies, consistent environments, full OS, deployment and scaling.

**Nhóm kiến thức:** Describe Azure architecture and services → compute → containers.

**Liên hệ lý thuyết:** Container image đóng gói mã và dependencies để giữ môi trường chạy nhất quán trên host tương thích. Docker cung cấp công cụ build, phân phối image và chạy/quản lý container. Container dạng process isolation chia sẻ kernel của host, không cần mỗi container có full guest OS như VM. Kubernetes là nền tảng mã nguồn mở điều phối triển khai, mở rộng và quản lý container, dùng được trên Azure và các môi trường khác.

**Cách phân tích đáp án:** Với bốn phát biểu đóng gói dependencies / Docker quản lý containers / containers luôn cần full OS / Kubernetes tự động triển khai và scale trên Azure, kết quả là True, True, False, True.

**Bẫy:** Cụm “in Azure” không đồng nghĩa “chỉ dành cho Azure”. Cần phân biệt Kubernetes và dịch vụ AKS. Nếu bộ lựa chọn thiếu T,T,F,T, đó là lỗi lựa chọn của đề, không đổi kiến thức để khớp đáp án.

**Chọn nền tảng hosting cho microservices:** Mỗi dịch vụ có thể đóng gói bằng một container image và triển khai độc lập. Khi cần một nền tảng Azure để điều phối nhiều workload, AKS cung cấp Kubernetes được quản lý và hỗ trợ cấu hình số replica hoặc autoscaling riêng cho từng dịch vụ. Container là đơn vị đóng gói và chạy. Azure Web Apps phù hợp để host web app hoặc API, còn Azure Virtual Desktop cung cấp desktop và ứng dụng từ xa.

<a id="az900-023"></a>

## AZ900-023 | Latency và triệu chứng phản hồi chậm

**Dấu hiệu:** Slow performance, delayed response, initial concern, common user problem.

**Nhóm kiến thức:** Describe cloud concepts → performance và cloud benefits.

**Liên hệ lý thuyết:** Latency là độ trễ từ khi gửi yêu cầu đến khi có phản hồi hoặc hoàn thành thao tác, tùy phép đo. Fault tolerance là khả năng tiếp tục hoạt động khi thành phần lỗi. Dynamic scalability là khả năng điều chỉnh năng lực theo tải. Agility là khả năng nhanh chóng triển khai và thích ứng.

**Cách phân tích đáp án:** Khi hỏi thuật ngữ mô tả trải nghiệm người dùng phải chờ lâu, latency phù hợp nhất trong các lựa chọn. Thiếu tài nguyên có thể gây chậm nhưng scalability mô tả khả năng đáp ứng tải, không phải tên triệu chứng.

**Bẫy:** Phản hồi chậm chưa chứng minh nguyên nhân là mạng. Cần đo compute, disk I/O, database, network và thời gian xử lý để tìm bottleneck. Định nghĩa latency phụ thuộc phép đo như round-trip time hoặc end-to-end response time.

<a id="az900-024"></a>

## AZ900-024 | Hybrid Cloud cho workload có yêu cầu khác nhau

**Dấu hiệu:** Move to Azure, retain control for some workloads, regulated banking data, reduce operational costs.

**Nhóm kiến thức:** Describe cloud concepts → cloud deployment models → hybrid cloud.

**Liên hệ lý thuyết:** Hybrid Cloud kết hợp public cloud với hạ tầng on-premises/private hoạt động cùng nhau. Tổ chức có thể chọn vị trí workload theo yêu cầu kiểm soát, tích hợp và vận hành.

**Cách phân tích đáp án:** Khi ý định đề là đưa workload phù hợp lên Azure và giữ một phần workload cần kiểm soát riêng trong private/on-premises, chọn Hybrid Cloud. Private-only không tận dụng đầy đủ public cloud; datacenter đơn thuần không thể hiện mô hình kết hợp.

**Bẫy:** Chỉ có dữ liệu nhạy cảm hoặc nhắc GDPR chưa đủ để bắt buộc hybrid/private. Public cloud có thể hỗ trợ yêu cầu tuân thủ khi được thiết kế và vận hành phù hợp. Hybrid không mặc nhiên rẻ hơn; cần tính cả chi phí kết nối và vận hành hai môi trường. Nếu đề không yêu cầu giữ workload riêng, cần nêu giả định khi chọn hybrid.

**Phân biệt:** Nếu hạ tầng giữ lại là một public cloud khác và tổ chức dùng thêm Azure, cách gọi phù hợp là multicloud. Hybrid cloud trong câu hỏi AZ-900 thường ngụ ý có môi trường private hoặc on-premises kết hợp với Azure.

<a id="az900-025"></a>

## AZ900-025 | Spot, Reservations và Hybrid Benefit

**Dấu hiệu:** Non-critical batch, tolerate interruptions, spare capacity, lower price, committing in advance.

**Nhóm kiến thức:** Describe Azure management and governance → cost management → factors affecting costs. Liên quan compute và VM pricing.

**Liên hệ lý thuyết:** Azure Spot VMs dùng công suất Azure chưa sử dụng với giá giảm, nhưng có thể bị thu hồi khi Azure cần capacity hoặc điều kiện giá không còn đáp ứng. VM Reservations cung cấp giảm giá cho usage đủ điều kiện theo cam kết thời hạn 1 hoặc 3 năm. Azure Hybrid Benefit tận dụng bản quyền phần mềm hiện có đủ điều kiện.

**Cách phân tích đáp án:** Spare capacity và chịu gián đoạn hướng tới Spot Instances. Cam kết sử dụng trước hướng tới VM Reservations. Availability Zones phục vụ cô lập lỗi và high availability, không phải cơ chế giảm giá dựa trên capacity dư.

**Bẫy:** Reservation là cam kết giá/usage, không mặc nhiên bảo đảm capacity; capacity reservation là khái niệm khác. Không cần hiểu cam kết trước là luôn thanh toán toàn bộ ngay lập tức. Workload Spot cần có khả năng khởi động lại hoặc checkpoint khi bị thu hồi. Hai đáp án mô tả hai chiến lược riêng, không có nghĩa cùng áp ưu đãi reservation lên một Spot VM.

<a id="az900-026"></a>

## AZ900-026 | Resource locks và phân quyền RBAC

**Dấu hiệu:** Protect critical production VM, accidental deletion or modification, shared resource group.

**Nhóm kiến thức:** Describe Azure management and governance → governance and compliance → resource locks.

**Liên hệ lý thuyết:** CanNotDelete cho phép đọc và sửa nhưng chặn xóa tài nguyên. ReadOnly cho phép đọc nhưng chặn sửa và xóa ở control plane. Locks có thể đặt tại subscription, resource group hoặc resource và kế thừa xuống scope con; áp hạn chế cho mọi user/role khi còn hiệu lực.

**Cách phân tích đáp án:** Bảo vệ VM quan trọng khỏi xóa/sửa và bảo vệ resource group dùng chung là hai tình huống phù hợp nhất trong bộ lựa chọn. Autoscale đáp ứng tải; Advisor/Cost Management hỗ trợ tối ưu chi phí, không phải chức năng resource locks.

**Bẫy:** Từ unauthorized trong lựa chọn resource group chưa chuẩn: RBAC kiểm soát ai có quyền làm gì, locks là lớp bảo vệ bổ sung ngay cả khi người dùng có quyền thay đổi tài nguyên. Người có quyền quản lý lock có thể gỡ lock. Locks chỉ bảo vệ control plane, không chặn mọi thao tác data plane như sửa/xóa dữ liệu bên trong tài nguyên. Chọn đúng loại lock: CanNotDelete không ngăn sửa cấu hình.

<a id="az900-027"></a>

## AZ900-027 | Subscription là điều kiện trước khi triển khai workload

**Dấu hiệu:** First required step, Azure trial account, create database and AI services.

**Nhóm kiến thức:** Describe Azure architecture and services → core architectural components → subscriptions, resource groups và resources.

**Liên hệ lý thuyết:** Subscription là phạm vi quản lý và thanh toán cho tài nguyên Azure. Với các dịch vụ workload thông thường, thứ tự tổ chức là Subscription → Resource Group → Resource.

**Cách phân tích đáp án:** Trong các lựa chọn Availability Zone, Resource Group, ARM template và Subscription, chọn Subscription làm điều kiện đầu tiên. Resource group được tạo trong subscription. ARM template là một cách triển khai tùy chọn; không phải tài nguyên nào cũng cần chọn availability zone.

**Bẫy:** Đăng ký Azure Trial thường đã cấp subscription, nên không cần tạo thêm subscription chỉ để thử dịch vụ. Nếu đề hỏi thao tác tiếp theo sau khi đã có subscription hoạt động thì resource group có thể là bước kế tiếp. Azure account là danh tính/tài khoản truy cập; subscription là phạm vi sử dụng dịch vụ và billing, không phải hai từ đồng nghĩa.

**Region và cấu trúc nhóm:** Resource Group gom tài nguyên liên quan như VM và Web App để quản lý chung. Region chọn khi tạo nhóm là nơi lưu metadata. Các tài nguyên thuộc cùng nhóm có thể triển khai ở nhiều region trong cùng subscription. Resource Groups không lồng nhau. Management Groups có thể lồng nhau ở cấp trên subscription.

<a id="az900-028"></a>

## AZ900-028 | Reliability, predictability và compliance

**Dấu hiệu:** NOT a benefit of reliability/predictability, unpredictable costs, reliable performance, global scale and business continuity.

**Nhóm kiến thức:** Describe cloud concepts → benefits of cloud services → reliability, predictability, security and governance.

**Liên hệ lý thuyết:** Reliability là khả năng phục hồi sau lỗi và tiếp tục hoạt động. Predictability gồm dự báo hiệu năng/tài nguyên cần thiết và chi phí. Compliance thuộc lợi ích security/governance; cloud hỗ trợ tuân thủ nhưng không tự bảo đảm mọi workload tuân thủ.

**Cách phân tích đáp án:** Performance ổn định phù hợp predictability; thiết kế đa region hỗ trợ business continuity và reliability. Chi phí khó dự đoán không phải lợi ích cost predictability. Với lựa chọn A “Ability to Handle Unpredictable Costs”, A có vẻ là đáp án tác giả dự kiến nhưng chưa có key xác nhận.

**Bẫy:** Nếu stem hỏi nghiêm ngặt lựa chọn ngoài nhóm reliability/predictability, D về industry regulations/compliance cũng có cơ sở vì thuộc governance. Câu LinkedIn 23/60 trộn tiêu chí phân nhóm với lợi ích triển khai, nên không dùng để đánh giá readiness khi chưa làm rõ. Nguồn: https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/3-reliability-predictability-cloud và https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/4-security-governance-cloud.

<a id="az900-029"></a>

## AZ900-029 | Blob Storage cho dữ liệu phi cấu trúc

**Dấu hiệu:** Large amounts of unstructured data, documents, images, videos, backups.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure storage services → Blob, Files, Table và Queue.

**Liên hệ lý thuyết:** Azure Blob Storage là object storage tối ưu lưu lượng lớn dữ liệu phi cấu trúc, như văn bản hoặc dữ liệu nhị phân. Các trường hợp phổ biến gồm tài liệu, hình ảnh, audio/video và backup/archive.

**Cách phân tích đáp án:** Chọn Blob khi đề nhấn mạnh unstructured data và object storage. Azure Files cung cấp file shares qua SMB/NFS; Table Storage lưu NoSQL entities theo key/attributes; Queue Storage lưu messages để xử lý bất đồng bộ.

**Bẫy:** Azure Files cũng lưu được ảnh và tài liệu; khác biệt quan trọng là cách truy cập và nhu cầu file share, không chỉ phần mở rộng file. Blob có thể lưu cả file chứa dữ liệu có cấu trúc như CSV/JSON; cụm optimized for unstructured data không phải giới hạn tuyệt đối. Phân biệt chọn dịch vụ Blob với chọn access tier Hot/Cool/Cold/Archive và với storage account chứa dịch vụ. Nguồn: https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction.

<a id="az900-030"></a>

## AZ900-030 | Public Preview và cam kết SLA

**Dấu hiệu** Public Preview, support, service-level agreement, General Availability (GA).

**Nhóm kiến thức** Kiến thức bổ trợ về vòng đời dịch vụ Azure. Đề cương AZ-900 ngày 20/07/2026 không liệt kê điều khoản SLA của Preview thành mục tiêu riêng.

**Liên hệ lý thuyết** Public Preview cho phép khách hàng thử nghiệm tính năng trước GA. Phạm vi hỗ trợ phụ thuộc điều khoản của tính năng, và Public Preview thường không có SLA.

**Cách phân tích đáp án** Chọn No khi đề giả định mặc định nhận được hỗ trợ kèm SLA. Khi so sánh nhà cung cấp, đọc SLA và điều kiện áp dụng của dịch vụ và cấu hình dự kiến. Dự toán chi phí là bước riêng.

**Bẫy** Hỗ trợ kỹ thuật và SLA là hai cam kết riêng. Một tính năng có thể được hỗ trợ ở mức giới hạn trong giai đoạn Preview mà không có SLA. Public Preview có thể miễn phí hoặc tính phí theo điều khoản sản phẩm. Việc trả phí không tự tạo cam kết SLA. Kiểm tra điều khoản cụ thể nếu đề nêu ngoại lệ.

<a id="az900-031"></a>

## AZ900-031 | Microsoft Defender for Cloud và tên cũ Azure Security Center

**Dấu hiệu** Security posture, industry regulations, regulatory compliance, potential threats, migration to Azure.

**Nhóm kiến thức** Describe Azure architecture and services → Azure identity, access, and security → Microsoft Defender for Cloud.

**Liên hệ lý thuyết** Microsoft Defender for Cloud, tên hiện hành của Azure Security Center, đánh giá cấu hình bảo mật và đưa ra khuyến nghị khắc phục. Regulatory compliance dashboard theo dõi tài nguyên theo các kiểm soát của tiêu chuẩn được gán. Các gói bảo vệ workload cung cấp khả năng phát hiện mối đe dọa theo phạm vi từng gói.

**Cách phân tích đáp án** Chọn Defender for Cloud khi cần kết hợp đánh giá bảo mật, theo dõi khoảng trống tuân thủ và bảo vệ workload. Availability Zones hỗ trợ chịu lỗi hạ tầng. Azure Virtual Network cung cấp kết nối và phân đoạn mạng. Cognitive Services cung cấp tính năng AI cho ứng dụng.

**Bẫy** Phân biệt chịu lỗi hạ tầng với chống mối đe dọa bảo mật. Dashboard giúp tìm khoảng trống tuân thủ, còn một số kiểm soát cần doanh nghiệp tự đánh giá và cung cấp bằng chứng.

<a id="az900-032"></a>

## AZ900-032 | Khôi phục khi mất cả Azure region

**Dấu hiệu** Region-wide failure, unplanned outage, recover, VMs in one region.

**Nhóm kiến thức** Describe cloud concepts → lợi ích của cloud → reliability và disaster recovery.

**Liên hệ lý thuyết** Disaster Recovery lập phương án khôi phục ứng dụng và dữ liệu sau sự cố lớn. Khi mất cả region, cần nơi phục hồi và dữ liệu sẵn có ở region khác, cùng quy trình failover hoặc restore. Azure Site Recovery có thể sao chép VM sang region đích để failover. Kiểm tra quota, khả năng tạo VM phù hợp và năng lực xử lý tải sau khi chuyển vùng.

**Cách phân tích đáp án** Disaster Recovery đáp ứng trực tiếp yêu cầu khôi phục. Nếu đề yêu cầu hai lựa chọn như tình huống này, Elasticity and Scalability là lựa chọn bổ trợ để lập kế hoạch công suất tại nơi phục hồi. Agility nói về tốc độ triển khai. VM Scale Sets hỗ trợ quản lý và mở rộng nhóm VM.

**Bẫy** Scale Sets hoặc Availability Zones triển khai trong cùng region chỉ có phạm vi bảo vệ bên trong region đó. Tăng số VM ở nơi đã mất dịch vụ không thay thế được phương án khôi phục tại một region khác.

<a id="az900-033"></a>

## AZ900-033 | Azure Virtual Desktop cho nhân viên làm việc từ xa

**Dấu hiệu** Windows remote desktop, virtualized desktop, personalized access to apps and data.

**Nhóm kiến thức** Describe Azure architecture and services → Azure compute and networking services → Azure Virtual Desktop.

**Liên hệ lý thuyết** Azure Virtual Desktop cung cấp desktop Windows đầy đủ hoặc từng ứng dụng qua RemoteApp. Personal host pool cho phép gán máy riêng, còn pooled host pool cho phép nhiều người dùng chia sẻ các session host theo cấu hình.

**Cách phân tích đáp án** Chọn AVD khi trọng tâm là cung cấp desktop hoặc ứng dụng từ xa cho nhân viên. Azure VM cung cấp máy ảo để chạy workload. VM Scale Sets giúp quản lý và mở rộng nhóm VM. Availability Sets phân tán VM qua fault domain và update domain để giảm tác động của lỗi phần cứng và bảo trì.

**Bẫy** AVD có thể dùng Azure VM làm session host. Người dùng vẫn truy cập từ thiết bị đầu cuối tương thích. Nhu cầu cấp quyền theo từng người không tự động đồng nghĩa mỗi người cần một VM riêng.

<a id="az900-034"></a>

## AZ900-034 | Cô lập mạng bằng VNet và phân đoạn bằng subnet

**Dấu hiệu** Isolated network environments, different departments, segmentation and isolation.

**Nhóm kiến thức** Describe Azure architecture and services → Azure compute and networking services → virtual networks và subnets.

**Liên hệ lý thuyết** Một VNet tạo môi trường mạng riêng trong Azure. Có thể dùng VNet riêng cho từng phòng ban và kết nối có chủ đích khi cần. Subnet chia không gian địa chỉ bên trong VNet. Azure định tuyến giữa các subnet trong cùng VNet theo mặc định. Có thể dùng NSG hoặc firewall phù hợp để giới hạn luồng được phép.

**Cách phân tích đáp án** Khi đề yêu cầu các môi trường mạng độc lập, chọn Azure Virtual Network. Nếu đề yêu cầu chia một VNet hiện có thành nhiều dải mạng, chọn subnet và bổ sung quy tắc nếu cần cô lập lưu lượng. ExpressRoute cung cấp kết nối riêng từ mạng doanh nghiệp tới Azure. Azure DNS phục vụ phân giải tên.

<a id="az900-035"></a>

## AZ900-035 | Microsoft Purview cho khám phá và quản trị dữ liệu

**Dấu hiệu** Data discovery, cataloging, data governance, lineage, metadata.

**Nhóm kiến thức** Describe Azure management and governance → governance and compliance → Microsoft Purview.

**Liên hệ lý thuyết** Azure Purview là tên cũ của dịch vụ quản trị dữ liệu nay thuộc Microsoft Purview. Data Map quét nguồn dữ liệu được hỗ trợ để thu thập metadata. Unified Catalog giúp người dùng tìm và quản lý tài sản dữ liệu đã đăng ký.

**Cách phân tích đáp án** Khi đề hỏi về khám phá, lập danh mục và quản trị dữ liệu, chọn Purview. Azure Machine Learning phục vụ vòng đời mô hình, Azure DevOps hỗ trợ quản lý mã nguồn và CI/CD, còn Cost Management & Billing phục vụ theo dõi chi phí và hóa đơn.

**Bẫy** Cụm “integrating seamlessly” không quyết định đáp án và không bảo đảm mọi kết nối. Phạm vi tích hợp phụ thuộc nguồn và cấu hình. Tìm thấy metadata trong catalog không tự cấp quyền đọc dữ liệu gốc.

<a id="az900-036"></a>

## AZ900-036 | Elasticity cho tải tăng theo đợt

**Dấu hiệu** Traffic spike, variable usage, end-of-quarter reporting, manage cost.

**Nhóm kiến thức** Describe cloud concepts → benefits of using cloud services → scalability và elasticity.

**Liên hệ lý thuyết** Scalability mô tả khả năng điều chỉnh công suất bằng cách thay đổi kích thước hoặc số lượng tài nguyên. Elasticity nhấn mạnh việc tự động điều chỉnh công suất theo biến động của tải. Autoscaling là một cách triển khai khi dịch vụ hỗ trợ.

**Cách phân tích đáp án** Nếu nhu cầu tăng mạnh cuối quý rồi trở về mức bình thường, chọn Elasticity. Tăng công suất lúc cao điểm để đáp ứng tải, rồi thu hồi phần công suất dư để kiểm soát chi phí. High Availability tập trung vào duy trì dịch vụ khi có sự cố. Agility tập trung vào tốc độ cấp phát và triển khai.

**Bẫy** Câu hỏi dùng Power BI Embedded làm bối cảnh. Đáp án gọi tên đặc tính cloud, còn cách cấu hình tăng giảm công suất phụ thuộc dịch vụ và gói đang dùng.

<a id="az900-037"></a>

## AZ900-037 | Region, VM size và phí truyền dữ liệu liên vùng

**Dấu hiệu** Pricing factors, datacenter location, virtual machine size, inter-region data transfer.

**Nhóm kiến thức** Describe Azure management and governance → cost management → factors that affect costs.

**Liên hệ lý thuyết** Giá tài nguyên có thể thay đổi theo Azure region và SKU. Với VM, kích cỡ hoặc dòng máy ảnh hưởng đơn giá compute. Theo biểu giá bandwidth chuẩn, dữ liệu liên vùng được tính phí egress ở phía gửi, còn ingress ở phía nhận miễn phí.

**Cách phân tích đáp án** Chọn vị trí triển khai, VM size và dung lượng truyền dữ liệu giữa các region. Azure Portal là giao diện quản lý. Khi tính chi phí cho luồng hai chiều, mỗi chiều có một phía gửi riêng.

<a id="az900-038"></a>

## AZ900-038 | Chọn công cụ chuyển tệp lên Azure Storage

**Dấu hiệu** Large file set, on-premises server, Azure Storage account, efficiency.

**Nhóm kiến thức** Describe Azure architecture and services → Azure storage services → file movement options.

**Liên hệ lý thuyết** AzCopy là công cụ dòng lệnh để sao chép dữ liệu tới, từ hoặc giữa các Storage account. Azure Storage Explorer cung cấp giao diện đồ họa quản lý và truyền dữ liệu. Azure Data Factory dùng Copy activity trong pipeline để chuyển dữ liệu giữa các nguồn và có thể kết hợp xử lý, lịch chạy, điều phối. Azure File Sync đồng bộ Azure Files với các máy chủ Windows và hỗ trợ cloud tiering.

**Cách phân tích đáp án** Với yêu cầu sao chép trực tiếp bộ tệp từ máy chủ lên Storage, AzCopy phù hợp nhất trong bộ lựa chọn. Data Factory cũng thực hiện được nhưng câu chưa yêu cầu pipeline. Khi cần duy trì đồng bộ file share hoặc cache cục bộ, xem xét File Sync.

<a id="az900-039"></a>

## AZ900-039 | Azure Arc cho quản trị hybrid và multicloud

**Dấu hiệu** Centralized management, on-premises servers, Kubernetes in multiple clouds, governance.

**Nhóm kiến thức** Describe Azure management and governance → managing and deploying Azure resources → Azure Arc.

**Liên hệ lý thuyết** Azure Arc đưa máy chủ và cụm Kubernetes được hỗ trợ bên ngoài Azure vào lớp quản lý Azure Resource Manager. Tài nguyên được kết nối có danh tính tài nguyên Azure và có thể dùng các cơ chế quản trị như Policy, RBAC và tags tùy loại tài nguyên và cấu hình.

**Cách phân tích đáp án** Chọn Yes khi tổ chức cần quản trị thống nhất tài nguyên on-premises, nhiều cloud và tài nguyên Azure gốc. Azure VM được quản lý trực tiếp trong Azure, còn Arc mở rộng phạm vi tới tài nguyên bên ngoài. Arc-enabled servers dùng Connected Machine agent cho máy ngoài Azure.

**Bẫy** Kết nối Arc tạo khả năng quản lý tập trung. Mức tuân thủ thực tế phụ thuộc policy được gán, cấu hình và xử lý các sai lệch.

<a id="az900-040"></a>

## AZ900-040 | Cấu hình CPU và RAM cho workload VM

**Dấu hiệu** Complex calculations, significant computational power, ample memory, large datasets.

**Nhóm kiến thức** Describe Azure architecture and services → Azure compute → virtual machines.

**Liên hệ lý thuyết** Chọn VM size theo nhu cầu vCPU, RAM, đĩa và mạng. CPU phục vụ tính toán, RAM giữ dữ liệu đang xử lý. Compute optimized và memory optimized đáp ứng các tỷ lệ CPU/RAM khác nhau, còn lựa chọn cụ thể cần số đo tải.

**Cách phân tích đáp án** Khi đề nhấn mạnh tính toán phức tạp và bộ nhớ lớn, ưu tiên CPU cores and memory. Network bandwidth ảnh hưởng truyền dữ liệu. Storage capacity là dung lượng lưu. VM Scale Sets quản lý nhóm VM và điều chỉnh số instance theo tải hoặc lịch.

**Bẫy** Tải mạng cao trong giờ làm việc là yêu cầu bổ sung. Xác định yêu cầu chính của câu hỏi, rồi kiểm tra các giới hạn mạng và đĩa của VM size đã chọn.

<a id="az900-041"></a>

## AZ900-041 | Microsoft 365, Blob Storage và mô hình dịch vụ

**Dấu hiệu** Microsoft 365, Azure Blob Storage, SaaS, PaaS, IaaS.

**Nhóm kiến thức** Describe cloud concepts → cloud service types.

**Liên hệ lý thuyết** Microsoft 365 cung cấp ứng dụng hoàn chỉnh theo mô hình SaaS. Azure Blob Storage là dịch vụ object storage được quản lý, được tài liệu Microsoft phân loại là PaaS. Azure Virtual Machines là ví dụ IaaS, nơi khách hàng quản lý guest OS và ứng dụng.

**Cách phân tích đáp án** Phân loại từng dịch vụ khi đề ghép nhiều dịch vụ trong một lựa chọn. Với Microsoft 365 và Blob Storage, tổ hợp là SaaS và PaaS. Nếu bộ lựa chọn chỉ có SaaS và IaaS thì ghi nhận thiếu đáp án phù hợp và loại câu khỏi đánh giá mức sẵn sàng.

**Bẫy** Storage có thể là một thành phần của hạ tầng IaaS, chẳng hạn đĩa của VM. Cần phân biệt vai trò đó với dịch vụ Blob Storage được quản lý.

**Tình huống tùy chỉnh Linux và directory:** Chọn IaaS khi ứng dụng yêu cầu kiểm soát hệ điều hành khách và tự vận hành phần mềm directory trên VM. Khách hàng cấu hình, cập nhật và bảo vệ guest OS cùng ứng dụng, còn Microsoft quản lý hạ tầng vật lý và lớp ảo hóa. Trong PaaS và SaaS, nền tảng quản lý hệ điều hành nền. Trách nhiệm quản lý tài khoản và quyền truy cập của khách hàng vẫn tồn tại trong mọi mô hình.

**Web Apps và Azure SQL:** Azure Web Apps (App Service), Azure SQL Database và Azure SQL Managed Instance thuộc PaaS: Microsoft quản lý nền tảng và hệ điều hành nền, khách hàng quản lý ứng dụng, dữ liệu và cấu hình truy cập. Khi đề viết Azure SQL Server cùng Web Apps, thường hiểu là Azure SQL được quản lý. SQL Server cài trên Azure Virtual Machines thuộc IaaS; cần đọc rõ cách triển khai.

<a id="az900-042"></a>

## AZ900-042 | Region Pairs, khôi phục và data residency

**Dấu hiệu** Regional outage, paired regions, data residency, backup and recovery.

**Nhóm kiến thức** Describe Azure architecture and services → core architectural components → regions và region pairs.

**Liên hệ lý thuyết** Phần lớn region pairs thuộc cùng geography, nhưng có ngoại lệ. Một số dịch vụ dùng cặp region cho geo-replication, chẳng hạn Storage GRS khi được cấu hình. Pairing hỗ trợ chiến lược khôi phục và Azure cố gắng triển khai cập nhật lệch thời điểm giữa hai region.

**Cách phân tích đáp án** Khi có cả yêu cầu residency và phục hồi ngoài region, kiểm tra nơi chứa dữ liệu chính cùng bản sao, rồi cấu hình backup, replication và khôi phục phù hợp với dịch vụ. Region Pairs tự nó không cung cấp cơ chế đồng bộ dữ liệu hoặc failover cho mọi ứng dụng.

**Bẫy** Các phát biểu “Regions ensure compliance” và “Region Pairs provide high availability through synchronization” cần điều kiện triển khai cụ thể. Nhiều region không có pair và nhiều dịch vụ cho phép geo-redundancy ngoài pair.

<a id="az900-043"></a>

## AZ900-043 | Public endpoints và Private endpoints

**Dấu hiệu:** Public internet, private IP, Virtual Network, default endpoints, reduced exposure.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure networking → public và private endpoints.

**Liên hệ lý thuyết:** Public endpoint cung cấp đường truy cập qua địa chỉ công khai, có thể được giới hạn bằng firewall và xác thực. Private endpoint dùng IP riêng trong subnet của VNet để kết nối riêng tới dịch vụ hỗ trợ Private Link. Có thể truy cập từ VNet, VNet peering hoặc mạng on-premises kết nối riêng nếu routing và DNS phù hợp.

**Cách phân tích đáp án:** Với bốn mệnh đề nhận diện public/private, truy cập riêng, mặc định bật cả hai và giảm phơi bày Internet, tổ hợp phù hợp là True, True, False, True. Private endpoint cần được tạo và cấu hình; không phải mọi dịch vụ đều mặc định bật cả public và private endpoints.

**Bẫy:** Tạo private endpoint không tự tắt public network access của dịch vụ. Muốn chỉ cho truy cập riêng, cấu hình chặn public access theo dịch vụ và kiểm tra DNS/routing. Private connectivity giảm bề mặt phơi bày nhưng vẫn cần xác thực và phân quyền.

<a id="az900-044"></a>

## AZ900-044 | ExpressRoute và kết nối riêng tới Azure

**Dấu hiệu:** On-premises datacenter, private connection, dedicated connectivity, bypass public internet, consistent latency.

**Nhóm kiến thức:** Describe Azure architecture and services → Azure networking → ExpressRoute.

**Liên hệ lý thuyết:** ExpressRoute mở rộng mạng on-premises tới Microsoft cloud qua kết nối riêng với nhà cung cấp kết nối hoặc ExpressRoute Direct. Lưu lượng trên kết nối ExpressRoute không đi qua Internet công cộng, hỗ trợ độ trễ ổn định và độ tin cậy cao hơn kết nối Internet thông thường. Hiệu năng thực tế phụ thuộc thiết kế, băng thông và các thành phần đường truyền.

**Cách phân tích đáp án:** Khi cần liên kết riêng từ datacenter tới Azure, chọn mô tả private, dedicated connection bypassing the public internet. Phương án nói ExpressRoute chạy qua public internet là sai. ExpressRoute không chỉ phục vụ doanh nghiệp nhỏ có nhu cầu mạng tối thiểu và không phải dịch vụ miễn phí mặc định theo subscription. VPN Site-to-Site thông thường tạo đường hầm IPsec qua Internet; cũng có thể cấu hình VPN qua ExpressRoute.

**Bẫy:** Kết nối riêng không đồng nghĩa tự động mã hóa. ExpressRoute không mã hóa lưu lượng mặc định; bổ sung TLS, IPsec hoặc MACsec phù hợp khi cần. Độ sẵn sàng còn phụ thuộc thiết kế dự phòng từ đầu tới cuối.
