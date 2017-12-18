# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView, TemplateView, ListView, FormView,View
from .models import Post, Tag, Comment, Project
from .forms import CommentForm

# Create your views here.

class PostDetailView(TemplateView):
	model = Post
	template_name = "post_detail.html"


	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['title']='Posts'
		context['tags']=Tag.objects.all().order_by('pk')
		context['form'] = CommentForm()
		context['post']=get_object_or_404(Post,	pk=self.kwargs['pk'])
		context['post_tags']=get_object_or_404(Post,	pk=self.kwargs['pk']).tags.all()
		return context

class HomeView(TemplateView):
	template_name='home.html'
	model=Tag

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['title']='Home'
		context['recent_posts']=Post.objects.all().order_by('date_published').reverse()
		context['all_posts']=Post.objects.all().order_by('pk')
		context['tags']=Tag.objects.all().order_by('pk')
		context['latest_post']=Post.objects.all().last()
		context['post_tags']=Post.objects.all().last().tags.all()
		return context



class TagPostView(ListView):
	template_name='tag_posts.html'
	model=Tag
	

	def get_context_data(self, **kwargs):
		context = super(TagPostView, self).get_context_data(**kwargs)
		context['tags']=Tag.objects.all().order_by('pk')
		context['title']=get_object_or_404(Tag,	pk=self.kwargs['pk'])
		context['tag_posts']=Post.objects.all().filter(tags__in=[self.kwargs['pk']])
		return context

def add_comment(request, pk):
		post = get_object_or_404(Post, pk=pk)
		tag =Tag.objects.all().order_by('pk')

		if request.method == "POST":
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.post = post
				comment.save()
				return redirect('post_detail', pk=post.pk)
		else:
			form = CommentForm()
		return render(request, 'add_comment.html', {'form': form, 'tags':tag})

class AboutView(TemplateView):
	template_name='about.html'
	

	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		context['title']='About'
		context['tags']=Tag.objects.all().order_by('pk')
		return context		

class ProjectView(TemplateView):
	template_name='project.html'
	

	def get_context_data(self, **kwargs):
		context = super(ProjectView, self).get_context_data(**kwargs)
		context['title']='Projects'
		context['tags']=Tag.objects.all().order_by('pk')
		context['projects']=Project.objects.all().order_by('pk')
		return context				




