from flask import request
from application import application
import json

from errors.error import InvalidUsage
from util.utils import *
from util.crawler import *

@application.route('/crawler_results', methods=['GET', 'POST'])
def getCrawlerResults():
    jsonData = request.get_json()
    url = jsonData["url"]
    depth = jsonData["depth"]
    if url:
        if depth:
            response = {}
            crawler = Crawler()
            response = crawler.getData(url, depth)
            return json.dumps(response, default=date_handler)
        else:
            raise InvalidUsage('Depth is missing.', status_code=400)
    else:
        raise InvalidUsage('Url is missing.', status_code=400)
