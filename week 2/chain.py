class EventChainHandler(object):
    def __init__(self):
        self.next_handler = None

    def check_request(self, request):
        raise NotImplementedError()

    def request(self, request):
        if self.check_request(request):
            return True
        if self.next_handler:
            return self.next_handler.request(request)
        else:
            print("request failed")
        return False

    def add_handler(self, handler):
        if self.next_handler:
            self.next_handler.add_handler(handler)
        else:
            self.next_handler = handler


class AEventHandle(EventChainHandler):
    def check_request(self, request):
        return True if request is "A" else False


class BEventHandle(EventChainHandler):
    def check_request(self, request):
        return True if request is "B" else False


class CEventHandle(EventChainHandler):
    def check_request(self, request):
        return True if request is "C" else False


event1 = "A"
event2 = "V"
event3 = "B"

evc = AEventHandle()
evc.add_handler(BEventHandle())
evc.add_handler(CEventHandle())

evc.request(event1)
evc.request(event2)
evc.request(event3)
