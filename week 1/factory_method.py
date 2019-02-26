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


class BaseMessageController(object):
    def send_new_message(self, message_type):
        new_message = self.message_factory(message_type)
        if new_message:
            new_message.send()

    def message_factory(self, message_type):
        raise NotImplementedError()


class MessageController(BaseMessageController):
    def message_factory(self, message_type):
        if message_type is 'p':
            return PooMessage()
        if message_type is 'w':
            return WeeMessage()
        return None


class MessageController2(BaseMessageController):
    def message_factory(self, message_type):
        if message_type is 'ss':
            return PooMessage()
        if message_type is 'w':
            return WeeMessage()
        return None


mc = MessageController()
mc.send_new_message('p')
mc.send_new_message('w')
mc.send_new_message('ss')

mc2 = MessageController2()
mc2.send_new_message('p')
mc2.send_new_message('w')
mc2.send_new_message('ss')
