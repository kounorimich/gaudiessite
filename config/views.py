from django.shortcuts import render #get_object_or_404
from datetime import datetime

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['now'] = datetime.now().time()
        return context


index = IndexView.as_view()

