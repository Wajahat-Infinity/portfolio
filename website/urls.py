from django.urls import path
from website.views import Home, BlogDetails, ProjectDetails, OurWorks

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blog/details/', BlogDetails.as_view(), name='blog-details'),
    path('project/details/', ProjectDetails.as_view(), name='project-details'),
    path('our/works/', OurWorks.as_view(), name='our-works'),
]
