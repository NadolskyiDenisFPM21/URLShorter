from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import AddURLForm
from .models import  ShortedURL
import secrets


def create_shorted_url():
    return secrets.token_urlsafe(6)


@login_required(login_url='main:login')
def index(request):
    count = int(request.GET.get('count', 10))
    urls = ShortedURL.objects.all().order_by('-id')
    paginator = Paginator(urls, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    add_form = AddURLForm()
    return render(request, 'index.html', {
                                                            'urls': page_obj.object_list,
                                                            'page_obj': page_obj,
                                                            'page_count': paginator.num_pages,
                                                            'add_form': add_form,
    })


def remove_shorted_link(request, id):
    if not id:
        return redirect('main:index')
    ShortedURL.objects.get(id=id).delete()
    return redirect('main:index')


def add_shorted_url(request):
    if request.method == 'POST':
        form = AddURLForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']
            shorted_url = ShortedURL(name=name, url=url, shorted_url=f'{request.build_absolute_uri(location="/")}{create_shorted_url()}')
            shorted_url.save()
            return redirect('main:index')

def redirect_from_shorted_url(request, shorted_url):
    try:
        url = ShortedURL.objects.get(shorted_url=f'{request.build_absolute_uri(location="/")}{shorted_url}')
        url.clicks += 1
        url.save()
        return redirect(url.url)
    except ShortedURL.DoesNotExist:
        return redirect('https://polymerservice.ua/')