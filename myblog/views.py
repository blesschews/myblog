# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView
from .models import Post, Tag

# Create your views here.

class PostDetailView(DetailView):
	model = Post
	template_name = "post_detail.html"

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['title']='Posts'
		context['post']=get_object_or_404(Post,	pk=self.kwargs['pk'])
		return context




class HomeView(TemplateView):
	template_name='home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['title']='Home'
		context['recent_posts']=Post.objects.all().order_by('date_published').reverse()
		context['all_posts']=Post.objects.all().order_by('pk')
		context['tags']=Tag.objects.all().order_by('pk')
		context['latest_post']=Post.objects.all().last()
		return context


    	
    	
