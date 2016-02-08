from rest_framework import serializers
from app.models import Person, Entry, Mantra, Tech

class TechSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tech
		fields = ('name', 'img')

class MantraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mantra
		field = ('author', 'mantra')

class PersonSerializer(serializers.ModelSerializer):
	techs = TechSerializer(many=True, read_only=True)
	mantra = MantraSerializer(many=False, read_only=True)

	class Meta:
		model = Person
		fields = ('id', 'name', 'email', 'mobile', 'facebook_username', 'twitter_username', 'medium_username', 'github_username', 'img', 'img2x', 'interests', 'mantra',  'techs')

class EntrySerializer(serializers.ModelSerializer):
    techs = TechSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = ('id', 'title', 'name_fixed', 'body', 'date', 'techs')
