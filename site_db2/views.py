from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from site_db2.models import Message
from site_db2.serializers import MessageSerializer, MessagePostSerializer
from rest_framework import permissions

# Create your views here.
def base(request):
    return render(request, "base.html")

class ListMessages(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class SingleMessage(APIView):

    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        id = request.GET.get("id")
        single_message = Message.objects.get(pk =id)
        serializer = MessageSerializer(single_message)
        return Response(serializer.data)

    def post(self, request):
        email_message = MessagePostSerializer(data=request.data)
        if email_message.is_valid():
            email_message.save()
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})