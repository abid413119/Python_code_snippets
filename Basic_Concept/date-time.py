import datetime
import pytz

d = datetime.date(2016, 7, 24)
today = datetime.date.today()
print(today)
print(today.weekday())      # Monday 0 Sunday 6
print(today.isoweekday())   # Monday 1 Sunday 7

# timedelta

tdelta = datetime.timedelta(days=7)
print(today + tdelta)                   # day a week ahead 
print(today - tdelta)                   # day a week before

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2019, 5, 8)
till_bday = bday - today
print(till_bday)


# --------------------------------------------------------------

t = datetime.time(9, 30, 45, 10000)     # ( hour, min, sec, microsec )

dt = datetime.datetime(2019, 2, 23, 12, 20, 34, 1000)
print(dt)
print(dt.time())

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_now)
# print(dt_now)
# print(dt_utcnow)

dt = datetime.datetime(2018, 11, 24, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)


dt_dhaka = dt_now.astimezone(pytz.timezone('Asia/Dhaka'))
print(dt_dhaka)

