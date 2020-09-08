class Subscriber(object):
    def __index__(self, name):
        self.name = name

    def update(self, message):
        print("{}, {}".format(self.name, message))

class Publisher(object):
    def __init__(self):
        self.subsribers = set()

    def register(self, who):
        self.subsribers.add(who)

    def unregister(self, who):
        self.subsribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subsribers:
            subscriber.update(message)

if __name__ == '__main__':
    pub = Publisher()

    astin = Subscriber("astin")
    james = Subscriber("james")
    jeff = Subscriber("jeff")

    pub.register(astin)
    pub.register(james)
    pub.register(james)

    pub.dispatch("it's lunch time")
    pub.unregister(jeff)
    pub.dispatch('time to go home')