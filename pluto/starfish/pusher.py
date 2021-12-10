import pusher
from django.conf import settings


class PusherChannel():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class PusherEvent():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Channels():
    STARFISH = PusherChannel('starfish')

class Events():
    START = PusherEvent('start')
    STOP = PusherEvent('stop')
    VOTING = PusherEvent('voting')
    COUNTING = PusherEvent('counting')
    JOIN = PusherEvent('join')
    CREATE = PusherEvent('create')

class Pusher():
    def __init__(self, channel: PusherChannel, event: PusherEvent) -> None:
        self.channel = channel.name
        self.event = event.name

        self.client = pusher.Pusher(**settings.PUSHER)

    def trigger(self, message: str) -> None:
        return self.client.trigger(self.channel, self.event, message)
