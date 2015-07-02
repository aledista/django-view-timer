import random
import time

from django.http import HttpResponse
from django.views.generic import View


def index(request):
    return HttpResponse('index')


def fun_base_test_view(request):
    i = 0
    for _ in xrange(10000000):
        i += 1
    return HttpResponse('fun_base')


class ClassBaseTestView(View):
    def get(self, request, *args, **kwargs):
        msecs = random.randint(10, 1000)
        time.sleep(msecs / float(1000))
        return HttpResponse('class_base')
