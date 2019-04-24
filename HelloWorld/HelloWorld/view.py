from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from TestModel.models import Test,weathers,phones
from TestModel.models import shubao
from django.core.paginator import Paginator

 
def abm(request):
    return render(request,'about me.html')



def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def movie(request):
    contents = Test.objects.all() 
    p = Paginator(contents,10)   
    if p.num_pages <= 1:  
        content_list = contents  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False 
        right_has_more = False  
        first = False   
       
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
            
                right_has_more = True
            if right[-1] < total_pages:  
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    return render(request,'test.html',context={
        'content_list':content_list,'data':data
    })


def weathers1(request):
    contents = weathers.objects.all() 
    p = Paginator(contents,10)   
    if p.num_pages <= 1:  
        content_list = contents  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    return render(request,'weathers.html',context={
        'content_list':content_list,'data':data
    })

def index(request):
    return render(request,'index.html')


def jd1(request):
    contents = phones.objects.all() 
    p = Paginator(contents,10)   
    if p.num_pages <= 1:  
        content_list = contents  
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    return render(request,'jd-1.html',context={
        'content_list':content_list,'data':data
    })


def showShuBao(request):
    shubao_list=shubao.objects.all()
    p = Paginator(shubao_list,10)   
    if p.num_pages <= 1:  
        content_list = shubao_list 
        data = ''  
    else:
        page = int(request.GET.get('page',1))  
        content_list = p.page(page) 
        left = []  
        right = []  
        left_has_more = False  
        right_has_more = False  
        first = False   
        last = False  
        total_pages = p.num_pages  
        page_range = p.page_range  
        if page == 1:  
            right = page_range[page:page+2]  
            print(total_pages)
            if right[-1] < total_pages - 1:    
                right_has_more = True
            if right[-1] < total_pages:   
                last = True
        elif page == total_pages:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]  
            if left[0] > 2:
                left_has_more = True  
            if left[0] > 1: 
                first = True
        else:  
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]   
            right = page_range[page:page+2] 
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {    
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
            'total_pages':total_pages,
            'page':page
        }
    return render(request,'shubao.html',context={
        'content_list':content_list,'data':data
    })






