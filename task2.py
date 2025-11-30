"""
مسئله دوم: بررسی چهار تا ۱ پشت سر هم (با در نظر گرفتن چرخش)

این برنامه بررسی می‌کند که آیا در یک رشته باینری ۷ رقمی، چهار تا عدد ۱ پشت سر هم وجود دارد یا خیر.
توجه: رشته به صورت چرخشی در نظر گرفته می‌شود (آخر رشته به اول وصل است).
"""


def has_four_consecutive_ones(binary_str: str) -> bool:
    """
    بررسی وجود چهار عدد ۱ پشت سر هم در رشته باینری (با در نظر گرفتن چرخش)
    
    Args:
        binary_str: رشته باینری ورودی
        
    Returns:
        bool: True اگر چهار ۱ پشت سر هم وجود داشته باشد، در غیر این صورت False
        
    Examples:
        >>> has_four_consecutive_ones("1010111")
        True
        >>> has_four_consecutive_ones("1010101")
        False
        >>> has_four_consecutive_ones("1111000")
        True
    """
    if not binary_str or len(binary_str) < 4:
        return False
    
    # برای بررسی حالت چرخشی، رشته را به خودش اضافه می‌کنیم
    # اما فقط به اندازه ۳ کاراکتر اول (چون به دنبال ۴ تا ۱ هستیم)
    circular_str = binary_str + binary_str[:3]
    
    # جستجوی چهار تا ۱ پشت سر هم
    target = "1111"
    if target in circular_str:
        return True
    
    return False


if __name__ == "__main__":
    # مثال‌های استفاده
    test_cases = [
        "1010111",  # True - سه تا ۱ آخر + یک ۱ اول = ۱۱۱۱
        "1010101",  # False - هیچ چهار ۱ پشت سر همی نیست
        "1111000",  # True - چهار ۱ پشت سر هم در ابتدا
        "0001111",  # True - چهار ۱ پشت سر هم در انتها
        "1110111",  # True - سه تا ۱ + یک ۱ در ابتدا
        "0101010",  # False
    ]
    
    print("نتایج تست:")
    print("-" * 50)
    for test in test_cases:
        result = has_four_consecutive_ones(test)
        print(f"رشته: '{test}' → نتیجه: {result}")

