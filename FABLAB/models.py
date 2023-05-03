
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.
class TrainingCategory(models.Model):
    name = models.CharField(_("Nom"),max_length=255, null=False, blank=False, unique=True)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    slug        = models.SlugField(_("Slug"), max_length=255, null=True, blank=True, editable=False, unique=False)

    def __str__(self):
        return self.name

def create_training_cat_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    ourQuery = TrainingCategory.objects.filter(slug=slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_training_cat_slug(instance, new_slug=new_slug)
    return slug

def presave_training_cat_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_training_cat_slug(instance)
pre_save.connect(presave_training_cat_slug, sender=TrainingCategory)







class Training(models.Model) :
    category = models.ForeignKey(TrainingCategory, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    prix = models.CharField(_("Tarif de Formation"),max_length=255, null=False, blank=False)
    debut_training = models.DateTimeField(null=False, blank=False )
    fin_training   = models.DateTimeField(null=False, blank=False )
    description = models.TextField(null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    slug        = models.SlugField(_("Slug"), max_length=255, null=True, blank=True, editable=False, unique=False)
    image = models.ImageField(upload_to = 'media', null=False, blank=False)
   
    def __str__(self):
        return self.name

def create_training_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    ourQuery = Training.objects.filter(slug=slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_training_slug(instance, new_slug=new_slug)
    return slug

def presave_training_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_training_slug(instance)
pre_save.connect(presave_training_slug, sender=Training)






class BlogCategory (models.Model):
    name =  models.CharField(_("Nom"),max_length=255, null=False, blank=False, unique=True)
    slug        = models.SlugField(_("Slug"), max_length=255, null=True, blank=True, editable=False, unique=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
   
    def __str__(self):
        return self.name

def create_Blog_cat_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    ourQuery = BlogCategory.objects.filter(slug=slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_Blog_cat_slug(instance, new_slug=new_slug)
    return slug

def presave_Blog_cat_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_Blog_cat_slug(instance)
pre_save.connect(presave_Blog_cat_slug, sender=BlogCategory)







class Blog(models.Model) :
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=False, blank=False, related_name="category_blog")
    name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to = 'media', null=True, blank=True)
    slug        = models.SlugField(_("Slug"), max_length=255, null=True, blank=True, editable=False, unique=False)

    def __str__(self):
        return self.name

def create_Blog_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    ourQuery = Blog.objects.filter(slug=slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_Blog_slug(instance, new_slug=new_slug)
    return slug

def presave_Blog_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_Blog_slug(instance)
pre_save.connect(presave_Blog_slug, sender=Blog)   





class BlogComment(models.Model) :
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, related_name="comment_blog")
    first_name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    last_name = models.CharField(_("Prenom"),max_length=255, null=False, blank=False)
    email = models.EmailField(_("Email"),max_length=255, null=False, blank=False)
    message = models.TextField(_("Commentaire"),null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email




class MachineCategory(models.Model):
    name = models.CharField(_("Nom"),max_length=255, null=False, blank=False, unique=True)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    slug        = models.SlugField(_("Slug"), max_length=255, null=True, blank=True, editable=False, unique=False)

    def __str__(self):
        return self.name

def create_machine_cat_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    ourQuery = MachineCategory.objects.filter(slug=slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_machine_cat_slug(instance, new_slug=new_slug)
    return slug

def presave_machine_cat_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_machine_cat_slug(instance)
pre_save.connect(presave_machine_cat_slug, sender=MachineCategory)







class Machine(models.Model):
    category = models.ForeignKey(MachineCategory, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    quantite = models.IntegerField(_("quantite"), null=True, blank=True)
    Prerequis = models.ForeignKey(TrainingCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(_("Description"),null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to = 'media', null=False, blank=False)
    slug        = models.SlugField(_("Slug"), max_length=255, null=True, blank=True, editable=False, unique=False)
    
    def __str__(self):
        return self.name

def create_machine_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    ourQuery = Machine.objects.filter(slug=slug)
    exists = ourQuery.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ourQuery.first().id)
        return create_machine_slug(instance, new_slug=new_slug)
    return slug

def presave_machine_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_machine_slug(instance)
pre_save.connect(presave_machine_slug, sender=Machine)






class Galery(models.Model) :
    image = models.ImageField(upload_to = 'media', null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    def __str__(self):
        return str(self.id)


class Newsletter(models.Model) :
    email = models.EmailField(max_length=255, null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    def __str__(self):
        return (self.email)

class Trustpilot(models.Model) :
    first_name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)
    def __str__(self):
        return (self.email)


class Admission(models.Model) :
    first_name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    last_name = models.CharField(_("Prenom"),max_length=255, null=False, blank=False)
    phone = models.CharField(_("Numero"),max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    training =  models.ForeignKey(Training, on_delete=models.CASCADE, null=False, blank=False)
    cv = models.FileField(upload_to = 'media', null=False, blank=False)
    motivation = models.TextField(null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email




class Contact(models.Model) :
    first_name = models.CharField(_("Nom"),max_length=255, null=False, blank=False)
    last_name = models.CharField(_("Prénom"),max_length=255, null=False, blank=False)
    phone = models.CharField(_("Téléphone"),max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    subject = models.CharField(_("Sujet"),max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    active     = models.BooleanField(_("Active"), default=True)
    timestamp  = models.DateTimeField(_("Created At"), auto_now_add=True, auto_now=False)
    updated    = models.DateTimeField(_("Updated At"), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email