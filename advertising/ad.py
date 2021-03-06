from advertising.base_advertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, img_url, link, advertiser):
        super(Ad, self).__init__(id)
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    @property
    def advertiser(self):
        return self._advertiser

    @advertiser.setter
    def advertiser(self, value):
        self._advertiser = value

    def inc_clicks(self):
        self._advertiser.inc_clicks()
        self._clicks += 1

    def inc_views(self):
        self._advertiser.inc_views()
        self._views += 1

    def describe_me(self):
        return "Ad with id:" + str(self._id)
