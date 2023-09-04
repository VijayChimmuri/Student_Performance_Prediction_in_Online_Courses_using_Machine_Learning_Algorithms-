
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import ClientRegister_Model,review_Model,student_performance_model,recommend_Model,performance_ratio_model,search_ratio_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            performance_ratio_model.objects.all().delete()
            search_ratio_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = student_performance_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=student_performance_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_Student_Performance(request): # Search

   if request.method == "POST":
        kword = request.POST.get('keyword')
        print(kword)
        obj = student_performance_model.objects.all().filter(Q(Enrollment_No__contains=kword) | Q(names__contains=kword))
        obj1 = student_performance_model.objects.get(Q(Enrollment_No__contains=kword) | Q(names__contains=kword))
        Diagnostic_Assessments_Grade = obj1.Diagnostic_Assessments_Grade
        Formative_Assessments_Grade = obj1.Formative_Assessments_Grade
        Interim_Assessments_Grade=obj1.Interim_Assessments_Grade
        Summative_Assessments_Grade=obj1.Summative_Assessments_Grade

        grade = ((Diagnostic_Assessments_Grade+Formative_Assessments_Grade+Interim_Assessments_Grade+Summative_Assessments_Grade)/28)*100

        if grade != 0:
            search_ratio_model.objects.create(names=kword, ratio=grade)
        return render(request, 'SProvider/Search_Student_Performance.html', {'objs': obj,'ratio': grade})
   return render(request, 'SProvider/Search_Student_Performance.html')

def View_All_StudentPerformance_Prediction_Details(request):
    sname = ''
    Eno = ''
    gender = ''
    cname = ''
    dname = ''
    collegename =''
    obj1 = student_performance_model.objects.values('names',
                                                    'Enrollment_No',
                                                    'Gender',
                                                    'Course_Name',
                                                    'Degree_Name',
                                                    'College_Name',
                                                    'Diagnostic_Assessments_Grade',
                                                    'Formative_Assessments_Grade',
                                                    'Interim_Assessments_Grade',
                                                    'Summative_Assessments_Grade'
                                                    )

    performance_ratio_model.objects.all().delete()
    for t in obj1:
        sname = t['names']
        Eno = t['Enrollment_No']
        gender = t['Gender']
        cname = t['Course_Name']
        dname = t['Degree_Name']
        collegename = t['College_Name']
        Diagnostic_Assessments_Grade = t['Diagnostic_Assessments_Grade']
        Formative_Assessments_Grade = t['Formative_Assessments_Grade']
        Interim_Assessments_Grade = t['Interim_Assessments_Grade']
        Summative_Assessments_Grade = t['Summative_Assessments_Grade']
        performance = ((Diagnostic_Assessments_Grade + Formative_Assessments_Grade + Interim_Assessments_Grade + Summative_Assessments_Grade) / 28) * 100
        performance_ratio_model.objects.create(names=sname,ENo=Eno,Gender=gender,Course_Name=cname,Degree_Name=dname,College_Name=collegename,perfromance=performance)

    obj = performance_ratio_model.objects.all()

    return render(request, 'SProvider/View_All_StudentPerformance_Prediction_Details.html', {'objs': object



def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = student_performance_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = student_performance_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = student_performance_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = search_ratio_model.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def charts1(request,chart_type):
    chart1 = performance_ratio_model.objects.values('names').annotate(dcount=Avg('perfromance'))
    return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def View_Student_Performance_Details(request):
    obj =student_performance_model.objects.all()
    return render(request, 'SProvider/View_Student_Performance_Details.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts =performance_ratio_model.objects.values('names').annotate(dcount=Avg('perfromance'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

def View_Students_Assessments_Grades(request):
    obj = student_performance_model.objects.all()
    return render(request, 'SProvider/View_Students_Assessments_Grades.html', {'list_objects': obj})

def View_Search_Ratio(request):
    obj = search_ratio_model.objects.all()
    return render(request, 'SProvider/View_Search_Ratio.html', {'list_objects': obj})







