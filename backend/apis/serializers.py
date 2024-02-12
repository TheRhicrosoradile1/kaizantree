from rest_framework.serializers import ModelSerializer,CharField,PrimaryKeyRelatedField,HyperlinkedModelSerializer,HyperlinkedIdentityField
from django.contrib.auth.models import User,Group
from .models import Item,Category
# ,CustomUser


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(HyperlinkedModelSerializer):
    # url = HyperlinkedIdentityField(view_name="groups")
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']


class GroupSerializer(HyperlinkedModelSerializer):
    # url = HyperlinkedIdentityField(view_name="groups")
    class Meta:
        model = Group
        fields = ['id','url', 'name']