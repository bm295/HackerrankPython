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
| sovereign region, national cloud, China, East US, Germany | [AZ900-010](#az900-010) | Phân biệt loại cloud với đơn vị vận hành; kiểm tra thông tin Azure Germany cũ. |
| varying traffic, lunchtime peaks, schedule, VM Scale Sets, Availability Sets | [AZ900-011](#az900-011) | Tải biến động cần autoscale bằng VMSS; Availability Sets xử lý phân tán lỗi và bảo trì. |
| numerous subscriptions, business units, governance, delegate management | [AZ900-012](#az900-012) | Management Groups tạo scope trên subscription để tổ chức và kế thừa Policy/RBAC. |
| Azure Policy, organizational standards, compliance, audit, deny | [AZ900-013](#az900-013) | Kiểm tra cấu hình theo quy tắc và effect; phân biệt Policy với RBAC, chi phí và monitoring. |
| Azure CLI, list all VMs, az vm list | [AZ900-014](#az900-014) | az + nhóm vm + thao tác list; kiểm tra subscription và resource-group scope. |
| telemetry, performance and health, alerts, user experiences, NOT use | [AZ900-015](#az900-015) | Monitor là nền tảng, Log Analytics truy vấn logs, Application Insights là APM; DevOps phục vụ phát triển. |
| Advisor, recommendations, cost saving, reliability, real-time monitoring | [AZ900-016](#az900-016) | Advisor đề xuất tối ưu; Monitor theo dõi telemetry và cảnh báo. |
| match Region, Availability Zone, Fault Domain, Georedundancy | [AZ900-017](#az900-017) | Phân biệt phạm vi địa lý, zone độc lập, phần cứng chung và sao chép liên region. |
| direct OS control, specialized software, isolated environment | [AZ900-018](#az900-018) | Chọn VM theo nhu cầu kiểm soát guest OS; phân biệt với môi trường container được quản lý. |
| service incidents, outages, status updates, incident details, maintenance | [AZ900-019](#az900-019) | Service Health thông báo sự cố nền tảng; Monitor phân tích telemetry workload. |
| centralized management, monitoring, unified console, Azure Portal | [AZ900-020](#az900-020) | Portal là giao diện tập trung để truy cập và quản lý dịch vụ; phân biệt với engine tự động hóa. |
| TCO calculator, cost savings, on-premises versus Azure, first step | [AZ900-021](#az900-021) | TCO so sánh tổng chi phí; Pricing calculator ước tính chi phí dịch vụ Azure. |
| containers dependencies, Docker, full OS, Kubernetes | [AZ900-022](#az900-022) | Image đóng gói dependencies; container chia sẻ kernel; Kubernetes điều phối đa môi trường. |
| slow performance, delayed response, latency, initial concern | [AZ900-023](#az900-023) | Latency mô tả độ trễ; cần đo để tìm nguyên nhân chậm. |
| regulated workloads, move to Azure, retain private infrastructure, hybrid | [AZ900-024](#az900-024) | Hybrid phù hợp khi kết hợp public với private/on-premises theo yêu cầu workload. |
| spare capacity, tolerate interruptions, batch, commit in advance, Spot, Reservations | [AZ900-025](#az900-025) | Spot dùng công suất dư có thể bị thu hồi; Reservations giảm giá theo cam kết thời hạn. |
| resource locks, accidental deletion, modification, shared resource group, ReadOnly, CanNotDelete | [AZ900-026](#az900-026) | Locks bảo vệ thao tác quản lý; RBAC xác định quyền theo danh tính. |

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

**Bẫy:** Khi đáp án gọi ARM templates là “scripts”, hiểu chính xác là tệp JSON dùng cú pháp khai báo trạng thái mong muốn; ARM xử lý triển khai và dependency. Templates hỗ trợ nhiều loại tài nguyên, không chỉ VM. Cụm “ARM is a scripting language” nhầm dịch vụ ARM với cách viết cấu hình hạ tầng. Thay đổi tài nguyên trực tiếp qua Portal có thể khiến cấu hình thực tế lệch khỏi mã.

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

**Nhóm kiến thức:** Describe Azure architecture and services → compute → Virtual Machines và containers.

**Liên hệ lý thuyết:** Azure VM cung cấp guest OS có thể cấu hình, cài phần mềm và vá lỗi theo nhu cầu. Microsoft quản lý phần cứng vật lý; khách hàng quản lý guest OS và ứng dụng.

**Cách phân tích đáp án:** Yêu cầu kiểm soát trực tiếp OS và cài phần mềm chuyên dụng hướng tới VM. Functions chạy mã theo trigger. ACI chạy container trên hạ tầng được quản lý. AKS điều phối container, có khả năng cấu hình node nhưng không phải lựa chọn đơn giản nhất khi đề chỉ yêu cầu môi trường OS riêng.

**Bẫy:** Từ isolated hoặc sensitive data không đủ để chọn VM. Container cũng có khả năng cô lập; dữ kiện phân biệt là mức kiểm soát OS cần thiết. VM không mặc nhiên cấp host vật lý độc quyền hay bảo đảm tuân thủ tài chính; cần cấu hình bảo mật và vận hành phù hợp.

<a id="az900-019"></a>

## AZ900-019 | Service Health và Monitor

**Dấu hiệu:** Azure service incidents, outages, service status updates, incident details, planned maintenance.

**Nhóm kiến thức:** Describe Azure management and governance → monitoring tools → Azure Service Health.

**Liên hệ lý thuyết:** Service Health cung cấp thông tin sự cố dịch vụ Azure, bảo trì và advisories liên quan đến subscription, region và dịch vụ đang dùng. Có thể cấu hình alert để nhận thông báo. Monitor thu thập metrics, logs và telemetry của workload để phân tích và cảnh báo.

**Cách phân tích đáp án:** Sự cố nền tảng được Azure công bố hướng tới Service Health. CPU cao, lỗi request hay độ trễ ứng dụng hướng tới Monitor/Application Insights. ARM triển khai và quản lý tài nguyên; Traffic Manager định tuyến DNS giữa các endpoint.

**Bẫy:** Service Health alerts dùng cơ chế Azure Monitor alerts, nhưng nguồn thông tin sự cố nền tảng trong câu hỏi là Service Health. Resource Health theo dõi tài nguyên cụ thể; Azure Status cung cấp thông tin công khai về sự cố diện rộng. Cập nhật Service Health gần thời gian thực khi Microsoft phát hiện và xác nhận vấn đề.

<a id="az900-020"></a>

## AZ900-020 | Azure Portal là giao diện quản lý tập trung

**Dấu hiệu:** Centralized management, monitoring, unified console, graphical interface.

**Nhóm kiến thức:** Describe Azure management and governance → tools for managing and deploying resources → Azure Portal.

**Liên hệ lý thuyết:** Azure Portal là giao diện web hợp nhất để tạo, quản lý và giám sát tài nguyên Azure. Portal tích hợp các màn hình quản lý của từng dịch vụ, dashboards và truy cập công cụ liên quan.

**Cách phân tích đáp án:** Khi hỏi điểm truy cập tập trung để quản lý nhiều loại tài nguyên, chọn Portal trong các lựa chọn VM/Entra ID/Portal/Monitor. VM cung cấp compute; Entra ID quản lý danh tính; Monitor thu thập và phân tích telemetry.

**Bẫy:** Automation trong câu mô tả giao diện truy cập và cấu hình công cụ tự động hóa. Portal không phải engine thực thi mọi automation; chức năng được cung cấp bởi dịch vụ nền và công cụ như Azure Automation, ARM, CLI/PowerShell. Đừng chỉ thấy monitoring mà bỏ qua phạm vi quản lý tổng thể.

<a id="az900-021"></a>

## AZ900-021 | TCO calculator và Pricing calculator

**Dấu hiệu:** First step, cost savings, on-premises versus Azure, conversion and implementation costs.

**Nhóm kiến thức:** Describe Azure management and governance → cost management → cost estimation tools. TCO là kiến thức bổ trợ theo tài liệu luyện thi.

**Liên hệ lý thuyết:** TCO calculator so sánh tổng chi phí sở hữu hạ tầng on-premises với triển khai tương đương trên Azure để ước tính tiết kiệm. Pricing calculator ước tính chi phí sử dụng dịch vụ Azure theo cấu hình và lượng dùng dự kiến.

**Cách phân tích đáp án:** Đề xuất dùng TCO làm bước đầu đánh giá lợi ích chi phí chuyển từ on-premises sang Azure là phù hợp. Đầu ra hỗ trợ business case và phụ thuộc dữ liệu, giả định nhập vào.

**Bẫy:** TCO không thay thế dự toán đầy đủ cho refactor, chuyển dữ liệu, đào tạo, nhân công triển khai hay so sánh mọi cloud vendor. Nếu yêu cầu chỉ là báo giá dịch vụ Azure dự kiến thì xét Pricing calculator. Đọc kỹ phạm vi “first step” khi chấm Yes/No.

<a id="az900-022"></a>

## AZ900-022 | Container, Docker và Kubernetes

**Dấu hiệu:** Package dependencies, consistent environments, full OS, deployment and scaling.

**Nhóm kiến thức:** Describe Azure architecture and services → compute → containers.

**Liên hệ lý thuyết:** Container image đóng gói mã và dependencies để giữ môi trường chạy nhất quán trên host tương thích. Docker cung cấp công cụ build, phân phối image và chạy/quản lý container. Container dạng process isolation chia sẻ kernel của host, không cần mỗi container có full guest OS như VM. Kubernetes là nền tảng mã nguồn mở điều phối triển khai, mở rộng và quản lý container, dùng được trên Azure và các môi trường khác.

**Cách phân tích đáp án:** Với bốn phát biểu đóng gói dependencies / Docker quản lý containers / containers luôn cần full OS / Kubernetes tự động triển khai và scale trên Azure, kết quả là True, True, False, True.

**Bẫy:** Cụm “in Azure” không đồng nghĩa “chỉ dành cho Azure”. Cần phân biệt Kubernetes và dịch vụ AKS. Nếu bộ lựa chọn thiếu T,T,F,T, đó là lỗi lựa chọn của đề, không đổi kiến thức để khớp đáp án.

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
