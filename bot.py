from dhooks import Webhook, File
import datetime
import time
hook = Webhook('https://discord.com/api/webhooks/822960791849664562/mjYqmK9LLYGECgASlw84kw-VTz1L0wcw_AnappyCEQjojp1eourOQvi0cTQRFeF4DowO')
zdj = File('pikachu.gif')
d = datetime.datetime.today()
while True:
  d = datetime.datetime.today()
  time.sleep(3)
  if d.hour == 11 and d.minute == 10:
       hook.send('test, bo zmiana czasu', file = zdj)
       time.sleep(60)
