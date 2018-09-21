from django.conf.urls import url

from api.views import AuditCreateView, AuditDetailView

urlpatterns = [
    url(r'^audits/$', AuditCreateView.as_view(), name='audits'),
    url(r'^audits/(?P<id>[0-9]+)$', AuditDetailView.as_view(), name='detail'),
]