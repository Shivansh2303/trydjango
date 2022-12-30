from django.http import HttpResponse
import random
from article.models import Article
from django.shortcuts import render
from django.template.loader import render_to_string,get_template

random_id = random.randint(1, 2)
article_obj = Article.objects.get(id=random_id)
article_queryset=Article.objects.all() # this is a query set
# my_list=article_queryset  #[132,32,145,21,1]
# my_list_str=""
# for i in my_list:
#     my_list_str += f"<li>number is {i}\n</li>"

context = {
    "object_list":article_queryset,
    # "my_list_str":my_list_str,
    "object": article_obj,
    "title" : article_obj.title,
    "id" : article_obj.id,
    "content" : article_obj.content
}
# django template
tmpl=get_template("home.html")
tmpl_string=tmpl.render(context=context)
# tmpl_string2=tmpl.render(context=context2)
# tmpl_string3=tmpl.render(context=context3)
HTML_STR=render_to_string("home.html",context=context)
# HTML_STR=render_to_string("home.html",context=context)
# HTML_STR=render_to_string("home.html",context=context)
# HTML_STR = """
# <h2> Hi title-{title}-id-{id}!</h2>""".format(**context)



def home(request, *args, **kwargs):
    # print(request.user)
    """
    take in a request 
    return html as as response
    """
    # return HttpResponse(HTML_STR)
    return render(request,'home.html',context=context)