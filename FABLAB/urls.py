from django.urls import path

from .views import *


urlpatterns = [
    path('', home_view, name="home"),
    path('contact/', contact_view, name="contact"),
    path('training_detail/<slug:slug>/', admission_view, name="admission"),
    path('blog/', blog_view, name="blog"),
    path('blog/<slug:slug>/', blog_detail_view, name="blog_detail"),
    path('apropos/', apropos_view, name="apropos"),
    path('machine/', machine_view, name="machine"),
    path('macchine/<slug:slug>/', machine_detail_view, name="machine_detail"),
    path('macchine/<slug:slug>/Prerequis', training_detail_view, name="Prerequis"),
    path('training/', training_view, name="training"),
    path('training/<slug:slug>/', training_detail_view, name="training_detail"),
    path('training/<slug:slug>/apply', training_postuler_view, name="training_postuler"),




]