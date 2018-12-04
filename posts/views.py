# akiyokoさんの言う通り、クラスベースでビューを作ってみよう！！
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

class IndexView(TemplateView):

    template_name = 'posts/index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

index = IndexView.as_view()
