from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from datetime import datetime

def index(request):
    template =loader.get_template('index.html')
    context = {
        'time': timezone.now(),
        'timestr': timezone.now().astimezone().strftime('%Y%m%d%H%M%S'),
    }
    return HttpResponse(template.render(context, request))
