import falcon

class send_json():
    def on_post(self, req, resp):
        raw_body=req.media
        print(raw_body)
        resp.status = falcon.HTTP_200
        resp.body = '{"message": "Hello world!"}'


api = falcon.API()
api.add_route('/send_json', send_json())