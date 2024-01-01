from django.views.generic import TemplateView, DetailView

from website.models import Project, Blog, Images, WebsiteContent, Services, SocialLinks, Skills


class Home(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        latest_social_links = SocialLinks.objects.order_by('-id').first()

        context['facebook'] = latest_social_links.facebook if latest_social_links else None
        context['twitter'] = latest_social_links.twitter if latest_social_links else None
        context['instagram'] = latest_social_links.instagram if latest_social_links else None
        context['linkedin'] = latest_social_links.linkedin if latest_social_links else None
        context['youtube'] = latest_social_links.youtube if latest_social_links else None
        context['tiktok'] = latest_social_links.tiktok if latest_social_links else None
        context['projects'] = Project.objects.all()
        context['blogs'] = Blog.objects.all()
        context['image'] = Images.objects.order_by('-id').first()
        context['content'] = WebsiteContent.objects.order_by('-id').first()
        context['services'] = Services.objects.all()
        context['skills'] = Skills.objects.all()


        return context


class BlogDetails(DetailView):
    model = Blog
    template_name = 'website/blogs_details.html'


class ProjectDetails(DetailView):
    model = Project
    template_name = 'website/project_details.html'


class OurWorks(TemplateView):
    template_name = 'website/our_work.html'
