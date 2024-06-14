from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style={'input_type':'password2'},write_only=True)
    class Meta:
        model = User
        fields= "__all__"
        extra_kwargs={
            'password':{'write_only':True},
        }

  
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get(('password2'))
        if password != password2:
            raise serializers.ValidationError("password and password 2  is not similler")
        return attrs
    
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
    
class  UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta :
        model = User
        fields= [ 'email' ,'password']  

class  MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(),
        email=validated_data['email'],
        password=validated_data['password'],
        first_name=validated_data.get('first_name', ''),
        last_name=validated_data.get('last_name')        

        