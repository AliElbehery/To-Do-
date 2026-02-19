from rest_framework import serializers
from .models import Mission

class MissionSerializer(serializers.ModelSerializer):
    genra_name = serializers.StringRelatedField()
    class Meta :
        model = Mission
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(MissionSerializer, self).to_representation(instance)
        rep['GENRA_NAME'] = instance.genra.name
        return rep