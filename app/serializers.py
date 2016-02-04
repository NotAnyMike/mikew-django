from rest_framework import serializers
from app.models import Person

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = ('id', 'name', 'email', 'mobile', 'facebook_username', 'twitter_username', 'medium_username', 'github_username', 'img', 'img2x', 'interests', 'techs')
