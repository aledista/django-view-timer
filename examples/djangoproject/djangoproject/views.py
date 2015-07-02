from django.http import HttpResponse
from django.views.generic import View


def fun_base_test_view(request):
    i = 0
    for _ in xrange(10000000):
        i += 1
    return HttpResponse('fun_base')


class ClassBaseTestView(View):
    def get(self, request, *args, **kwargs):
        i = 0
        for _ in xrange(10000000):
            i += 1
        return HttpResponse('class_base')
