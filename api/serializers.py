from rest_framework.serializers import ModelSerializer

from api.models import Audit

class AuditSerializer(ModelSerializer):
    class Meta:
        model = Audit
        fields = ('id', 'name', 'year_of_release')
        extra_kwargs = {
            'id': {'read_only': True}
        }