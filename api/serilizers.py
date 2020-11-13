from rest_framework import serializers
from authentication.models import User

class create_user_serilizers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100,write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'})

    confirm_password = serializers.CharField(max_length=100,write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Retype- Password'})


    def create(self,validated_data):
        password = validated_data['password']
        confirm_password = validated_data['confirm_password']

        if password != confirm_password:
            raise AssertionError('password dont match ')
        else:
            _user = User.objects.create(
                email= validated_data['email'],
                first_name = validated_data['first_name'],
                last_name= validated_data['last_name']


            )
            _user.set_password(password)
            _user.save()
            return _user

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','confirm_password')

class profile_serilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('first_name','last_name','email')
