from google.appengine.ext import ndb


class Member(ndb.Model):
    uid = ndb.StringProperty()
    name = ndb.StringProperty(default='')
    date = ndb.DateTimeProperty(auto_now_add=True)


class Members:
    def get(self, id_):
        pass

    def update(self, id_):
        pass
