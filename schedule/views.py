from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse
from django.template.loader import render_to_string

from schedule.models import Schedule
from schedule.forms import ScheduleForm

def index(request):
    return render(request, 'index.html')

def schedule_list(request):
    context = {}
    schedules = Schedule.objects.filter().order_by('-id')[:7]

    context['schedules'] = schedules
    return render(request, 'schedule_list.html', context)


def save_book_form(request, form, template_name):
    data = dict()

    print(template_name)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            schedules = Schedule.objects.all().order_by('-id')[:7]
            data['html_schedule_list'] = render_to_string('includes/partial_schedule_list.html', {
                'schedules': schedules
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
    else:
        form = ScheduleForm()

    print("Schedule form")
    print(form)

    return save_book_form(request, form, 'includes/partial_schedule_create.html')


def schedule_update(request, pk):
    book = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=book)
    else:
        form = ScheduleForm(instance=book)

    return save_book_form(request, form, 'includes/partial_schedule_update.html')

def schedule_delete(request, pk):
    book = get_object_or_404(Schedule, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        schedules = Schedule.objects.all()
        data['html_schedule_list'] = render_to_string('includes/partial_schedule_list.html', {
            'schedules': schedules
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('includes/partial_schedule_delete.html', context, request=request)

    return JsonResponse(data)