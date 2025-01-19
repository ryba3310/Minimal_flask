# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from prometheus_client import make_wsgi_app, Counter, Histogram, Summary, generate_latest
import random, time, requests, os

LAMBDA_ENDPOINT = os.environ['LAMBDA_VPCE']
DURATION = Summary('flask_index_response_time', 'Time spent on index response', ['method', 'endpoint', 'http_status'])
REQUESTS = Counter('flask_request_count', 'Number of requests to index', ['method', 'endpoint', 'http_status'])
PROCESSING = Histogram('flask_request_proccessing_time', 'Time spent processing request data', ['method', 'endpoint'])

@DURATION.time()
@blueprint.route('/')
def index():
    start_time = time.time()
    REQUESTS.labels('GET', '/', '200').inc()
    # Some mocking sleep time for proccesing latency generation
    time.sleep(random.uniform(0.1, 1.0))
    PROCESSING.labels('GET', '/').observe(time.time() - start_time)

    return render_template('home/index.html', segment='index')

@blueprint.route('/search', methods=['GET'])
def search():
    if request.query_string:
        query = request.args['query']
        movies = requests.get(f'{LAMBDA_ENDPOINT}?query={query}')
        return render_template('home/search.html', pagination=movies)

    return render_template('home/search.html', )
# @blueprint.route('/metrics')
# def metrics():
#     return generate_latest()

# @blueprint.route('/<template>')
# def route_template(template):

#     try:

#         if not template.endswith('.html'):
#             template += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/" + template, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
