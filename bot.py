from dhooks import Webhook, File
import datetime
import time
hook = Webhook('https://discord.com/api/webhooks/822960833339588608/jR4wJDqZMqvINZt2RjhZ8x8ed3_XqYgfX_fE9ydAHbV-0X0eT0u2qQV_UvEE9GC6zHTl')
d = datetime.datetime.today()
zdj = File('papiezyk.jpg')
while True:
  d = datetime.datetime.today()
  time.sleep(3)
  if d.hour == 17 and d.minute == 30:
       hook.send('<@&662300886671818752> Dzisiaj przypada 16. rocznica śmierci Jana Pawła 2. Zasłynął jako niestrudzony pielgrzym, myśliciel i filozof oraz inspirator przemian na świecie. Dziedzictwo Papieża Polaka pozostało z wiernymi na całym świecie i wciąż jest żywe. Dlatego taktyczne 2137 na chacie!', file = zdj)
       time.sleep(60)
