from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'core/index.html'

	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)