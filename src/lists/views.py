import logging

from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ValidationError

from lists.forms import ItemForm
from lists.models import Item, List
from common.decorators import ajax_required

# Get an instance of a logger
logger = logging.getLogger(__name__)


def home_page(request):
    logger.debug('----Start----')
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, id):
    list_ = List.objects.get(id=id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


@ajax_required
def like(reqiest):
    """Test"""
    return HttpResponse(f"{like.__name__}{like.__doc__}")

