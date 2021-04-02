from dhooks import Webhook, File
import datetime
import time
hook = Webhook('https://discord.com/api/webhooks/822960791849664562/mjYqmK9LLYGECgASlw84kw-VTz1L0wcw_AnappyCEQjojp1eourOQvi0cTQRFeF4DowO')
d = datetime.datetime.today()
zdj = File('papiezyk.jpg')
while True:
  d = datetime.datetime.today()
  time.sleep(3)
  if d.hour == 19 and d.minute == 37:
       hook.send('<@&822960885156806697> Dzisiaj przypada 16. rocznica śmierci Jana Pawła 2. Zasłynął jako niestrudzony pielgrzym, myśliciel i filozof oraz inspirator przemian na świecie. Dziedzictwo Papieża Polaka pozostało z wiernymi na całym świecie i wciąż jest żywe. Dlatego taktyczne 2137 na chacie!', file = zdj)
       time.sleep(60)
