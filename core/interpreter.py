def giai_nghia(name):
    """Trả lời ngắn gọn ý triết học của quẻ"""
    mapping = {
        "Thuần Càn": "Thời của hành động, dấn thân, khai mở. Nhưng phải giữ chính đạo.",
        "Thuần Khôn": "Thời của tĩnh – thuận theo, dưỡng nội khí, nuôi gốc.",
        "Thủy Hỏa Ký Tế": "Mọi việc đã viên mãn, nhưng phải giữ thế ổn định, đừng chủ quan.",
        "Hỏa Thủy Vị Tế": "Việc còn dang dở, đừng vội, cần thêm thời gian và lòng tin."
    }
    return mapping.get(name, "Đang bổ sung.")
