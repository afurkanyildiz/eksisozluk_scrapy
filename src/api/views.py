from rest_framework.generics import ListAPIView
from .models import eksisozluk_entries
from .serializers import EksiSozlukEntrySerializer

class EksiSozlukEntryList(ListAPIView):
    queryset = eksisozluk_entries.objects.all()
    serializer_class = EksiSozlukEntrySerializer
    # print(queryset)
    # print(serializer_class)
