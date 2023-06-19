from rest_framework import serializers


class RegistrationsSerializer(serializers.Serializer):
    state = serializers.CharField(max_length=50)
    district = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100)
    pan = serializers.CharField(max_length=50)
    tan = serializers.CharField(max_length=50)
    name_of_md = serializers.CharField(max_length=50)
    designation = serializers.CharField(max_length=50)
    mobile_no = serializers.IntegerField()
    email_id = serializers.EmailField()
    service_tax_no = serializers.IntegerField()
    password = serializers.CharField(max_length=50)


class RegistrationsRetrieveSerializer(serializers.Serializer):
    state = serializers.CharField(max_length=50)
    district = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100)

