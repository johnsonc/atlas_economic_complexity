# -*- coding: utf-8 -*-
# Django
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
# General
import json
# Project specific
from atlas.languages import supported_langs
# App specific
from observatory.models import *

def home(request):
	try:
		ip = request.META["HTTP_X_FORWARDED_FOR"]
	except KeyError:
		ip = request.META["REMOTE_ADDR"]
	return render_to_response("home.html", {"client_ip": ip, "supported_langs": supported_langs})