from abc import ABC, abstractmethod
from typing import List


class ObserverI:
    def update(self):
        raise NotImplemented()


class ObservableI:
    def attach(self, o: ObserverI):
        raise NotImplemented()

    def detach(self, o: ObserverI):
        raise NotImplemented()

    def notify(self):
        raise NotImplemented()


class YoutubeChannel(ObservableI):

    __channel_subscribers: List[ObserverI] = []
    __last_posted_video: str = ""

    def attach(self, o: ObserverI):
        self.__channel_subscribers.append(o)

    def detach(o: ObserverI):
        pass

    def notify(self):
        for sub in self.__channel_subscribers:
            sub.update()

    def add_new_video(self, title: str):
        self.__last_posted_video = title
        print("New youtube video added to channel")
        self.notify()

    def last_video_title(self) -> str:
        return self.__last_posted_video

class Subscriber(ObserverI):

    def __init__(self, observable: ObservableI):
        self.observable = observable

    def update(self):
        print("New video posted")
        print(f'{self.observable.last_video_title()}')

channel = YoutubeChannel()
s1 = Subscriber(channel)
s2 = Subscriber(channel)

channel.attach(s1)
channel.attach(s2)

channel.add_new_video(title='Video programming')