from urllib import request
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        req = request.Request(url)

        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")

        response = request.urlopen(req)
        if response.getcode()!=200:
            return None
        return response.read().decode("utf-8")