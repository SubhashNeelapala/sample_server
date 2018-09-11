from rest_framework import serializers
from polls.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,User




class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name','mobile_number','email')
			
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=30)

    def validate(self, data):
        if not data['username'] and not data['password']:
            raise serializers.ValidationError("please provide username/password")
        return data


class UserregistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    mobile_number = serializers.IntegerField()
    age = serializers.IntegerField()
    password=serializers.CharField()

    def validate_username(self,value):
        if len(value) < 2:
            raise serializers.ValidationError("Username Required")
        return value
    def validate_first_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("First Name Required")
        return value
    def validate_last_name(self,value):
        if len(value)<1:
            raise serializers.ValidationError("Last Name Required")
        return value
    # def validate_mobile_number(self,value):
    #     # value = value.replace(' ', '')
    #     if len(value) != 10:
    #         raise serializers.ValidationError("Mobile Number Length Must Be 10 Digits")
    #     if not value.isnumeric():
    #         raise serializers.ValidationError("Mobile Number Must Be Digits")
    #     if not str(value).startswith(('6','7','8','9')):
    #         raise serializers.ValidationError("Invalid mobile number")
    #     return value
