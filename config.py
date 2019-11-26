DEBUG = True

DB_USERNAME = 'my_bbs'
DB_PASSWORD = 'my_bbs'
DB_HOST = '172.16.100.101'
DB_PORT = '3306'
DB_NAME = 'my_bbs'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

SQLALCHEMY_DATABASE_URI = DB_URI
# 模型对象追踪，默认情况下，一旦模型对象有改变，就发送信号，此处关闭该功能
SQLALCHEMY_TRACK_MODIFICATIONS = False
