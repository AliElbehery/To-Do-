from .models import Mission
from .serializer import MissionSerializer
from rest_framework import generics



class MissionList(generics.ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionCreate(generics.CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class MissionRetrieve(generics.RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'pk'

class MissionUpdate(generics.UpdateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'pk'

class MissionDestroy(generics.DestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    lookup_field = 'pk'

