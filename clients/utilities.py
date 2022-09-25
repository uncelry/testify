import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    """Get file name including timestamp and it's path"""
    return '%s%s' % (datetime.datetime.now().timestamp(), splitext(filename)[1])
