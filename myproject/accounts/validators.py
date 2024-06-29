# myapp/validators.py

from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator
from django.utils.translation import gettext_lazy as _

class ChineseMinimumLengthValidator(MinimumLengthValidator):
    def __init__(self, min_length=8):
        super().__init__(min_length)
        self.message = _("密码长度不能少于 %(min_length)d 个字符。") % {'min_length': min_length}

class ChineseCommonPasswordValidator(CommonPasswordValidator):
    def __init__(self):
        super().__init__()
        self.message = _("密码过于简单，不安全。请不要使用常见密码。")

class ChineseNumericPasswordValidator(NumericPasswordValidator):
    def __init__(self):
        super().__init__()
        self.message = _("密码不能完全由数字组成。")
