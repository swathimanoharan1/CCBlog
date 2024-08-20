from django.shortcuts import render
from django.views import generic
from .models import Post, Contact
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            contact = Contact(name=name, email=email, message=message)
            contact.save()

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('success')
        else:
            messages.error(request, 'Please fill in all fields.')


    return render(request, 'base.html')

def success(request):
    return render(request, "success.html")

def aboutus(request):
    return render(request, 'aboutus.html')


def search(request):
    query = request.GET.get('q', '').strip()
    results = Post.objects.filter(title__icontains=query) if query else Post.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})

class HomeView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"

