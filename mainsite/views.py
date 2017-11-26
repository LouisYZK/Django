# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 
from .models import Post 
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
	posts = Post.objects.all()
	template = get_template('index.html')
	now = datetime.now()
	html = template.render(locals())
	# post_lists =list()
	# for count,post in enumerate(posts):
	# 	post_lists.append("No.{}".format(str(count))+str(post)+"<hr>")
	# 	post_lists.append("<small>" + str(post.body) + "</small><br><br>")
	return HttpResponse(html)

def showpost(request,slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')