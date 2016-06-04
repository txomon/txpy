from __future__ import unicode_literals

import datetime
import pytz

TIMESTAMP_FORMAT = '%Y%m%dT%H%M%S'


def serialize_timestamp(ts):
    assert isinstance(ts, datetime.datetime)
    timestamp = ts.strftime(TIMESTAMP_FORMAT)
    if ts.tzinfo != datetime.timezone.utc:
        timezone = ts.tzname()
        if timezone not in pytz.all_timezones:
            raise ValueError("Timezone %s doesn't exist" % timezone)
        timestamp = '{}Z{}'.format(timestamp, timezone)
    return timestamp


def unserialize_timestamp(timestamp):
    if 'Z' not in timestamp:
        timestamp, zone = timestamp, 'UTC'
    else:
        timestamp, zone = timestamp.split('Z', maxsplit=1)

    tz = pytz.timezone(zone)
    ts = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    return pytz.tz.localize(ts)
