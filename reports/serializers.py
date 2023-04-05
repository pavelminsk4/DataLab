from .models import RegularReport
from drf_writable_nested.serializers import WritableNestedModelSerializer
from api.serializers import UserSerializer

class RegularReportSerializer(WritableNestedModelSerializer):
  user = UserSerializer(many=True, required=False)
  creator = UserSerializer(required=False)
  class Meta:
    model = RegularReport
    fields = '__all__'
