class IStateContext(object):
    current_state = None
    action_chain = []

    def setState(self, new_state):
        self.current_state = new_state


class IState(object):
    def action(self):
        raise NotImplementedError()

    def next(self, state_object):
        raise NotImplementedError()

    def prior(self, state_object):
        raise NotImplementedError()

    def stop(self, state_object):
        state_object.setState(state_object.idle)

    def reset(self, state_object):
        state_object.setState(state_object.reset)


class Up(IState):
    def action(self):
        print("up")

    def next(self, state_object):
        state_object.setState(state_object.down)

    def prior(self, state_object):
        state_object.setState(state_object.reset)


class Down(IState):
    def action(self):
        print("down")

    def next(self, state_object):
        state_object.setState(state_object.reset)

    def prior(self, state_object):
        state_object.setState(state_object.up)


class Reset(IState):
    def action(self):
        print("reset")

    def next(self, state_object):
        state_object.setState(state_object.idle)

    def prior(self, state_object):
        state_object.setState(state_object.down)


class Idle(IState):
    def action(self):
        print("idle")

    def next(self, state_object):
        state_object.setState(state_object.up)

    def prior(self, state_object):
        pass


class RoboChair(IStateContext):
    def __init__(self):
        self.idle = Idle()
        self.current_state = self.idle
        self.up = Up()
        self.reset = Reset()
        self.down = Down()

    def undo(self):
        self.action_chain.pop(-1)

    def next(self):
        self.current_state.next(self)
        self.current_state.action()

    def prior(self):
        self.current_state.prior(self)
        self.current_state.action()

    def stop(self):
        self.current_state.stop(self)
        self.current_state.action()

    def reset1(self):
        self.current_state.reset(self)
        self.current_state.action()


rob = RoboChair()
rob.next()
rob.next()
rob.next()
rob.next()
rob.prior()
rob.stop()
rob.reset1()

