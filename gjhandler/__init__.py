# -*- coding: utf-8 -*-

import json
import logging.handlers
import math


class GoogleJsonHandler(logging.handlers.RotatingFileHandler):

    def __init__(self, filename):
        super(GoogleJsonHandler, self).__init__(
            filename,
            maxBytes=8*1024*1024,
            backupCount=5
        )

    def format(self, record):
        message = super(GoogleJsonHandler, self).format(record)
        subsecond, second = math.modf(record.created)
        payload = {
            "message": message,
            "timestamp": {
                "seconds": int(second),
                "nanos": int(subsecond * 1e9)
            },
            "thread": record.thread,
            "severity": record.levelname,
        }
        return json.dumps(payload, ensure_ascii=False)
