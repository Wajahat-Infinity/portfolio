from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'website/home.html'


class BlogDetails(TemplateView):
    template_name = 'website/blogs_details.html'


class ProjectDetails(TemplateView):
    template_name = 'website/project_details.html'


class OurWorks(TemplateView):
    template_name = 'website/our_work.html'



