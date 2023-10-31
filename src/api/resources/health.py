from falcon import HTTP_200

class HealthRoot():
    def on_get(self, req, resp):
        resp.media={'message': "it's alive!"}