from .base import *
DEBUG = True
# 开启日志
DRF_API_LOGGER_DATABASE = True
DRF_API_LOGGER_SIGNAL = True
DRF_API_LOGGER_PATH_TYPE = 'ABSOLUTE'  # 路径类型
DRF_API_LOGGER_SKIP_URL_NAME = []  # 跳过的url
DRF_API_LOGGER_SKIP_NAMESPACE = []  # 跳过的命名空间
DRF_API_LOGGER_EXCLUDE_KEYS = []  # 排除的key
DRF_LOGGER_QUEUE_MAX_SIZE = 500  # 队列的最大日志条数
DRF_LOGGER_QUEUE_FLUSH_INTERVAL = 10  # 日志队列刷新时间间隔，单位为秒
DRF_API_LOGGER_LOGS_EXPIRE_DAYS = 5  # 日志过期时间，单位为天


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ChSpeed',
        'USER': 'root',  # 数据库名字用户名
        'PASSWORD': '',  # 数据库密码
        'HOST': '127.0.0.1',
        'PORT': '3306',  # 端口
        'OPTIONS': {'charset': 'utf8mb4'},  # 打开数据库 编码格式 ——解决4字节表情无法储存问题
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4000",
    "http://127.0.0.1:4000",
]
