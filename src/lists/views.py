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
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    try:
        item = Item(text=request.POST['text'], list=list_)
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)


@ajax_required
def like(reqiest):
    return HttpResponse('TEST')