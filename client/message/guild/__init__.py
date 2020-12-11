class Guild(object):
    def __init__(self, guild):
        self.id = guild.get('id')
        self.name = guild.get('name')
        self.icon = guild.get('icon')

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getDisplayImageURL(self):
        return "https://cdn.discordapp.com/icons/{}/{}.png".format(self.id, self.icon)