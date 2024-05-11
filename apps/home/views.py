# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.http import JsonResponse
from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect
from .models import Monitor, AirQuality, Device, Feedback
from .serialnumber import serialnumbers

@login_required(login_url="/login/")
def index(request):
    monitor_id = 2  # Replace 1 with the actual ID you want to find
    try:
        airquality = AirQuality.objects.all()
        monitor = Monitor.objects.get(id=monitor_id)
        airquality = AirQuality.objects.filter(monitor=monitor)
    except Monitor.DoesNotExist:
        monitor = None
        airquality = None
    return render(request,'home/index.html',{'monitor':monitor,'airquality':airquality})


""" @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request)) """
@login_required(login_url="/login/")
def showaddmonitor(request):
    
    return render(request,'home/add_monitor.html')
@login_required(login_url="/login/")
def history(request):
    monitor_id = 3  # Replace 1 with the actual ID you want to find
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        airquality = AirQuality.objects.filter(monitor=monitor)
    except Monitor.DoesNotExist:
        monitor = None
        airquality = None
    return render(request,'home/histories.html',{'monitor':monitor,'airquality':airquality})
@login_required(login_url="/login/")
def monitor(request):
    
    monitor=Monitor.objects.all()
    return render(request,'home/monitors.html',{'monitor':monitor})


""" @login_required(login_url="/login/")
def show_air_quality(request):
                monitor_name = request.GET.get('monitor_name')
                monitors = Monitor.objects.filter(name__icontains=monitor_name)
                
                for monitor in monitors:
                    latest_air_quality = monitor.airquality_set.order_by('-datetime').first()
                    monitor.latest_air_quality = latest_air_quality
                
                return render(request, 'home/index.html', {'monitors': monitors}) """
@login_required(login_url="/login/")
def addmonitor(request):
    msg = None
    x=request.POST['monitor_name']
    y=request.POST['serial_number']
    z=request.user
    if any(serialnumber['serialnumber'] == y for serialnumber in serialnumbers):
            monitor = Monitor.objects.create(user=z, name=x, serial_number=y)
            monitor.save()
            return redirect("/")
    else:
        msg = 'Monitor Not Exist'
        return render(request, 'home/add_monitor.html',{'msg':msg})  # You can create a template for this

@login_required(login_url="/login/")
def deleteairquality(request,id):
    aqi=AirQuality.objects.get(id=id)
    aqi.delete()
    return redirect("/history")

@login_required(login_url="/login/")
def deletemonitor(request,id):
    monitor=Monitor.objects.get(id=id)
    monitor.delete()
    return redirect("/monitors")

@login_required(login_url="/login/")
def showeditmonitor(request,id):
    monitor=Monitor.objects.get(id=id)
    return render(request,'home/edit_monitor.html',{'monitor':monitor})

@login_required(login_url="/login/")
def editmonitor(request,id):
    x=request.POST['monitor_name']
    monitor=Monitor.objects.get(id=id)
    monitor.name=x
    monitor.save()
    return redirect("/monitors")

@login_required(login_url="/login/")
def air_quality_chart(request):
    # Aggregate air quality data by day
    air_quality_data = AirQuality.objects.annotate(date=TruncDate('datetime')).values('date').annotate(average_air_quality=Avg('air_quality_aqi'))

    # Prepare data for chart
    dates = [entry['date'].strftime('%Y-%m-%d') for entry in air_quality_data]
    air_quality_values = [entry['average_air_quality'] for entry in air_quality_data]

    context = {
        'dates': dates,
        'air_quality_values': air_quality_values,
    }

    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def deletehistory(request,id):
    aqi=AirQuality.objects.get(id=id)
    aqi.delete()
    return redirect("/histories")
@login_required(login_url="/login/")
def showfeedback(request):
    
    return render(request,'home/feedback.html')
@login_required(login_url="/login/")
def device(request):
    device=Device.objects.all()
    return render(request,'home/device.html',{'device':device})
@login_required(login_url="/login/")
def showeditdevice(request,id):
    device=Device.objects.get(id=id)
    return render(request,'home/edit_device.html',{'device':device})

@login_required(login_url="/login/")
def editdevice(request,id):
    x=request.POST['device_name']
    device=Device.objects.get(id=id)
    device.name=x
    device.save()
    return redirect("/devices")
@login_required(login_url="/login/")
def deletedevice(request,id):
    device=Device.objects.get(id=id)
    device.delete()
    return redirect("/devices")
@login_required(login_url="/login/")
def feedback(request):
    x=request.POST['feedback']
    y=request.user
    feedback=Feedback(feedback=x,user=y)
    feedback.save()
    return redirect("/feedback")