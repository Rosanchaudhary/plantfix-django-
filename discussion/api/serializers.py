from tokenize import group
from rest_framework import serializers

from discussion.models import DiscussionGroup, Message



class DiscussionGroupSerializer(serializers.ModelSerializer):
   #creater = serializers.StringRelatedField(read_only=True)
    # creater = RegistrationSerializer(read_only=True)


    class Meta:
        model = DiscussionGroup
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    #sender = serializers.StringRelatedField(read_only=True)
    # creater = RegistrationSerializer(read_only=True)


    class Meta:
        model = Message
        exclude = ('group',) 