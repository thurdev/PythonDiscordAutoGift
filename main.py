import re

from client import Client

client = Client()

client.login("MzA3NDUwODMwNTk1MDMxMDQx.XzA6TQ.pyJ1NvVRQ39vKWHXe6_X1DuMA_4")

@client.ready
def onReady():
    print("Logged in as {}#{}".format(client.getUsername(), client.getDiscriminator()))

@client.message
def onMessage(message):
    regex = r"(?:https?:)?discord(?:app.com\/gifts\/|.gift\/)([^\s]{0,24})"
    matches = re.findall(regex, message.getContent())
    if len(matches) > 0:
        for code in matches:
            response = client.useGift(code)
            response['giftUrl'] = "https://discord.gift/{}".format(code)
            print(response)


client.setAutoReconnect(True)


