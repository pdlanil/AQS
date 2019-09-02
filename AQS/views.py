from django.shortcuts import render, redirect

from contact.models import Contact
from .forms import ParagraphForm
from . import aqgFunction

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def project(request):
    return render(request,'project.html')


def paragraph(request):
    if request.method == 'GET':
        context = {
            'form': ParagraphForm(),
        }
        return render(request, 'paragraph.html', context)
    else:
        paragraph = request.POST.get('paragraph')
        aqg = aqgFunction.AutomaticQuestionGenerator()
        questionList = aqg.aqgParse(paragraph)
        aqg.display(questionList)
        f= open('output.txt','r')
        all_question = []
        line = f.readline()
        while line:
            all_question.append(line)
            line = f.readline()
        f.close()
        return render(request, 'questions.html',{'question':all_question})

def questions(request):
    context= {
        'form': ParagraphForm(),

    }
    return render(request,'questions.html',context)


def contact(request):
    if request.method =='GET' :
        return render(request,'contact.html')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        message= request.POST.get('message')
        c=Contact(full_name=name, email=email,message=message)
        c.save()
        return render(request,'contact.html')