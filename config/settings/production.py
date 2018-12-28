from .base import *

DEBUG = False

STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)
MEDIA_ROOT = '/var/www/{}/media'.format(PROJECT_NAME)

LOGGING = {
    #  バージョンは「1」固定
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d}'
            '%(pathname)s:%(lineno)d %(message)s'
        }
    },
    # ハンドラ
    'handlers': {
        # ファイル出力用ハンドラ
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}.log'.format(PROJECT_NAME),
            'formatter': 'production',
        }
    },
    # ロガー
    'loggers': {
        #自作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },

    },

}
