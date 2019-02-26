class IMessage(object):
    def get_message_type(self):
        raise NotImplementedError()

    def send(self):
        print("sent: " + self.get_message_type())


class PooMessage(IMessage):
    def get_message_type(self):
        return 'poo'


class WeeMessage(IMessage):
    def get_message_type(self):
        return 'wee'


class MessageFactory(object):
    def __init__(self):
        self.number_messages = 0

    def create_message(self, message_type):
        if message_type is 'p':
            self.number_messages += 1
            return PooMessage()
        if message_type is 'w':
            self.number_messages += 1
            return WeeMessage()
        return None


class MessageController(object):
    def __init__(self):
        self.m_factory = MessageFactory()

    def send_new_message(self, message_type):
        new_message = self.m_factory.create_message(message_type)
        if new_message:
            new_message.send()
        print("Total messages created: " + str(self.m_factory.number_messages))


mc = MessageController()
mc.send_new_message('p')
mc.send_new_message('w')
mc.send_new_message('ss')
