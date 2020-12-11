from .guild import Guild

import requests

class Message(object):
    def __init__(self, token, message):

        self.message = message
        
        headers = {'Authorization': token}

        r = requests.get('https://discord.com/api/v8/guilds/' + self.message['guild_id'], headers=headers)

        self.guild = Guild(r.json())
        

    def getContent(self):
        return self.message.get('content')

    def getGuild(self):
        return self.guild