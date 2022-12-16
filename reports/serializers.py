from .models import RegularReport
from drf_writable_nested.serializers import WritableNestedModelSerializer

class RegularReportSerializer(WritableNestedModelSerializer):
  class Meta:
    model = RegularReport
    fields = '__all__'
