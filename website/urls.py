from django.urls import path
from website.views import Home, BlogDetails, ProjectDetails, OurWorks

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blog/details/<slug:pk>/', BlogDetails.as_view(), name='blog-details'),
    path('project/details/<slug:pk>/', ProjectDetails.as_view(), name='project-details'),
    path('our/works/', OurWorks.as_view(), name='our-works'),
]
