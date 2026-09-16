from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name is required.")
        return value

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be greater than 0.")
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be 10 digits."
            )

        return value

    def validate_gender(self, value):
        if not value.strip():
            raise serializers.ValidationError("Gender is required.")
        return value

    def validate_disease(self, value):
        if not value.strip():
            raise serializers.ValidationError("Disease is required.")
        return value

    def validate_doctor_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Doctor name is required.")
        return value