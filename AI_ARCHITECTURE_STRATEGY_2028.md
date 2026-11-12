# Chiến lược kiến trúc AI 2028

**Bản đề xuất 0.5 · Cập nhật 12/11/2026 · Nguồn kiểm tra đến 12/11/2026**

## Phạm vi và quyết định cần chốt

Xây dựng năng lực AI cho một đội phát triển phần mềm, bắt đầu bằng trợ lý tra cứu tài liệu nội bộ có trích dẫn. Ưu tiên đo hiệu quả trên một quy trình cụ thể trước khi đầu tư nền tảng dùng chung. Repo này lưu chiến lược và phương pháp. Phạm vi sản phẩm triển khai, chủ sở hữu nghiệp vụ, ngân sách, dữ liệu, lưu lượng và năng lực đội ngũ cần được xác nhận trong R27-01. Các vai trò, ngưỡng và lịch dưới đây là đề xuất.

| Mục tiêu đến cuối 2028 | Kết quả cần chứng minh |
| --- | --- |
| O28-01 · Trợ lý tra cứu hữu ích | Người dùng tìm được câu trả lời đúng và kiểm được nguồn. Thử nghiệm cho thấy thời gian hoàn thành tác vụ giảm so với tìm kiếm hiện tại. |
| O28-02 · Vận hành có kiểm soát | Hệ thống đo được chất lượng, p95 và chi phí trên mỗi tác vụ thành công. Đội vận hành diễn tập ngắt AI, hoàn nguyên và xử lý sự cố phân quyền. |
| O28-03 · Mở rộng theo bằng chứng | Có quyết định mở rộng, thu hẹp hoặc dừng dựa trên kết quả pilot. Workflow gọi công cụ chỉ được đầu tư khi có lợi ích tăng thêm và kiểm soát quyền ở tầng ứng dụng. |

## Danh mục use case

| Ưu tiên | Use case | Baseline và chỉ số | Điều kiện đầu tư |
| --- | --- | --- | --- |
| 1 | Hỏi đáp tài liệu nội bộ chỉ đọc | Tìm kiếm từ khóa hoặc tra cứu thủ công. So sánh tỷ lệ hoàn thành, thời gian, độ đúng của trích dẫn và chi phí mỗi tác vụ thành công. | Chủ sở hữu dữ liệu phê duyệt tập tài liệu và quyền truy cập. Cho phép từ chối trả lời và chuyển về tìm kiếm thủ công. |
| 2 | Đề xuất bước xử lý hoặc soạn nháp | Mẫu và checklist hiện hành. Đo thời gian hoàn thành, tỷ lệ phải sửa và lỗi nghiêm trọng. | Chỉ thử sau khi pilot chỉ đọc đạt gate. Người dùng duyệt trước khi tác động tới nghiệp vụ. |
| 3 | Workflow AI gọi công cụ | Workflow cố định hoặc quy tắc nghiệp vụ. Đo thành công đầu cuối, chi phí và thao tác ngoài quyền. | Thử trong sandbox với công cụ chỉ đọc. Hành động ghi cần một quyết định riêng về quyền, phê duyệt, idempotency và phục hồi. |

## Kịch bản 2028

| Kịch bản | Giả định và tín hiệu theo dõi | Quyết định nếu xảy ra |
| --- | --- | --- |
| Cơ sở | Chất lượng model tiến bộ dần. Bộ đánh giá nội bộ cho thấy tra cứu có trích dẫn tạo giá trị ổn định. | Chuẩn hóa ingestion, đánh giá và đường lui. Mở rộng từng nhóm người dùng khi qua gate. |
| Tăng tốc | Chi phí trên mỗi tác vụ thành công giảm hoặc model xử lý tác vụ nhiều bước tốt hơn trên cùng bộ đánh giá, qua hai vòng đo. | Thử workflow giới hạn theo ADR-03. Giữ xác thực, phân quyền và phê duyệt ở backend. |
| Hạn chế | Chi phí vượt trần, dữ liệu không được phép gửi tới môi trường inference, hoặc pilot chưa đạt chất lượng. | Thu hẹp tập dữ liệu, giữ phương án tìm kiếm và thử hosted khác hoặc self-hosted khi phù hợp với quyền và TCO. |

Theo dõi các kịch bản bằng kết quả đo trên dữ liệu của đội. Việc quản lý vòng đời context có thể trở nên quan trọng hơn khi workflow nhiều bước được dùng rộng rãi. Đây là giả thuyết cần kiểm tra bằng R27-09, dựa trên góc nhìn thiết kế của S01.

## Kiến trúc đích và ADR đề xuất

Luồng đọc đi từ ứng dụng qua xác thực và phân quyền, rồi truy xuất tài liệu trong phạm vi người dùng. Ứng dụng ghép context có giới hạn từ tài liệu được cấp quyền, gọi model qua adapter, kiểm tra trích dẫn và trả câu trả lời hoặc phương án tra cứu thủ công. Pipeline ingest ghi lại chủ sở hữu, phiên bản và quyền tài liệu. Tài liệu gốc giữ vai trò nguồn có thẩm quyền. Cache, index và log tuân theo chính sách quyền, lưu giữ và xóa tương ứng. Chỉ bổ sung memory dài hạn khi một use case đã chứng minh cần lưu trạng thái qua phiên. [S01, S02, S03]

| ADR | Lựa chọn và đánh đổi | Điều kiện xem lại |
| --- | --- | --- |
| ADR-01 · Tìm kiếm hay RAG | Dùng tìm kiếm làm baseline, thử RAG có trích dẫn cho bộ câu hỏi cần tổng hợp. RAG tăng chi phí và có thể dẫn sai nguồn hoặc dùng dữ liệu cũ. | Giữ tìm kiếm cho các tác vụ mà RAG không cải thiện đủ thời gian hoặc chất lượng. Kiểm chứng ở R27-04. |
| ADR-02 · Model API hay tự vận hành | Thử model API qua adapter nếu chính sách dữ liệu cho phép. Đánh giá self-hosted nếu yêu cầu kiểm soát dữ liệu hoặc TCO khiến model API không khả thi. Quản lý model/prompt/config theo phiên bản qua contract ổn định. Chỉ thử routing nhiều model khi phân nhóm tác vụ cho thấy tiềm năng cải thiện chất lượng hoặc chi phí. [S06] | So sánh trên cùng tải, bộ dữ liệu và ngưỡng chất lượng. Điều kiện dữ liệu là gate bắt buộc. Thay model hoặc routing phải qua gate hồi quy và diễn tập rollback cấu hình. Kiểm chứng ở R27-05 và R27-11. |
| ADR-03 · Workflow cố định hay agent | Dùng workflow cố định làm baseline. Chỉ chạy đồng thời các bước độc lập. Thử agent chọn công cụ chỉ đọc khi tác vụ cần chọn bước động. Backend kiểm quyền theo người dùng, tác vụ và ranh giới nghiệp vụ cho từng lần gọi. Áp dụng allowlist, schema và giới hạn thời gian. [S02, S05] | Giữ baseline nếu phương án thử chưa chứng minh lợi ích hoặc trượt gate chất lượng, phân quyền hay truy vết. Chỉ xét nhiều agent nếu workflow đơn giản còn khoảng cách đã đo. Kiểm chứng ở R27-10. |
| ADR-04 · Mức độ phức tạp của context | Dùng retrieval có giới hạn và trích dẫn làm baseline. Thử xếp hạng theo độ mới hoặc nén context khi có bằng chứng về lỗi dữ liệu cũ, nhiễu hoặc vượt ngân sách token. Khi cần tái sử dụng kinh nghiệm qua phiên, so sánh không memory, ghi chú trong phiên và hợp nhất/kiểm chứng ngoài phiên có giới hạn. Memory là dữ liệu suy diễn có thể sai; không thay nguồn nghiệp vụ có thẩm quyền. [S01, S07] | Chỉ giữ phần cải thiện được chất lượng hoặc chi phí trên cùng workload mà vẫn qua gate về quyền và độ đúng. Kiểm chứng ở R27-09. |
| ADR-05 · Điều phối coding agent trong quy trình phát triển | Dùng một coding agent với kiểm chứng độc lập làm baseline. Thử nhiều agent khi tác vụ có thể chia theo phạm vi chỉnh sửa rõ ràng. Cách này có thể giảm xung đột nhưng tăng công điều phối và bàn giao. [S04] | Xét áp dụng năm 2028 nếu R27-13 đạt gate trên tác vụ đại diện và đội có năng lực vận hành. |

### Rà soát năng lực theo 7 lớp

Đây là các ranh giới trách nhiệm đề xuất, có thể cùng nằm trong một ứng dụng. Chưa có bằng chứng triển khai trong repo chiến lược. Không yêu cầu 7 dịch vụ hoặc đầu tư nền tảng dùng chung trước khi pilot chứng minh nhu cầu. [S06]

| Năng lực | Trách nhiệm và contract đề xuất | Vai trò phụ trách | Áp dụng / điều kiện |
| --- | --- | --- | --- |
| Data & Knowledge | Nhận truy vấn và phạm vi quyền, trả đoạn tài liệu có nguồn, phiên bản và độ mới. | AI Engineer | MVP R27-04; tài liệu gốc là nguồn có thẩm quyền. |
| Model & Inference | Nhận yêu cầu chuẩn hóa, trả đầu ra có cấu trúc và usage qua adapter. | Platform Lead | Cấu hình có phiên bản; ADR-02, R27-05. Routing chỉ thử khi có nhu cầu đã đo. |
| Orchestration | Nhận tác vụ đã xác thực, thực hiện workflow và trả kết quả hoặc lỗi rõ ràng. | Tech Lead | Workflow cố định trước; ADR-03, R27-10. |
| Security & Guardrails | Nhận danh tính, tài nguyên và hành động; trả allow/deny trước truy xuất hoặc gọi tool. | Security Lead | Tối thiểu từ R27-04; kiểm thử mở rộng ở R27-06. |
| Application | Nhận yêu cầu người dùng, hiển thị kết quả, nguồn và fallback qua contract ứng dụng. | Tech Lead | Giữ logic workflow và quyền giao dịch tại backend/domain. |
| Observability | Nhận sự kiện có correlation ID; xuất trace đã loại dữ liệu nhạy cảm, latency, token và chi phí. | Platform Lead | Tối thiểu từ R27-04; dashboard và diễn tập R27-07. |
| Agentic Operations | Nhận cấu hình phát hành và bộ đánh giá có phiên bản; trả báo cáo gate và quyết định đề xuất. | QA Lead | Regression từ MVP; giám sát chất lượng khi pilot R27-08. |

Nếu R27-10 chứng minh cần nhiều agent được sở hữu hoặc tái sử dụng độc lập, lập catalog cấu hình ghi owner, capability, phiên bản, tool/quyền, contract và trạng thái vòng đời. Chỉ xét registry/discovery riêng khi catalog đơn giản không đáp ứng nhu cầu; ghi quyết định và TCO trong ADR-03. Đây là điều kiện mở lại, chưa phải nhiệm vụ xây registry. [S06]

## Timeline thực thi năm 2027

Mỗi nhiệm vụ ở trạng thái **Đề xuất**. Mốc tháng là cửa sổ lập kế hoạch. Tên vai trò dùng để phân công khi đội triển khai được xác định.

| ID | Thời gian | Mục tiêu hoặc ADR | Vai trò phụ trách | Phụ thuộc | Đầu ra và tiêu chí hoàn thành |
| --- | --- | --- | --- | --- | --- |
| R27-01 | Q1 · Tháng 1 | O28-01 | Product Owner | — | Chọn một nhóm người dùng và một quy trình tra cứu. Ghi nhận chủ sở hữu dữ liệu, phạm vi, ngân sách thử nghiệm và cách đo thời gian hiện tại. |
| R27-02 | Q1 · Tháng 2 | O28-01, ADR-01 | QA Lead | R27-01 | Bộ đánh giá có phiên bản, câu trả lời và nguồn chuẩn, ca thiếu dữ liệu và ca bị từ chối quyền. Chốt cách tách bộ phát triển và bộ kiểm thử giữ riêng. |
| R27-03 | Q1 · Tháng 3 | O28-01, ADR-01 | Tech Lead | R27-02 | Báo cáo baseline tìm kiếm trên bộ kiểm thử, ghi tỷ lệ hoàn thành, thời gian tác vụ, p95 và chi phí theo cách đo đã thống nhất. |
| R27-04 | Q2 · Tháng 4 | O28-01, ADR-01 | AI Engineer | R27-03 | MVP RAG chỉ đọc có trích dẫn, kiểm quyền trước retrieval, trace đã loại dữ liệu nhạy cảm và đo latency/token/chi phí theo request. Lưu cấu hình model, prompt, retrieval và phiên bản bộ đánh giá; chạy gate hồi quy và kiểm tra fallback trước khi bàn giao. [S06] Dùng dữ liệu đã được phép xử lý trong môi trường thử nghiệm hoặc dữ liệu tổng hợp. Chạy so sánh với baseline trên cùng câu hỏi, nguồn và quyền. Ra quyết định tiếp tục chuẩn bị pilot hoặc quay về baseline; chỉ mở pilot sau R27-06–07. |
| R27-05 | Q2 · Tháng 5 | O28-02, ADR-02 | Platform Lead | R27-04 | ADR về inference, biểu đồ p50/p95 và TCO cho tải thấp/cơ sở/cao. Ghi ngưỡng chi phí đề xuất và quyết định ứng viên nào được phép dùng dữ liệu pilot. Kiểm chứng đổi cấu hình qua adapter và rollback; nếu thử routing, so với một model trên cùng tác vụ và gate. [S06] |
| R27-06 | Q2 · Tháng 6 | O28-02 | Security Lead | R27-05 | Mở rộng các kiểm soát tối thiểu đã có từ R27-04. Kết quả kiểm thử từ chối truy cập, thu hồi quyền, rò rỉ qua cache/log, prompt injection và xóa dữ liệu khỏi index. Sửa các lỗi nghiêm trọng trước pilot. |
| R27-07 | Q3 · Tháng 7 | O28-02 | Platform Lead | R27-06 | Hoàn thiện dashboard từ telemetry R27-04 về chất lượng, độ trễ, chi phí và lỗi. Chốt owner, lịch lấy mẫu đánh giá production được phép, ngưỡng cảnh báo và phản ứng khi chất lượng giảm. Phân biệt điểm tự động với mẫu được người kiểm chứng. [S06] Diễn tập timeout, tắt AI và hoàn nguyên. Ghi thời gian khôi phục và chủ sở hữu sự cố. |
| R27-08 | Q3 · Tháng 8 | O28-01, O28-02 | Product Owner | R27-07 | Pilot có giới hạn, kèm báo cáo so sánh thời gian, tỷ lệ hoàn thành và chi phí với baseline. Vận hành lịch lấy mẫu đánh giá đã chốt ở R27-07, ghi cả ca khó và quyền bị từ chối. Chốt tiếp tục, thu hẹp hoặc dừng. |
| R27-09 | Q3 · Tháng 9 | O28-03, ADR-04 | AI Engineer | R27-08 | Thử nghiệm context có kiểm soát nếu pilot tiếp tục. So sánh độ đúng, độ mới, token, p95 và chi phí mỗi tác vụ thành công. Kiểm tra lỗi do nén hoặc dữ liệu xung đột. Nếu có nhu cầu qua phiên, thực hiện đối chứng memory theo quy trình R27-09 bên dưới; ghi quyết định giữ, bỏ hoặc hoãn từng phương án và tổng chi phí bảo trì. [S07] |
| R27-10 | Q4 · Tháng 10 | O28-02, O28-03, ADR-03 | Tech Lead | R27-08 | Nếu use case cần nhiều bước, lập sơ đồ phụ thuộc và ma trận quyền công cụ, sau đó thử trong sandbox theo quy trình dưới đây. Báo cáo kết quả theo nhóm tác vụ và quyết định giữ baseline, thử tiếp hoặc hoãn kèm điều kiện mở lại. |
| R27-13 | Q4 · Tháng 10, tùy chọn | ADR-05 | Tech Lead | — | Khi có năng lực thử nghiệm và repo sandbox được phép sử dụng, so sánh hai cách điều phối trên các tác vụ tương đương. Báo cáo số liệu, kết quả gate và quyết định giữ baseline hoặc mở pilot 2028. Nếu thiếu điều kiện, ghi nhận hoãn. |
| R27-11 | Q4 · Tháng 11 | O28-02, ADR-02 | Platform Lead | R27-08 | Kiểm thử tải và chuyển adapter hoặc hoàn nguyên về tìm kiếm. Cập nhật chi phí theo dữ liệu pilot và ghi kết quả diễn tập. |
| R27-12 | Q4 · Tháng 12 | O28-01, O28-02, O28-03 | Product Owner | R27-09, R27-10, R27-11 | Hồ sơ quyết định đầu tư 2028, gồm kết quả đã đo, các lựa chọn giữ/mở rộng/dừng, chủ sở hữu và điều kiện giải ngân. Ghi rõ các thử nghiệm đã hoãn. Nếu R27-13 có kết quả, đính kèm quyết định về coding agent riêng. |

**90 ngày đầu kể từ 09/11/2026.** Chọn ứng viên use case, xác định ai có thể cấp quyền đọc tài liệu và đối chiếu năng lực đội trong tháng 11–12. Dùng tháng 1 để chốt R27-01, sau đó bắt đầu thu thập bộ đánh giá nếu đã có quyền và người phụ trách.

### Cách đo thử nghiệm memory R27-09

- Chỉ mở nhánh thử này nếu pilot có nhu cầu qua phiên đã ghi nhận; giữ tháng 9, owner AI Engineer và phụ thuộc R27-08. Nếu chưa có nhu cầu, ghi hoãn và giữ retrieval hiện tại.
- QA Lead tách dữ liệu phát triển và tập giữ riêng theo chuỗi phiên, tránh ghi đáp án kiểm thử vào memory. So sánh retrieval không memory, ghi chú trong phiên và ghi chú có hợp nhất/kiểm chứng ngoài phiên trên cùng tác vụ, model, công cụ và quyền. Đây là thiết kế thử nghiệm đề xuất từ S07, chưa có kết quả nội bộ.
- Chỉ lưu transcript khi có mục đích, quyền và thời hạn lưu được phê duyệt. Mỗi ghi nhớ có nguồn, phiên bản và trạng thái kiểm chứng; transcript chỉ là bằng chứng tương tác. Kiểm chứng sự thật nghiệp vụ với nguồn có thẩm quyền. Phân biệt ghi chú, wiki tùy chọn và context nhỏ nạp đầu phiên.
- Trước thử nghiệm, AI Engineer và QA Lead chốt ngưỡng chất lượng, tỷ lệ ghi nhớ sai/cũ, tỷ lệ sửa đúng và độ trễ cập nhật; Platform Lead chốt ngân sách compute, lịch bảo trì và chi phí. Đo task success, groundedness, p95, token và chi phí mỗi tác vụ thành công gồm tạo, xác minh, lưu và bảo trì memory; phân tích theo số lần tái sử dụng.
- Kiểm thử ghi đè đồng thời, memory poisoning, thu hồi quyền và xóa các bản suy diễn. Dùng owner theo đối tượng, kiểm tra phiên bản khi ghi, snapshot và rollback trước khi đưa memory đã kiểm chứng vào sử dụng. Memory không có quyền sửa policy hoặc mở rộng tool.
- Chỉ giữ phương án đạt gate quyền/chất lượng và cải thiện đủ mức đã chốt so với retrieval; nếu chi phí bảo trì vượt lợi ích hoặc lỗi tăng, hoàn nguyên snapshot hoặc tắt memory. Không mặc định cần wiki, graph hay agent chạy nền. [S07]

### Cách đo thử nghiệm điều phối trong sản phẩm R27-10

- Phân nhóm tác vụ có bước độc lập và tác vụ có bước cần kết quả từ bước trước. So sánh workflow cố định tuần tự với phiên bản chạy đồng thời ở các bước đủ điều kiện. Giữ cùng bộ tác vụ đại diện, cấu hình model nếu có, công cụ, quyền và tải. Nếu cần chọn bước động, thử riêng phương án agent gọi công cụ chỉ đọc với baseline cố định đã chọn để tách tác động của cách điều phối khỏi tác động của việc chọn công cụ. [S02, S05]
- Ghi rõ dữ liệu và công cụ thuộc từng ranh giới nghiệp vụ. Kiểm quyền tại backend trước mỗi lần gọi theo người dùng và tác vụ. Dùng mã tương quan để nối các bước lập kế hoạch, gọi hoặc từ chối công cụ và xác minh đầu ra. Loại dữ liệu nhạy cảm khỏi trace. Kiểm thử công cụ ngoài phạm vi, thu hồi quyền và khả năng dựng lại chuỗi sự kiện. [S05]
- Trước khi chạy, chốt ngưỡng chất lượng, mức cải thiện tối thiểu và trần chi phí với chủ sở hữu. Đo tỷ lệ hoàn thành đúng, độ đúng của bằng chứng khi có, p95 đầu cuối, số lần gọi công cụ và chi phí mỗi tác vụ thành công. Chỉ chọn phương án mới khi cải thiện p95 hoặc chi phí đủ mức đã chốt, chỉ số còn lại trong ngân sách, đạt ngưỡng chất lượng, truy vết đầy đủ và không quan sát thấy vi phạm quyền nghiêm trọng. Nếu thiếu dữ liệu để kết luận, giữ baseline.

### Cách đo thử nghiệm coding agent R27-13

- Dùng các tác vụ có độ khó tương đương, cùng điều kiện truy cập, bộ kiểm tra CI và quy trình review. Giữ người duyệt PR độc lập với bên tạo thay đổi ở cả hai phương án.
- Với nhiều agent, phân quyền theo vai trò và cô lập nhánh hoặc vùng chỉnh sửa. Ghi lại nhiệm vụ, trạng thái bàn giao, phiên bản thay đổi và kết quả kiểm tra để truy vết từng PR. [S04]
- Đo thời gian từ lúc nhận tác vụ đến lúc PR được duyệt, thời gian review của con người, số vòng làm lại, xung đột tích hợp và chi phí mỗi PR được duyệt. Chốt mức cải thiện tối thiểu và trần chi phí trước khi chạy. Chỉ xét mở pilot nếu giảm thời gian đầu cuối đủ mức đã chốt, công review và lỗi tích hợp không tăng, chi phí trong trần và không quan sát thấy vi phạm quyền nghiêm trọng. Nếu mẫu quá ít để kết luận, tiếp tục dùng baseline.

## Gate, chi phí và quyết định dừng

| Gate | Cách kiểm chứng và hành động khi không đạt |
| --- | --- |
| Chất lượng và giá trị | Ngưỡng khởi điểm đề xuất cho pilot là ít nhất 90% trích dẫn đúng trên tập giữ riêng và giảm ít nhất 20% trung vị thời gian hoàn thành so với baseline, với tỷ lệ hoàn thành ít nhất ngang baseline. QA và Product Owner xác nhận cỡ mẫu, tiêu chí chấm và ngưỡng sau R27-03. Nếu không đạt, thu hẹp phạm vi hoặc giữ tìm kiếm. |
| Quyền và an toàn | Yêu cầu 0 lỗi nghiêm trọng quan sát được trong bộ kiểm thử rò rỉ, thu hồi quyền và thao tác ngoài quyền. Chặn pilot hoặc tắt tính năng khi phát hiện lỗi, sau đó kiểm thử lại trước khi mở. [S03] |
| Vận hành và kinh tế | Chốt ngân sách p95 và chi phí trên mỗi tác vụ thành công với chủ sở hữu sau baseline. Đo trên tải dự kiến và tải đỉnh trước khi mở rộng. Dùng adapter hoặc tìm kiếm làm đường lui khi inference vượt ngân sách hoặc gián đoạn. |
| Hồi quy và phát hành | Từ R27-04, mọi thay đổi model, prompt, retrieval hoặc tool phải có cấu hình và bộ đánh giá có phiên bản, so với bản tốt đã biết trên cùng tác vụ. QA Lead chốt ngưỡng trước thử nghiệm; chặn phát hành khi trượt gate chất lượng, quyền, p95 hoặc chi phí. Platform Lead giữ cấu hình rollback; R27-07 diễn tập và R27-08 theo dõi chất lượng bằng mẫu được phép, không lưu payload nhạy cảm mặc định. [S06] |
| Memory có điều kiện | R27-09 phải chứng minh nguồn và trạng thái kiểm chứng, cách ly quyền, xử lý ghi đồng thời, xóa bản suy diễn và rollback. QA/Platform chốt ngưỡng trước thử nghiệm; chặn đưa memory vào pilot khi trượt gate hoặc chưa tính chi phí bảo trì. [S07] |
| Mở rộng | Dùng kết quả hai vòng đo liên tiếp trên pilot để xét mở rộng. Đánh giá thêm chi phí vận hành, khả năng phân công trực sự cố và chi phí chuyển đổi nhà cung cấp. |

Nếu thử memory, cộng chi phí tạo/hợp nhất/kiểm chứng, lưu trữ và bảo trì vào TCO; báo cáo chi phí phân bổ theo số lần tái sử dụng, không chỉ token tại thời điểm trả lời. [S07]

TCO tháng = inference + truy xuất + lưu trữ + chi phí tích hợp phân bổ + đánh giá + vận hành + rà soát của con người. Chi phí mỗi tác vụ thành công = tổng chi phí phân bổ, gồm retry và fallback, chia cho số tác vụ hoàn thành đạt chuẩn. Ước tính công sức theo vai trò sau R27-01 và chi phí theo ba mức tải sau R27-03. Ưu tiên cấp ngân sách theo gate từng quý. Hiện chưa có số liệu sử dụng hoặc báo giá để xác lập TCO.

## Nguồn và lịch sử cập nhật

| ID | Nguồn | Công bố / kiểm tra | Phạm vi sử dụng |
| --- | --- | --- | --- |
| S01 | [Adi Polak, Systemic Approach to Memory, Knowledge, and Context in Agentic AI Architectures](https://www.infoq.com/articles/agentic-ai-context-memory-knowledge/) | 02/11/2026 / 09/11/2026 | Góc nhìn về context, memory và knowledge. Dùng để thiết kế ADR-04 và R27-09. Bài viết đưa ra quan điểm thiết kế và thiếu benchmark cho workload này. |
| S02 | [Anthropic, Building effective AI agents](https://www.anthropic.com/research/building-effective-agents) | 19/12/2024 / 09/11/2026 | Các mẫu workflow và agent, cùng lý do bắt đầu từ cấu trúc đơn giản. Dùng cho ADR-03 và R27-10. Phạm vi sử dụng là mẫu thiết kế, vì công cụ cụ thể đã thay đổi từ thời điểm bài đăng. |
| S03 | [NIST AI 600-1, Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | 26/07/2024 / 09/11/2026 | Hướng dẫn tự nguyện về quản lý rủi ro AI tạo sinh. Dùng để định hướng đánh giá trước triển khai và giám sát ở R27-06–07. Các gate trong file là đề xuất cho kế hoạch này. |
| S04 | [Denis Shokhirev, Why one agent is no longer enough](https://gerdennisai.com/blog/multi-agent-cli-orchestration-without-chaos) | 09/11/2026 / 09/11/2026 | Kinh nghiệm triển khai tách vai trò, cô lập vùng sửa và lưu trạng thái điều phối. Dùng để thiết kế ADR-05 và R27-13. Bài viết chưa đưa ra benchmark đối chứng cho hiệu quả multi-agent. |
| S05 | [Rafał Gancarz, Agentic AI Architecture: Current Challenges and Future Opportunities](https://www.infoq.com/articles/agentic-ai-architecture-challenges-opportunities/) | 09/11/2026 / 10/11/2026 | Phân tích ranh giới nghiệp vụ, điều phối theo loại tác vụ, quyền theo tác vụ và truy vết theo bước. Dùng cho ADR-03 và R27-10. Bài viết tổng hợp góc nhìn và nghiên cứu bên ngoài. Hiệu quả trên workload này cần đo trong pilot. |
| S06 | [AWS, Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic AI reference architecture](https://aws.amazon.com/blogs/machine-learning/pluggable-agentic-ai-framework-a-seven-layer-composable-enterprise-agentic-ai-reference-architecture-on-amazon-bedrock-agentcore/) | 09/11/2026 / 11/11/2026 | Kiến trúc tham chiếu của nhà cung cấp: contract phân lớp, cấu hình inference, observability và continuous evaluation. Dùng cho rà soát 7 năng lực, ADR-02–03, R27-04–08, R27-11 và gate phát hành. Chưa có benchmark cho workload này; không coi dịch vụ AWS, registry, multi-agent hoặc đánh giá mọi session là bắt buộc. Các gate và cách lấy mẫu là đề xuất của chiến lược. |
| S07 | [Lance Martin, The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) | 06/11/2026 / 12/11/2026 | Thử nghiệm của Anthropic về phân tầng memory và hợp nhất/kiểm chứng ngoài phiên. Dùng cho ADR-04, R27-09 và gate/TCO memory. Hiệu quả phụ thuộc tác vụ/model; không suy rộng benchmark thành ROI của đội, không coi wiki hoặc dreaming là bắt buộc. |

| Phiên bản | Ngày | Nguồn | Thay đổi |
| --- | --- | --- | --- |
| 0.1 | 09/11/2026 | S01–S03 | Tạo chiến lược, ADR đề xuất và 12 nhiệm vụ năm 2027. Chờ xác nhận bối cảnh triển khai và đo baseline. |
| 0.2 | 09/11/2026 | S04 | Bổ sung ADR-05 và thử nghiệm coding agent tùy chọn R27-13, tách khỏi pilot tra cứu tài liệu và workflow gọi công cụ của sản phẩm. |
| 0.3 | 10/11/2026 | S05 | Cập nhật ADR-03 và R27-10 với thử nghiệm điều phối theo phụ thuộc, phân quyền theo phạm vi và gate truy vết cho workflow trong sản phẩm. |
| 0.4 | 11/11/2026 | S06 | Bổ sung rà soát 7 năng lực và catalog có điều kiện; cập nhật ADR-02–03, đưa quyền/trace/evaluation vào R27-04, hoàn thiện R27-05–08 và gate hồi quy/rollback liên kết R27-11. Cập nhật skill và workbook cùng đợt; giữ nguyên hướng pilot và trạng thái Đề xuất. |
| 0.5 | 12/11/2026 | S07 | Mở rộng ADR-04 và R27-09 với đối chứng memory, kiểm chứng nguồn, ghi đồng thời, rollback và TCO bảo trì. Cập nhật skill và context reference cùng đợt; giữ pilot RAG, lịch và trạng thái Đề xuất. |

Khi có reference mới, cập nhật các ADR, nhiệm vụ và gate chịu ảnh hưởng theo [quy trình duy trì chiến lược](.skills/ai-architecture-strategy-2028/SKILL.md#maintain-the-strategy-file). Rà soát lại các giả định và quyết định đầu tư vào cuối mỗi quý.
