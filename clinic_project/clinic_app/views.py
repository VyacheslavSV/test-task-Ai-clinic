from rest_framework import serializers
from rest_framework import viewsets

from clinic_app.models import Team, Person
from clinic_app.serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def validate_email(self, value):
        if Person.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
