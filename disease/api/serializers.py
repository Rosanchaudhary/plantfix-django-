from rest_framework import serializers

from disease.models import Disease



class DiseasesSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Disease
        fields = "__all__"