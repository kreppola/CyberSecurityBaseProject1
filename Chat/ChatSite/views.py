from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from . import models
from . import additional

# Create your views here.
@login_required
def index(request):
    if request.method == "GET":
        messages = []
        user_rooms = additional.get_user_rooms(request.user)
        for msg in models.message.objects.filter(room_nr=0):
            messages.append(f"{msg.user} [{msg.pub_date.strftime('%H:%M')}]: {msg.content}")
        return render(request, 'ChatBox.html', {'messages': messages, 'room': 0, 'user_rooms': user_rooms})
    return redirect('/')

@login_required
@csrf_exempt
def add_message(request):
    if request.method == 'POST':
        room = request.POST.get('room', 0)
        models.message.objects.create(user=request.user, content=request.POST.get('content', ''), pub_date=datetime.now(), room_nr=room)
        if int(room) == 0:
            return redirect('/?room=' + room)
        else:
            return redirect('/privateRoom/?room=' + room)

@login_required
@csrf_exempt
def add_private_room(request):
    if request.method == "POST":
        models.privateRoom.objects.create(member1=request.user, member2=request.POST.get('member2', ''), pid=additional.get_pid())
    return redirect('/')

@login_required
def search(request):
    user_input = request.GET.get('query', "")
    if search == "":
        return redirect("/")
    room = int(request.GET.get('room', 0))
    user_rooms = additional.get_user_rooms(request.user)
    # Check if the user is member of the room
    if room in user_rooms or int(room) == 0:
        messages = additional.search_messages_query(user_input, room)
        return render(request, 'ChatBox.html', {'messages': messages, 'room': room, 'user_rooms': user_rooms })
    return redirect('/')

@login_required
def private_room(request):
    room_nr = request.GET.get('room', 0)
    room = models.privateRoom.objects.filter(pid=room_nr)[0]
    user_rooms = additional.get_user_rooms(request.user)
    #if not (str(request.user) == str(room.member1) or str(request.user) == str(room.member2)):
    #    return redirect('/')
    messages = []
    for msg in models.message.objects.filter(room_nr=room_nr):
        messages.append(f"{msg.user} [{msg.pub_date.strftime('%H:%M')}]: {msg.content}")
    return render(request, 'ChatBox.html', {'messages': messages, 'room': room_nr, 'user_rooms': user_rooms})
