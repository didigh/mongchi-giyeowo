from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone 
from .models import Diary
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    diary = Diary()
    diary.title = request.POST['title']
    diary.body = request.POST['body']
    diary.date = timezone.datetime.now()
    if request.method == 'POST'and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        diary.image = fs.url(filename)
    diary.save()
    return redirect('/')

def mains(request):
    diary = Diary.objects.all()
    search = 'Search,,'

    if request.method == 'POST':
        search = request.POST.get('search')
        diary = diary.filter(title__contains=search)    

    paginator = Paginator(diary, 4)
    page = request.GET.get('page')
    try: 
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = page.get_page(1)
    except EmptyPage :
        posts = paginator.get_page(paginator.num_pages) 

    return render(request, 'main.html', {'diary':diary, 'posts':posts})

def detail(request, diary_id):
    diary = Diary.objects.get(pk = diary_id)
    diary2 = get_object_or_404(Diary, pk = diary_id)
    return render(request, 'detail.html', {'diary':diary, 'diary2':diary2})


def edit(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    if request.method == 'POST':
        diary.title = request.POST['title']
        diary.body = request.POST['body']
        # myfile = request.FILES['image']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # diary.image = fs.url(filename)
        # 기본사진이 수정할떄 저장되게 하는 방법은?
        diary.date = timezone.datetime.now()
        if request.FILES['image']:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            diary.image = fs.url(filename)
        diary.save()
        return redirect('/')  
    else:
        return render(request, 'edit.html', {'diary':diary})

def delete(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    diary.delete()
    return redirect('/')

def login(request):
    return render(request, 'login.html')

def map(request):
    return render(request, 'map.html')
    











