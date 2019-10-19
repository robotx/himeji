from django.views import generic
from .models import Post2


class Base(generic.ListView):
    queryset = Post2.objects.order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 5
