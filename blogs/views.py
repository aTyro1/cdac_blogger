from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import writer, verified_writer,blogs
from writers.models import writer as writersWriter
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def home(request):
    # b=blogs.objects.filter(id=request.GET.get('id'))
    # b.comments[date.today]={
    #     'comment':request.GET.get('new_comment')
    # }
    print('home')
    path=settings.MEDIA_ROOT
    home=loader.get_template('home.html')
   
    if(request.session['default_mode']=='T'):
        return redirect('/writers')
    name_of_the_writer=request.GET.get('name')
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
    request.session.flush()
    path=settings.MEDIA_ROOT
    img='atmsd.jpg'
    home=loader.get_template('default.html')
    request.session['default_mode']='T'
    total_blogs=blogs.objects.all().values()
    return HttpResponse(home.render({'writer_name_fl':'D','blogs':total_blogs,'writer_name':'Aman','img_path':path,'img':img}))
def loadArticles(request):
    if(request.session['default_mode']=='T'):
        writer_name='Guest'
    else:
        writer_name=request.session['writer']
    print('load articles')
    article=loader.get_template('articles.html')
    a=blogs.objects.filter(id=request.GET.get('id'))
    print(a[0].id)
    comments=a[0].comments
    writer=a[0].writer_name
    # for i in list_of_similar_topics:
    #     print(unstem(str(i)))
    return HttpResponse(article.render({'writer_name':writer_name,'date':a[0].date,'title':a[0].title,'blog':a[0].blog,'comments':comments,'blog_id':a[0].id,'writer':writer,'image':a[0].images}))

def submissions(request):
    type=request.GET.get('type')
    if(type=='Feeds'):
        print(type)
        if(request.session['default_mode']=='T'):
            name_of_the_writer='Guest'
            home=loader.get_template('default.html')
            request.session['default_mode']='T'
            total_blogs=blogs.objects.all().values()
            return HttpResponse(home.render({'writer_name_fl':'D','blogs':total_blogs,'writer_name':'Aman'}))      
        else:
            name_of_the_writer=request.session['writer']
        w_id=request.session['id']
        if(len(verified_writer.objects.filter(writer_name=name_of_the_writer,writer_id=w_id))):
            home=loader.get_template('home.html')
            total_blogs=blogs.objects.all().values()
            return HttpResponse(home.render({'writer_name_fl':name_of_the_writer[0].upper(),'blogs':total_blogs,'writer_name':name_of_the_writer}))

    elif(request.session['default_mode']=='T'):
         return redirect('/writers/messagedLogin?message='+'you need to login first')
    else:
        submissions_html=loader.get_template('submissions.html')
        b=blogs.objects.filter(writer_id=request.session['id'])
        writer_name=verified_writer.objects.filter(writer_id=request.session['id'])[0].writer_name
        return HttpResponse(submissions_html.render({'f_l':request.session['writer'][0].upper(),'blogs':b,'writer_name':writer_name}))

def new(request):
    if(request.session['default_mode']=='T'):
        return redirect('/writers')
    print('here_new')
    new_submissions_html=loader.get_template('new_submissions.html')
    writer_name=request.session['writer']
    return HttpResponse(new_submissions_html.render({'message':'','f_l':request.session['writer'][0].upper(),'writer_name':writer_name}))

@csrf_protect
@csrf_exempt
def submit_article(request):
    if request.FILES['uploaded']:
        upload = request.FILES['uploaded']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
    blog_content=request.POST['blog']
    blog_title=request.POST['title']
    b=blogs(images=file_url,title=blog_title,writer_id=request.session['id'],blog=blog_content,writer_name=verified_writer.objects.filter(writer_id=request.session['id'])[0].writer_name)
    b.save()
    new_submissions_html=loader.get_template('new_submissions.html')
    return HttpResponse(new_submissions_html.render({'message':'submitted successfully!','f_l':request.session['writer'][0].upper()}))

@csrf_protect
@csrf_exempt
def loadComments(request):
    print(request.session['default_mode'])
    if(request.session['default_mode']=='T'):
        return redirect('/writers/default')
    article=loader.get_template('articles.html')
    b=blogs.objects.get(id=request.POST['blog_id'])
    t_d=str(date.today())
    if(b.comments==''):
        b.comments={request.POST['new_comment']:
            {
        'date':str(date.today()),
        'comment':request.POST['new_comment'],
        'commentor':request.session['writer']
        }}
    else:
        b.comments[request.POST['new_comment']]={
            'date':str(date.today()),
            'comment':request.POST['new_comment'],
            'commentor':request.session['writer']
        }
    b.save()
    comments=b.comments
    for i in comments:
        print(i)
    return HttpResponse(article.render({'writer_name':request.session['writer'],'writer_name_fl':request.session['writer'][0].upper(),'date':b.date,'title':b.title,'blog':b.blog,'comments':comments,'blog_id':b.id,'image':b.images}))

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

@csrf_protect
@csrf_exempt   
def changePassword(request):
    # w=writersWriter.objects.get(writer_id=request.session['id']).values()[0]
    # if(w['password']==request.POST['current_password']):
    #     if(request.POST['new_password1']==request.POST['new_password2']):
    #         w['password']=request.POST['new_password1']
    #         w.update()
    #     else:
    #         print('new unequlas')
    # else:
    #     print('password didnt match')
    # return HttpResponse('changing password')
    print(request.session['id'])
    message=''
    try:
        w=writersWriter.objects.get(writer_id=request.session['id'],password=request.POST['current_password'])
        if(request.POST['new_password1']==request.POST['new_password2']):
            w.password=request.POST['new_password1']
            w.save()
            message='PASSWORD CHANGED RE-ENTER'
        else:
            print('non equal password!')
    except:
            print('invalid')
    return redirect('/writers/messagedLogin?message='+message)

@csrf_protect
@csrf_exempt
def delete(request):
    try:
        w=writersWriter.objects.filter(writer_id=request.session['id'],password=request.POST['password'])
        w.delete()
    except:
        print('invalid!')

    return default(request)


@csrf_protect
@csrf_exempt
def upload(request):
    fss = FileSystemStorage()
    file = fss.save(request.POST['file_name'], request.POST['file'])
    return HttpResponse('uploaded!')
