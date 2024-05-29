from rest_framework import serializers

from collaborator.models import Collaborator


class CollaboratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaborator
        fields = "__all__"
