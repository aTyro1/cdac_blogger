from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import writer, verified_writer,blogs
from django.views.decorators.csrf import csrf_protect,csrf_exempt

def home(request):
    home=loader.get_template('home.html')
    name_of_the_writer=request.GET.get('name')
    id=request.GET.get('id')
    request.session['writer']=name_of_the_writer
    if(len(verified_writer.objects.filter(writer_name=name_of_the_writer,writer_id=id))):
        request.session['id']=id
        total_blogs=blogs.objects.all().values()
        return HttpResponse(home.render({'writer_name_fl':name_of_the_writer[0].upper(),'blogs':total_blogs,'writer_name':name_of_the_writer}))
    else:
        return HttpResponse('writer is not registered with us!')
def loadArticles(request):
    article=loader.get_template('articles.html')
    a=blogs.objects.filter(id=request.GET.get('id'))
    return HttpResponse(article.render({'writer_name':request.session['writer'],'writer_name_fl':request.session['writer'][0].upper(),'date':a[0].date,'title':a[0].title,'blog':a[0].blog}))

def submissions(request):
    submissions_html=loader.get_template('submissions.html')
   
    return HttpResponse(submissions_html.render({}))

def new(request):
    new_submissions_html=loader.get_template('new_submissions.html')
    return HttpResponse(new_submissions_html.render({}))

@csrf_protect
@csrf_exempt
def submit_article(request):
    file_path='static/blogs/'+request.POST['blog_path']
    file=open(file_path,'r')
    blog_content=file.read()
    blog_title=request.POST['title']
    b=blogs(title=blog_title,writer_id=request.session['id'],blog=blog_content)
    b.save()
    return HttpResponse('submitted')

