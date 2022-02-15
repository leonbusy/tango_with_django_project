from asyncio.windows_events import NULL
from email.policy import default
from http.client import FOUND
from telnetlib import STATUS
from urllib import response
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category
from rango.models import Page

#def index(request):
    #return HttpResponse(r"<a href='/rango/about/'>About</a>"+'Rango says hey there partner!')
# def index(request):
#     # Construct a dictionary to pass to the template engine as its context.
#     # Note the key boldmessage matches to {{ boldmessage }} in the template!
#     context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
#     # Return a rendered response to send to the client.
#     # We make use of the shortcut function to make our lives easier.
#     # Note that the first parameter is the template we wish to use.
#     return render(request, 'rango/index.html', context=context_dict)
def index(request):
# Query the database for a list of ALL categories currently stored.
# Order the categories by the number of likes in descending order.
# Retrieve the top 5 only -- or all if less than 5.
# Place the list in our context_dict dictionary (with our boldmessage!)
# that will be passed to the template engine.
    #try:
    category_list = Category.objects.order_by('-likes')[0:5]
    page_list=Page.objects.order_by('-views')[0:5]
    
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages']=page_list
    #print(context_dict)
    # except:
    #     pass
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Hanliang.'}
    return render(request,'rango/about.html',context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
        #return render(request, 'rango/category.html', context=context_dict)
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        # context_dict['category'] = None
        # context_dict['pages'] = None
        pass
        #print("error")
    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)

