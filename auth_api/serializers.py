from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework import serializers

UserModel = get_user_model()


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.groups.set([1])
        user.is_active = True
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.groups.set([2])
        user.is_active = True
        user.save()
        return user


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.save()
        return user
