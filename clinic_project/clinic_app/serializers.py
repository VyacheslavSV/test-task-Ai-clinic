from rest_framework import serializers

from .models import Person, Team


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_email(self, value):
        if Person.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value


class TeamSerializer(serializers.ModelSerializer):
    members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
