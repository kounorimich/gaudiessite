# from django.shortcuts import render #get_object_or_404
# from datetime import datetime

from posts.models import Post

from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = 'top/index.html'

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        #context['fixed_post'] = Post.objects.get(pk=6)  # topに固定して表示するpost
        #固定ポストと最新ポストが異なる場合のみトップに表示
        #if not Post.objects.order_by('-published')[0].id == context['fixed_post'].id:
        context['last_post'] = Post.objects.order_by('-published')[0]
        return context


top = TopView.as_view()
