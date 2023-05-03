from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages



def home_view(request):
    template = "index.html"
    context = {}
    return render(request, template, context)




def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a ete envoye avec success")
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = ContactForm()
    template = "contact.html"
    context = {'form': form}
    return render(request,template, context)




def admission_view(request, slug=None):
    admission = get_object_or_404(Training, slug=slug)
    categories = TrainingCategory.objects.all()
    trainings = Training.objects.all()
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        if form.is_valid():
           form.save()
           # messages.success(request, "Votre message a ete envoye avec success")
           return redirect(request.META['HTTP_REFERER'])
    else:
        form = AdmissionForm()
    template = "admission.html"
    context = {
        'form': form,
        'admission' : admission,
        'trainings': trainings,
        'categories' : categories,

    }
    return render(request,template, context)





def blog_view(request):
    template = "blog.html"
    blogs = Blog.objects.all()
    categories = BlogCategory.objects.all()
    
    filter = request.GET.get('filter')
    if filter:
        blogs = Blog.objects.filter(category__slug=filter)
    context = {

        'blogs': blogs,
        'categories': categories,
    }
    return render(request, template, context)



def blog_detail_view(request, slug=None):
    blog = get_object_or_404(Blog, slug=slug)
    categories = BlogCategory.objects.all()
    blogs = Blog.objects.all()
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog
            obj.save()
            messages.success(request, "Votre message a ete envoye avec success")
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = BlogCommentForm()
    template = "blog-detail.html"
    context = {
        'blog': blog,
        'form': form,
        'categories': categories,
        'blogs': blogs
    }
    return render(request, template, context)







def apropos_view(request):
    template = "apropos.html"
    context = {}
    return render(request, template, context)






def training_view(request):
    trainings = Training.objects.all()
    categories = TrainingCategory.objects.all()
    template = "formation.html"
    context = {
       'trainings' : trainings,
       'categories' : categories 
    }
    
    return render(request, template, context)


def training_detail_view(request, slug=None):
    training = get_object_or_404(Training, slug=slug)
    categories = TrainingCategory.objects.all()
    trainings = Training.objects.all()
    template = "formation-detail.html"
    context = {
        'training': training,
        'trainings': trainings,
        'categories' : categories,
    }
    return render(request, template, context)








def training_postuler_view(request, slug=None):
    training = get_object_or_404(Training, slug=slug)
   
    if request.method == "POST":
        
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
         
            obj = form.save(commit=False)
            obj.training = training
            obj.save()
            messages.success(request, "Votre message a ete envoye avec success")
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = AdmissionForm()
    template = "Admission.html"
    context = {
        'form':form
    }
    return render(request, template, context)


def machine_view(request):
    template = "machine.html"
    categories = MachineCategory.objects.all()
    machines = Machine.objects.all()
    
    filter = request.GET.get('filter')
    if filter:
        machines = Machine.objects.filter(category__slug=filter)
    context = {

        'machines': machines,
        'categories': categories,
    }
    return render(request, template, context)


def machine_detail_view(request, slug=None):
    machine = get_object_or_404(Machine, slug=slug)
    categories = MachineCategory.objects.all()
    machines = Machine.objects.all()
    template = "machine-detail.html"
    context = {
        'machine': machine,
        'machines': machines,
        'categories' : categories,
    }
    return render(request, template, context)






def blogcomment_view(request):
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Votre message a ete envoye avec success")
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = BlogCommentForm()
    template = "blog-detail.html"
    context = {'form': form}
    return render(request,template, context)



   