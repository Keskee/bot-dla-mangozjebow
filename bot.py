from dhooks import Webhook, File
import datetime
import time
hook = Webhook('https://discord.com/api/webhooks/822960833339588608/jR4wJDqZMqvINZt2RjhZ8x8ed3_XqYgfX_fE9ydAHbV-0X0eT0u2qQV_UvEE9GC6zHTl')
zdj = File('pope.gif')
d = datetime.datetime.today()
while True:
  d = datetime.datetime.today()
  time.sleep(3)
  if d.hour == 16 and d.minute == 57:
       hook.send('<@&662300886671818752> Kręcimy śmigłem!', file = zdj)
       time.sleep(60)
