from django.core.mail import send_mass_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from article.models import Article
# from trydjango import
from .forms import ArticleForm
from django.template.loader import render_to_string

def mail(request):
    form=contactForm()
    if request.method=='POST':
        form=contactForm(request.POST)

        if form.is_valid():
            print(request.POST)
            title=form.cleaned_data['title']
            email = form.cleaned_data['email']
            content=form.cleaned_data['content']

            html=render_to_string('article/contactform.html',{
                'title':title,
                'email':email,
                'content':content,

            },)
            # print("the form was valid")
            datatuple=(
                ('Subject','Message','from@example.com',['to@example.com']),
                ('Subject2','Message2','fromm@example.com',['too@example.com']),
            )
            send_mass_mail(datatuple)
            # send_mail(
            #     'this is a contact form',
            #     'the message the email testing is successful',
            #     'noreply@mail.com',
            #     ['shivanshkate@gmail.com'],html_message=html
            # )
            return redirect('mail')
        else:
            print("the form is not valid")
            form=contactForm()
    return render(request,"article/create1.html",{'form':form})

def article_search_view(request):
    print(request.POST)
    query_dict=request.GET # this is a dictionary
    # query=query_dict.get('query') # < input type='text' name='query'/>
    try:
        query=query_dict.get("query")
    except:
        query=None
    article_obj=None
    if query is not None:
        article_obj=Article.objects.filter(title__icontains=query)
        print(article_obj.count())
    context={
        "object":article_obj,
    }
    return render(request,"article/search.html",context=context)

'''
Alternate method
if request.user.is_authenticated:
    return redirect("/login/")
else:
    the later create function
'''
# shortcode for loginrequired
@login_required
def article_create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        'form':form
    }
    if form.is_valid():
        article_object=form.save()
        context['form']=ArticleForm()
        # title=form.cleaned_data.get("title")
        # content=form.cleaned_data.get("content")
        # article_object=Article.objects.create(title=title,content=content)
        # context['object']=article_object
        # context['created']=True
    return render(request, "article/create.html", context=context)

# def article_create_view(request):
#     form=ArticleForm()
#     context={
#         'form':form
#     }
#     if request.method=='POST':
#         form=ArticleForm(request.POST)
#         # print(request.POST)
#         context['form']=form
#         if form.is_valid():
#             title=form.cleaned_data.get("title")
#             content=form.cleaned_data.get("content")
#             article_object=Article.objects.create(title=title,content=content)
#             context['object']=article_object
#             context['created']=True
#     return render(request, "article/create.html", context=context)


def article_detail_view(request,id=None):
    article_obj=None 
    if id is not None:
        article_obj=Article.objects.get(id=id)
    
    context={
        'object':article_obj,
    }
    return render(request,"article/detail.html",context=context)

