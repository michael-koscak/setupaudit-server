from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Audit
from api.serializers import AuditSerializer

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

def email(request):
    subject = 'Test Message'
    message = 'test body'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mkoscak23@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )

class AuditCreateView(ListCreateAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    email('test')

class AuditDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    email('test')

