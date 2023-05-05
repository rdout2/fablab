# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import *

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['email', 'first_name', 'last_name', 'active', 'timestamp']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email', 'first_name', 'last_name']
    list_per_page       = 25
    class Meta:
        model = Contact
admin.site.register(Contact, ContactAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', ]
    list_per_page       = 25
    class Meta:
        model = BlogCategory
admin.site.register(BlogCategory, BlogCategoryAdmin)





class TrainingCategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', ]
    list_per_page       = 25
    class Meta:
        model = TrainingCategory
admin.site.register(TrainingCategory, TrainingCategoryAdmin)

class MachineCategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name',]
    list_per_page       = 25
    class Meta:
        model = MachineCategory
admin.site.register(MachineCategory, MachineCategoryAdmin)

class GaleryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['image', 'active', 'timestamp', 'updated']
    list_display_links  = ['image',]
    list_filter         = ['image']
    search_fields       = ['image',]
    list_per_page       = 25
    class Meta:
        model = Galery
admin.site.register(Galery, GaleryAdmin)

class BlogCommentAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = [ 'email','first_name', 'last_name','message', 'active', 'timestamp']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email',]
    list_per_page       = 25
    class Meta:
        model = BlogComment
admin.site.register(BlogComment, BlogCommentAdmin)




class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name',]
    list_per_page       = 25
    class Meta:
        model = Blog
admin.site.register(Blog, BlogAdmin)


class TrainingAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name',]
    list_per_page       = 25
    class Meta:
        model = Training
admin.site.register(Training, TrainingAdmin)

class MachineAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name',]
    list_per_page       = 25
    class Meta:
        model = Machine
admin.site.register(Machine, MachineAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['email', 'active', 'timestamp', 'updated']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email',]
    list_per_page       = 25
    class Meta:
        model = Newsletter
admin.site.register(Newsletter, NewsletterAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['email','active', 'timestamp', 'updated']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email',]
    list_per_page       = 25
    class Meta:
        model = Testimonial
admin.site.register(Testimonial, TestimonialAdmin)


class AdmissionAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['email', 'first_name','training', 'last_name', 'active', 'timestamp']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email', 'first_name', 'last_name']
    list_per_page       = 25
    class Meta:
        model = Admission
admin.site.register(Admission, AdmissionAdmin)
