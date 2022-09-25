from rest_framework.decorators import api_view
import requests
from django.http import HttpResponse
import json


@api_view(['GET', ])
def get_stat_api_view(request):

    # Send request for memory stat to a local web daemon
    response = requests.get(
        'http://localhost:1234/',
    )

    # Get response and return json data
    return HttpResponse(json.dumps(response.json()), content_type='application/json')
