from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from django import forms
from django.views import generic
from .utils import get_contents, remove_object, get_items, get_itemlist, get_username, add_object
from .models import User, ItemList, Item

class IndexView(generic.ListView):
    template_name #= loginpage
    context_object_name = Context({})

def page_handler(request):
    if request.method == "POST":
        id = request.POST.get("acc_name", None)
        contents = get_contents(id)

        if "home" in request.POST:
            objects = get_items(get_itemlist(id))
            render(request, ..., objects) #.. nameofmainpage), objects

        elif "make_account" in request.POST:
            render(request,) #make account page, {})

        elif "match" in request.POST:
            if request.POST.get("match", None) != None:
                match = request.POST.get("match", None)
                user = get_contents(id)
                matched = get_contents(match)
                render(request,) #matched page, {'user' : user, 'matched' : matched})

        elif "add" in request.POST:
            a = get_itemlist(id).id
            b = request.POST.get('obj_ty')
            c = request.POST.get('obj_nm')
            d = request.POST.get('obj_des')
            e = request.POST.get('q')
            if not(a and b and c and d):
                add_object(a, b, c, d, e)

        elif "remove" in request.POST:
            remove_object(request.POST.get('item_num'))
            render(request)

        #result = generate_characters(screenname)
        # handle is the name of the input in the question.
        # Here you can do anything with your screenname, like passing it to the function.
        return render(request, '../templates/nursery/story.html', {'result':result})
    return render(request, '../templates/nursery/index.html', {})
# Create your views here.

# Create your views here.
