# ---------------------------------------------------------------------------
# --------------------------------错误配置文件--------------------------------
#
# EC Error Code     错误码
# ER Error Reason   错误原因
#
# ---------------------------------------------------------------------------

EC_REQ_NORMAL = 0
# 通用错误[1-100]


# 注册错误[101-200]
EC_REGISTER_PHONENUM_TYPE_ERROR = 101
ER_REGISTER_PHONENUM_TYPE_ERROR = "手机号格式错误, 请重新输入"
EC_REGISTER_PASSWORD_TYPE_ERROR = 102
ER_REGISTER_PASSWORD_TYPE_ERROR = "密码格式错误, 请重新输入"
EC_REGISTER_USERID_REPEAT = 103
ER_REGISTER_USERID_REPEAT = "该账号已被注册"
EC_REGISTER_IDCARD_TYPE_ERROR = 104
ER_REGISTER_IDCARD_TYPE_ERROR = "身份证号格式错误, 请重新输入"


# 登录错误[201-300]
EC_LOGIN_USERID_ERROR = 201
ER_LOGIN_USERID_ERROR = "账号不存在, 请重新输入"
EC_LOGIN_PASSWORD_ERROR = 202
ER_LOGIN_PASSWORD_ERROR = "密码错误, 请重新输入"
ER_LOGIN_INVALID = 203
ER_LOGIN_INVALID = "无效账户, 请尝试登录"

# 商城错误[301-400]
EC_SHOP_VERSION_LOW = 301
ER_SHOP_VERSION_LOW = "商城版本过低, 请刷新重试"
EC_SHOP_NOT_EXIST = 302
ER_SHOP_NOT_EXIST = "该道具不存在"
EC_CLIENT_VERSION_LOW = 303
ER_CLIENT_VERSION_LOW = "客户端版本过低, 请更新后重试"
EC_SHOP_PAYTYPE_ERROR = 304
ER_SHOP_PAYTYPE_ERROR = "不支持当前选择支付方式"
EC_SHOP_MONEY_NOT_ENONGH = 305
ER_SHOP_MONEY_NOT_ENONGH = "余额不足, 请及时充值"
