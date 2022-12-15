from datetime import datetime

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import *



class NewsList(ListView):
    model = News1
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = News1
    template_name = 'one_news.html'
    context_object_name = 'one_news'