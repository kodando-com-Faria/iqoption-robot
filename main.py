from iqoptionapi.stable_api import IQ_Option
import logging
import userdata


asset = "EURUSD-OTC"
maxdict = 10
size = 300

logging.disable(level=(logging.DEBUG))

user = userdata.mainUser
Iq = IQ_Option(user["username"], user["password"])
check, reason = Iq.connect()

MODE = "PRACTICE"  # /"REAL"
Iq.change_balance(MODE)

# compra simples no binario
# duration = 1
# Iq.buy(1, asset, "put", duration)

# pegar dados do perfil
profile = Iq.get_profile_ansyc()
print(profile)
