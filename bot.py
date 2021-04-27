from dhooks import Webhook, File
import datetime
import time
hook = Webhook('https://discord.com/api/webhooks/822960791849664562/mjYqmK9LLYGECgASlw84kw-VTz1L0wcw_AnappyCEQjojp1eourOQvi0cTQRFeF4DowO')
d = datetime.datetime.today()
#zdj = File('kremowki.jpg')
while True:
  d = datetime.datetime.today()
  time.sleep(3)
  if d.hour == 19 and d.minute == 37:
       hook.send('<@&822960885156806697> 2137 wariatyyy!')
       time.sleep(60)
