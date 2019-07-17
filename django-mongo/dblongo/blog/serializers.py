from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')

        # def print_data(self):
        #     return self.model

    # def print_data(self):
    #     return serializers.ModelSerializer

    # def save(self):
    #     return self.model.save()
    # class Meta:
    #     model = Post
    #     fields = ('title', 'content', 'autor')
