from django.shortcuts import render
from django.template.loader import get_template
import time
import random
# Create your views here.

from django.http import HttpResponse


def index(request):
    __template_page = get_template('pw_index.html')
    __html = __template_page.render()
    return HttpResponse(__html)


def location_practices_page(request):
    __template_page = get_template('location.html')
    __html = __template_page.render()
    return HttpResponse(__html)


def element_practices_page(request):
    __template_page = get_template('webelements.html')
    __html = __template_page.render()
    return HttpResponse(__html)


def frame_practices_page(request):
    __template_page = get_template('frame.html')
    __html = __template_page.render()
    return HttpResponse(__html)

def wait10sec_practices_page(request):
    random_sleep_time = random.randint(0, 10)
    time.sleep(random_sleep_time)
    __template_page = get_template('10seconds.html')
    __html = __template_page.render({"sleep_sec":random_sleep_time})
    return HttpResponse(__html)



