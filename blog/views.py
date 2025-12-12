from django.views import generic
from django.db.models import Count, Prefetch

from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = (
        Post.objects.select_related("owner")
        .annotate(num_comments=Count("commentaries"))
    )


class PostDetailView(generic.DetailView):
   model = Post
   queryset = Post.objects.prefetch_related(
       Prefetch(
           "commentaries",
           queryset=Commentary.objects.select_related("user")
       )
   ).annotate(num_comments=Count("commentaries"))