from django.shortcuts import render


# Create your views here.
from backend.booking.forms import PostForm


def index(request):
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()

        else:
            context = {}
            context['form'] = post
            return render(request, 'booking/index.html', context)
    form = PostForm(initial={'author': request.user})
    context = {
        'form': form
    }


    return render(request, 'booking/index.html', context)
