from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import (
    RegisterForm,
    AppointmentForm,
    ReviewForm,
    MasterMessageForm
)
from .models import (
    Service,
    Master,
    MasterWork,
    MasterMessage,
    Appointment,
    Review
)

# ГЛАВНАЯ
@login_required
def home(request):

    services = Service.objects.all()

    masters = Master.objects.all()

    reviews = Review.objects.all().order_by('-id')[:6]

    return render(request, 'beauty/home.html', {
        'services': services,
        'masters': masters,
        'reviews': reviews
    })


# РЕГИСТРАЦИЯ
def register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    else:

        form = RegisterForm()

    return render(request, 'beauty/register.html', {
        'form': form
    })

# ЗАПИСЬ
@login_required
def create_appointment(request):

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.save(commit=False)

            appointment.client = request.user

            appointment.save()

            return redirect('/')

    else:

        form = AppointmentForm()

    return render(request, 'beauty/appointment.html', {
        'form': form
    })


# ПРОФИЛЬ
@login_required
def profile(request):

    appointments = Appointment.objects.filter(
        client=request.user
    ).order_by('-date')

    now = timezone.now().date()

    finished_appointments = appointments.filter(
        date__lt=now
    )

    return render(request, 'beauty/profile.html', {
        'appointments': appointments,
        'finished_appointments': finished_appointments
    })


# ОТЗЫВЫ
@login_required
def reviews(request):

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.client = request.user

            review.save()

            return redirect('/reviews/')

    else:

        form = ReviewForm()

    all_reviews = Review.objects.all()

    return render(request, 'beauty/reviews.html', {
        'form': form,
        'reviews': all_reviews
    })


# УСЛУГА
@login_required
def service_detail(request, id):

    service = Service.objects.get(id=id)

    return render(request, 'beauty/service_detail.html', {
        'service': service
    })


# МАСТЕР
@login_required
def master_detail(request, id):

    master = Master.objects.get(id=id)

    works = MasterWork.objects.filter(master=master)

    messages = MasterMessage.objects.filter(master=master).order_by('-created_at')

    # КТО МАСТЕР (Оксана)
    is_master = (request.user.email == "oks@gmail.com")

    if request.method == 'POST':

        form = MasterMessageForm(request.POST)

        if form.is_valid():

            msg = form.save(commit=False)

            msg.client = request.user
            msg.master = master

            msg.save()

            return redirect(f'/master/{master.id}/')

    else:

        form = MasterMessageForm()

    return render(request, 'beauty/master_detail.html', {
        'master': master,
        'works': works,
        'messages': messages,
        'form': form,
        'is_master': is_master
    })
    
@login_required
def master_reply(request, message_id):

    message = MasterMessage.objects.get(id=message_id)

    if request.method == 'POST':

        text = request.POST.get('reply')

        MasterMessage.objects.create(

            master=message.master,

            client=message.client,

            message=text,

            is_from_master=True

        )

    return redirect(f'/master/{message.master.id}/')