# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import UbtVIP
# Create your views here.

def index(request):

    #ubt = UbtVIP.objects.filter(cguid='11111')
    ubt = UbtVIP.objects.get(id=1)
    return render(request, 'blog/index.html', {'ubt': ubt})
