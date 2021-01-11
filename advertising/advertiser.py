from advertising.base_advertising import BaseAdvertising

total_clicks = 0


class Advertiser(BaseAdvertising):

    def __init__(self, id, name):
        super(Advertiser, self).__init__(id)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def help():
        return "Fields of this class are name, id, clicks ,and views"

    def describe_me(self):
        return "return Advertiser with id:" + self._id

    @staticmethod
    def get_total_clicks():
        return total_clicks

    # TODO
    def inc_clicks(self):
        super().inc_clicks()
        total_clicks += 1
