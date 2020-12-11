import discum  
import requests
from .message import Message

class Client:
    def login(self, token):
        self.client = discum.Client(token=token, log=False)
        
        self.token = token
        print("Logging in")

    def ready(self, func):
        def wrapper():
            @self.client.gateway.command
            def gatewayResponse(response):
                if response['t'] == 'READY_SUPPLEMENTAL':
                    self.user = self.client.gateway.SessionSettings.user
                    func()
                    
        wrapper()
        return wrapper

    def message(self, func):
        def wrapper():
            @self.client.gateway.command
            def gatewayResponse(response):
                if response['t'] == 'MESSAGE_CREATE':
                    message = Message(self.getToken(), response['d'])
                    func(message)
        wrapper()
        return wrapper

    def getToken(self):
        return self.token

    def getId(self):
        return self.user.get('id')

    def getUsername(self):
        return self.user.get('username')

    def getDiscriminator(self):
        return self.user.get('discriminator')

    def isAccountVerified(self):
        return self.user.get('verified')

    def getEmail(self):
        return self.user.get('email')

    def __getAvatar(self):
        return self.user.get('avatar')

    def getDisplayAvatarURL(self):
        return "https://cdn.discordapp.com/avatars/{}/{}.png".format(self.getId(), self.__getAvatar())

    def useGift(self, gift):
        headers = {'Authorization': self.getToken()}
        r = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/' + gift + '/redeem', headers=headers)
        return r.json()

    def getGatewayClient(self):
        return self.client


    def setAutoReconnect(self, boolean):

        self.autoReconnect = boolean

        self.__AutoReconnect()

    def __AutoReconnect(self):
        if self.autoReconnect:
            self.client.gateway.run(auto_reconnect=True)
        else:
            self.client.gateway.run(auto_reconnect=False)
