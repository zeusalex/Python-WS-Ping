log_dict = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s %(threadName)10s [%(levelname)s] %(name)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'fileError': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'error.log',
            'mode': 'a',
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
        },
        'fileDebug': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'debug.log',
            'mode': 'a',
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
        },
        'fileInfo': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'info.log',
            'mode': 'a',
            'maxBytes': 1024 * 1024 * 1024,
            'backupCount': 1,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'fileError', 'fileInfo', 'fileDebug'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

config = {
    'port': 8889,
}

