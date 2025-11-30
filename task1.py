"""
مسئله اول: طول بزرگ‌ترین زیررشته بدون تکرار

این برنامه طول بزرگترین زیررشته‌ای را که هیچ کاراکتری در آن تکرار نشده است پیدا می‌کند.
"""


def longest_substring_without_repetition(s: str) -> int:
    """
    پیدا کردن طول بزرگترین زیررشته بدون تکرار کاراکتر
    
    Args:
        s: رشته ورودی
        
    Returns:
        int: طول بزرگترین زیررشته بدون تکرار
        
    Examples:
        >>> longest_substring_without_repetition("ABCABCFKAB")
        5
        >>> longest_substring_without_repetition("AAA")
        1
        >>> longest_substring_without_repetition("ABCDEF")
        6
    """
    if not s:
        return 0
    
    # استفاده از تکنیک پنجره لغزان (Sliding Window)
    char_index = {}  # ذخیره آخرین موقعیت هر کاراکتر
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        current_char = s[end]
        
        # اگر کاراکتر قبلا دیده شده و در پنجره فعلی است
        if current_char in char_index and char_index[current_char] >= start:
            start = char_index[current_char] + 1
        
        # به‌روزرسانی موقعیت کاراکتر
        char_index[current_char] = end
        
        # محاسبه طول فعلی و به‌روزرسانی حداکثر
        current_length = end - start + 1
        max_length = max(max_length, current_length)
    
    return max_length


if __name__ == "__main__":
    # مثال‌های استفاده
    test_cases = [
        "ABCABCFKAB",
        "AAA",
        "ABCDEF",
        "PWWKEW",
        ""
    ]
    
    print("نتایج تست:")
    print("-" * 50)
    for test in test_cases:
        result = longest_substring_without_repetition(test)
        print(f"رشته: '{test}' → طول: {result}")

