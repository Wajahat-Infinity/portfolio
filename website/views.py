from django.views.generic import TemplateView, DetailView

from website.models import Project, Blog, Images, WebsiteContent, Services


class Home(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['projects'] = Project.objects.all()
        context['blogs'] = Blog.objects.all()
        context['image'] = Images.objects.get(id=1)
        context['content'] = WebsiteContent.objects.get(id=1)
        context['services'] = Services.objects.all()


        return context


class BlogDetails(DetailView):
    model = Blog
    template_name = 'website/blogs_details.html'


class ProjectDetails(DetailView):
    model = Project
    template_name = 'website/project_details.html'


class OurWorks(TemplateView):
    template_name = 'website/our_work.html'
