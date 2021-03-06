import os
from datetime import datetime


def set_filename_format(now, instance, filename):
    return "{date}-{microsecond}{extension}".format(
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def services_path(instance, filename):
    now = datetime.now()

    path = "services/{year}/{month}/{day}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        filename=set_filename_format(now, instance, filename),
    )
    return path
