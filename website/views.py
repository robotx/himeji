from django.views import generic
from .models import Post
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

from .forms import ContactForm


class AllList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1, category="News").order_by('-created_on')
    template_name = 'news.html'
    paginate_by = 5


class KnowledgeList(generic.ListView):
    queryset = Post.objects.filter(status=1, category="Savoir").order_by('-created_on')
    template_name = 'knowledge.html'
    paginate_by = 5


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
       'form': form_class,
    })

#https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/

