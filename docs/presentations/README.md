# Chiến lược kiến trúc AI 2028

Presentation tiếng Việt gồm 16 slide, tóm lược bản đề xuất 0.6 cập nhật ngày 19/11/2026.

- [PowerPoint](AI_ARCHITECTURE_STRATEGY_2028.pptx)
- [Chiến lược nguồn](../../AI_ARCHITECTURE_STRATEGY_2028.md)
- Snapshot nguồn: `b525e994c35b6d2f5bab1eda3f2b1dd4894ad799`.

Nhiệm vụ, vai trò, lịch và ngưỡng đều là đề xuất. Presentation không bổ sung dự báo hoặc kết quả triển khai ngoài bản nguồn. Nguồn snapshot được ghi trong speaker notes của từng slide.

## Nội dung từng slide

### 1. Chiến lược kiến trúc AI 2028

Kế hoạch thực thi năm 2027

- **Bản đề xuất 0.6:** Nguồn cập nhật 19/11/2026. Phạm vi, ngân sách và nhân sự chờ xác nhận ở R27-01.

### 2. Phạm vi đầu tư

Một quy trình tra cứu tài liệu nội bộ

- **Điểm bắt đầu:** Trợ lý chỉ đọc có trích dẫn. Đo hiệu quả so với tìm kiếm và tra cứu thủ công.

- **Phạm vi repo:** Lưu chiến lược và phương pháp. Chưa có bằng chứng triển khai sản phẩm trong repo chiến lược.

- **Quyết định R27-01:** Chốt nhóm người dùng, dữ liệu được phép xử lý, owner nghiệp vụ và ngân sách thử nghiệm.

### 3. Kết quả cần chứng minh đến 2028

Bốn mục tiêu của chiến lược

- **O28-01 · Tra cứu hữu ích:** Câu trả lời đúng, nguồn kiểm chứng được và thời gian tác vụ giảm.

- **O28-02 · Vận hành có kiểm soát:** Đo chất lượng, p95 và chi phí mỗi tác vụ thành công. Diễn tập ngắt AI và hoàn nguyên.

- **O28-03 · Mở rộng theo bằng chứng:** Quyết định mở rộng, thu hẹp hoặc dừng dựa trên pilot.

- **O28-04 · Quyết định có quản trị:** Bằng chứng nguồn, policy có phiên bản, người duyệt có danh tính và audit.

### 4. Danh mục use case

Thứ tự và điều kiện đầu tư

- **1 · Hỏi đáp tài liệu:** Ưu tiên đầu tiên. Cần quyền dữ liệu, trích dẫn và fallback về tìm kiếm.

- **2 · Đề xuất hoặc soạn nháp:** Sau gate pilot chỉ đọc. Người dùng duyệt trước tác động nghiệp vụ.

- **3 · Workflow gọi công cụ:** Sandbox với tool chỉ đọc. Hành động ghi cần quyết định riêng.

- **4 · Đề xuất bổ sung tồn kho:** Sandbox sau gate an toàn. So với quy tắc + quản lý, không tự tạo đơn mua.

### 5. Kịch bản năm 2028

Tín hiệu đo quyết định hướng đầu tư

- **Cơ sở:** Tra cứu có trích dẫn tạo giá trị ổn định: chuẩn hóa ingestion, đánh giá và đường lui.

- **Tăng tốc:** Chi phí giảm hoặc tác vụ nhiều bước tốt hơn qua hai vòng đo: thử workflow giới hạn.

- **Hạn chế:** Chi phí vượt trần, dữ liệu bị hạn chế hoặc chất lượng chưa đạt: thu hẹp, giữ tìm kiếm, xét inference khác.

### 6. Luồng đọc và nguồn dữ liệu

Ranh giới trách nhiệm trong kiến trúc đích

- **Truy cập và retrieval:** Ứng dụng xác thực, kiểm quyền trước retrieval và chỉ lấy tài liệu thuộc phạm vi người dùng.

- **Context và inference:** Ghép context có giới hạn, gọi model qua adapter, kiểm tra trích dẫn.

- **Kết quả và fallback:** Trả câu trả lời có nguồn hoặc chuyển về tra cứu thủ công.

- **Vòng đời dữ liệu:** Ingest lưu owner, phiên bản và quyền. Cache, index, log tuân thủ lưu giữ và xóa. Nguồn gốc có thẩm quyền.

### 7. Bảy năng lực kiến trúc

Ranh giới logic có thể cùng nằm trong một ứng dụng

- **Dữ liệu và suy luận:** Data & Knowledge quản lý nguồn. Model & Inference cung cấp adapter và usage.

- **Ứng dụng và điều phối:** Application giữ contract người dùng. Orchestration thực hiện workflow đã xác thực.

- **Quyền và quan sát:** Security & Guardrails kiểm allow/deny. Observability nối trace và đo latency, token, chi phí.

- **Agentic Operations:** Bộ đánh giá và cấu hình có phiên bản. Chỉ xét registry khi catalog đơn giản không đáp ứng nhu cầu.

### 8. Các quyết định kiến trúc

ADR-01 đến ADR-06

- **ADR-01 / ADR-02:** Tìm kiếm làm baseline cho RAG. Model API qua adapter nếu dữ liệu cho phép, self-hosted theo quyền và TCO.

- **ADR-03 / ADR-04:** Workflow cố định trước agent. Retrieval có giới hạn trước context phức tạp hoặc memory dài hạn.

- **ADR-05:** Một coding agent với kiểm chứng độc lập làm baseline. Nhiều agent cần thử nghiệm riêng.

- **ADR-06:** AI đề xuất, backend kiểm chính sách và quyền. Phê duyệt, thực thi có quyền và audit tách trách nhiệm.

### 9. Q1–Q2 năm 2027

Baseline trước MVP, an toàn trước pilot

- **Tháng 1–3 · R27-01/02/03:** Product Owner chốt use case. QA Lead tạo tập đánh giá giữ riêng. Tech Lead đo baseline tìm kiếm.

- **Tháng 4 · R27-04:** AI Engineer xây MVP RAG có trích dẫn, quyền, trace và gate hồi quy. So sánh trên cùng câu hỏi và nguồn.

- **Tháng 5 · R27-05:** Platform Lead đánh giá inference, p50/p95 và TCO theo ba mức tải. Kiểm chứng rollback cấu hình.

- **Tháng 6 · R27-06:** Security Lead kiểm rò rỉ, thu hồi quyền, cache/log, injection và xóa index. Sửa lỗi nghiêm trọng trước pilot.

### 10. Q3–Q4 năm 2027

Pilot và hồ sơ quyết định đầu tư

- **Tháng 7–8 · R27-07/08:** Platform Lead hoàn thiện giám sát, diễn tập tắt AI. Product Owner chạy pilot giới hạn và chốt tiếp tục/thu hẹp/dừng.

- **Tháng 9–10 · R27-09/10:** Sau R27-08: AI Engineer thử context/memory có nhu cầu. Tech Lead thử điều phối và quyền tool trong sandbox.

- **Tháng 11 · R27-11:** Platform Lead kiểm tải, chuyển adapter hoặc hoàn nguyên tìm kiếm. Phụ thuộc R27-08.

- **Tháng 12 · R27-12:** Product Owner tổng hợp R27-09/10/11: kết quả đo, lựa chọn đầu tư, owner, điều kiện giải ngân và thử nghiệm đã hoãn.

### 11. Các thử nghiệm tùy chọn

R27-13 và R27-14 có phạm vi riêng

- **R27-13 · Tháng 10 · Tech Lead:** So một coding agent với nhiều agent trên tác vụ tương đương. Cần năng lực và repo sandbox được phép.

- **Gate coding agent:** Đo thời gian tới PR được duyệt, công review, làm lại, xung đột và chi phí mỗi PR. Giữ review độc lập.

- **R27-14 · Tháng 11 · Tech + Security Lead:** Sau R27-08 và R27-10. So quy tắc + người duyệt với AI có policy gate.

- **Gate quyết định:** Đo correctness, vi phạm policy, độ trễ duyệt, audit và chi phí quyết định hợp lệ. FnBAz PR #7 còn là proof of concept.

### 12. Memory và điều phối

Thử nghiệm đối chứng trước khi giữ phương án mới

- **Memory R27-09:** So không memory, ghi chú trong phiên và hợp nhất/kiểm chứng ngoài phiên. Tách dữ liệu theo chuỗi phiên.

- **Điều kiện memory:** Nguồn, phiên bản, trạng thái kiểm chứng, xóa theo quyền và rollback. TCO gồm chi phí tạo và bảo trì.

- **Điều phối R27-10:** So tuần tự với chạy đồng thời ở bước độc lập. Thử chọn tool động riêng với baseline cố định.

- **Điều kiện agent:** Quyền backend ở từng lần gọi, schema, allowlist và giới hạn thời gian. Chỉ chọn khi đủ bằng chứng cải thiện.

### 13. Quyết định AI có quản trị

ADR-06 và thử nghiệm R27-14

- **Bằng chứng và đề xuất:** Knowledge/Evidence cung cấp nguồn. AI tạo recommendation, model không có quyền giao dịch.

- **Policy và phê duyệt:** Backend xác minh danh tính, policy version và quyền. Người duyệt có danh tính khi cần.

- **Thực thi và audit:** Chỉ thực thi sau kiểm quyền/phê duyệt. Lưu provenance, correlation ID, kết quả và lý do từ chối.

- **Các ca chặn triển khai:** Reviewer giả mạo, policy drift, replay, race, rollback và audit thiếu sự kiện. Kiến trúc S08 chưa chứng minh ROI nội bộ.

### 14. Gate pilot và mở rộng

Các ngưỡng dưới đây là đề xuất

- **Chất lượng và giá trị:** Ít nhất 90% trích dẫn đúng, giảm ít nhất 20% trung vị thời gian và tỷ lệ hoàn thành ngang baseline trở lên.

- **Quyền và an toàn:** 0 lỗi nghiêm trọng quan sát được trong bộ kiểm thử. Có lỗi: chặn pilot hoặc tắt tính năng rồi kiểm thử lại.

- **Vận hành và phát hành:** Chốt p95 và trần chi phí sau baseline. Chặn thay đổi trượt gate, giữ cấu hình rollback.

- **Mở rộng:** Hai vòng đo liên tiếp đạt yêu cầu. QA và Product Owner xác nhận cỡ mẫu, cách chấm và ngưỡng sau R27-03.

### 15. Kinh tế và quyết định dừng

Chưa có số liệu sử dụng hoặc báo giá TCO

- **TCO tháng:** Inference, retrieval, lưu trữ, tích hợp phân bổ, đánh giá, vận hành và rà soát của con người.

- **Chi phí mỗi tác vụ thành công:** Tổng chi phí phân bổ gồm retry và fallback, chia số tác vụ hoàn thành đạt chuẩn.

- **Điều kiện thu hẹp hoặc dừng:** Không cải thiện đủ so baseline, vượt ngân sách hoặc trượt gate quyền/chất lượng. Giữ phương án tìm kiếm.

- **90 ngày đầu theo bản nguồn:** Từ 19/11/2026: chọn ứng viên use case, owner dữ liệu và năng lực đội. Tháng 1 chốt R27-01 rồi thu thập tập đánh giá.

### 16. Nguồn và phạm vi bằng chứng

Tóm lược từ chiến lược v0.6

- **S01–S03:** Context/memory của Adi Polak, Building effective AI agents và NIST AI 600-1. Cơ sở thiết kế và quản lý rủi ro.

- **S04–S06:** Điều phối coding agent, ranh giới agentic AI và kiến trúc tham chiếu bảy lớp. Chưa có benchmark cho workload của đội.

- **S07–S08:** Components of agent memory và governed cognitive enterprises. Dùng thiết kế đối chứng và gate quản trị.

- **Nguồn có thẩm quyền của deck:** AI_ARCHITECTURE_STRATEGY_2028.md tại commit b525e994. Toàn bộ nhiệm vụ là đề xuất, chưa phải kết quả triển khai.
