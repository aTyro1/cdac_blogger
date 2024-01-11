from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import writer, verified_writer,blogs
from writers.models import writer as writersWriter
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from datetime import date

def home(request):
    # b=blogs.objects.filter(id=request.GET.get('id'))
    # b.comments[date.today]={
    #     'comment':request.GET.get('new_comment')
    # }
    print('home')
    home=loader.get_template('home.html')
    name_of_the_writer=request.GET.get('name')
    print(request.session['default_mode'])
    request.session['default_mode']='F'
    print(request.session['default_mode'])
    id=request.GET.get('id')
    
    if(len(verified_writer.objects.filter(writer_name=name_of_the_writer,writer_id=id))):
        request.session['id']=id
        request.session['writer']=name_of_the_writer
        total_blogs=blogs.objects.all().values()
        request.session['default_mode']='F'
        return HttpResponse(home.render({'writer_name_fl':name_of_the_writer[0].upper(),'blogs':total_blogs,'writer_name':name_of_the_writer}))
    else:
        return HttpResponse('writer is not registered with us!')
def default(request):
    home=loader.get_template('default.html')
    request.session['default_mode']='T'
    total_blogs=blogs.objects.all().values()
    return HttpResponse(home.render({'writer_name_fl':'D','blogs':total_blogs,'writer_name':'Aman'}))
def loadArticles(request):
  
    print('load articles')
    article=loader.get_template('articles.html')
    a=blogs.objects.filter(id=request.GET.get('id'))
    comments=a[0].comments
    return HttpResponse(article.render({'writer_name':request.session['writer'],'writer_name_fl':request.session['writer'][0].upper(),'date':a[0].date,'title':a[0].title,'blog':a[0].blog,'comments':comments,'blog_id':a[0].id}))

def submissions(request):
    type=request.GET.get('type')
    if(type=='Feeds'):
        print(type)
        name_of_the_writer=request.session['writer']
        w_id=request.session['id']
        if(len(verified_writer.objects.filter(writer_name=name_of_the_writer,writer_id=w_id))):
            home=loader.get_template('home.html')
            total_blogs=blogs.objects.all().values()
            return HttpResponse(home.render({'writer_name_fl':name_of_the_writer[0].upper(),'blogs':total_blogs,'writer_name':name_of_the_writer}))

    elif(request.session['default_mode']=='T'):
        return redirect('/writers')
    else:
        submissions_html=loader.get_template('submissions.html')
        b=blogs.objects.filter(writer_id=request.session['id'])
        return HttpResponse(submissions_html.render({'f_l':request.session['writer'][0].upper(),'blogs':b}))

def new(request):
    if(request.session['default_mode']=='T'):
        return redirect('/writers')
    print('here_new')
    new_submissions_html=loader.get_template('new_submissions.html')
    return HttpResponse(new_submissions_html.render({'message':'','f_l':request.session['writer'][0].upper()}))

@csrf_protect
@csrf_exempt
def submit_article(request):
    print('here')
    file_path='static/blogs/'+request.POST['blog_path']
    file=open(file_path,'r')
    blog_content=file.read()
    blog_title=request.POST['title']
    b=blogs(title=blog_title,writer_id=request.session['id'],blog=blog_content)
    b.save()
    new_submissions_html=loader.get_template('new_submissions.html')
    return HttpResponse(new_submissions_html.render({'message':'submitted successfully!','f_l':request.session['writer'][0].upper()}))

def loadComments(request):
    if(request.session['default_mode']=='T'):
        return redirect('/writers')
    article=loader.get_template('articles.html')
    b=blogs.objects.filter(id=request.GET.get('id'))[0]
    t_d=str(date.today())
    b.comments[request.GET.get('new_comment')]={
        'date':str(date.today()),
        'comment':request.GET.get('new_comment'),
        'commentor':request.session['writer']
    }
    b.save()
    comments=b.comments
    for i in comments:
        print(i)
    return HttpResponse(article.render({'writer_name':request.session['writer'],'writer_name_fl':request.session['writer'][0].upper(),'date':b.date,'title':b.title,'blog':b.blog,'comments':comments,'blog_id':b.id}))

def account(request):
    if(request.session['default_mode']=='T'):
        return redirect('/writers')
    writer_name=request.session['writer']
    wid=request.session['id']
    account=loader.get_template('account.html')
    try:
        w=writersWriter.objects.filter(writer_id=wid).values()[0]
    except:
        print('passed')
    return HttpResponse(account.render({'writer':writer_name,'writer_id':wid,'email':w['email']}))
    
