 
from django.shortcuts import render 
from django.http import Http404 
from django.shortcuts import get_object_or_404
from django.db.models import Q

from datetime import datetime

from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication ,SessionAuthentication,BasicAuthentication
from rest_framework import generics, permissions, viewsets

from django.contrib.auth.models import User,Group

from .models import Item,Category 
from .serializers import ItemSerializer,CategorySerializer,UserSerializer,GroupSerializer
# ,UserSerializer
  

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

from django.contrib.auth import authenticate


class ItemList(APIView):
    def get(self, request, format=None): 
        items = Item.objects.all() 
        serializer = ItemSerializer(items, many=True) 
   
        return Response(serializer.data) 
    

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get filter params from request
        filters = self.request.query_params.get('filters', None)
        # Get order_by criteria from request
        order_by = self.request.query_params.get('order_by', None)

        # Apply filters if provided
        if filters:
            try:
                filters_dict = eval(filters) if filters else {}
            except Exception as e:
                print("Error parsing filter params:", e)
                filters_dict = {}

            if filters_dict:
                query = Q()
                for key, value in filters_dict.items():
                    query &= Q(**{key: value})
                queryset = queryset.filter(query)

        # Apply order_by criteria if provided
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset
    
    def post(self, request, format=None): 
        serializer = ItemSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class ItemDetail(APIView): 
    """ 
    List all Items, or add a new Item 
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            data = get_object_or_404(Item,id=pk)
            serializer = ItemSerializer(data=data.__dict__) 

            if serializer.is_valid(): 
                return Response(status=status.HTTP_200_OK,data=serializer.data )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Item.DoesNotExist: 
            raise Http404 
  
    
    def delete(self, request, pk, format=None): 
        item = get_object_or_404(Item,id=pk)
        item.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def put(self, request, pk, format=None): 
    #     transformer = self.get_object(pk) 
    #     serializer = TransformerSerializer(transformer, data=request.data) 
    #     if serializer.is_valid(): 
    #         serializer.save() 
    #         return Response(serializer.data) 
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
    # def patch(self, request, pk, format=None): 
    #     transformer = self.get_object(pk) 
    #     serializer = TransformerSerializer(transformer, 
    #                                        data=request.data, 
    #                                        partial=True) 
    #     if serializer.is_valid(): 
    #         serializer.save() 
    #         return Response(serializer.data) 
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class CategoryList(APIView):
    def get(self, request, format=None): 
        categorys = Category.objects.all() 
        serializer = CategorySerializer(categorys, many=True) 
        return Response(serializer.data) 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filters = self.request.GET.get('filters', '{}')  # Get filter params from request, defaulting to empty dict
        order_by = self.request.GET.get('order_by', '')  # Get order_by criteria from request, defaulting to empty string
        
        # Convert filter string to dictionary
        try:
            filters_dict = eval(filters) if filters else {}
        except SyntaxError:
            filters_dict = {}
        
        # Apply filters
        if filters_dict:
            query = Q()
            for key, value in filters_dict.items():
                query &= Q(**{key: value})
            queryset = queryset.filter(query)
        
        # Apply order_by criteria
        if order_by:
            queryset = queryset.order_by(order_by)
        
        return queryset
    
    def post(self, request, format=None): 
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CategoryDetail(APIView): 
    """ 
    List all Category, or add a new Category 
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
        
    def get(self, request,pk): 
        # Returns an object instance that should  
        # be used for detail views. 
        try: 
            data = get_object_or_404(Category,id=pk)
            serializer = ItemSerializer(data=data.__dict__) 
            print(data.__dict__)
            if serializer.is_valid(): 
                return Response(status=status.HTTP_200_OK,data=serializer.data )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Category.DoesNotExist: 
            raise Http404 
  
    
    def delete(self, request, pk, format=None): 
        category = get_object_or_404(Category,id=pk)
        category.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class FilterItems(APIView):
    def get(self, request):
        # Extract filter parameters from query parameters
        category_id = request.query_params.get('category_id')
        status = request.query_params.get('status')
        name = request.query_params.get('name')
        tag = request.query_params.get('tag')
        sku = request.query_params.get('sku')
        status =  request.query_params.get('status')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')

        # Build queryset based on filter parameters
        queryset = Item.objects.all()

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if status:
            queryset = queryset.filter(status=status)
        if name:
            queryset = queryset.filter(name=name)
        if tag:
            queryset = queryset.filter(tag=tag)
        if sku:
            queryset = queryset.filter(sku=sku)
        if start_time and end_time:
            start_time = datetime.strptime(start_time, '%Y-%m-%d')
            end_time = datetime.strptime(end_time, '%Y-%m-%d')
            queryset = queryset.filter(created_at__range=[start_time, end_time])


        # Serialize queryset and return response
        serializer = ItemSerializer(queryset, many=True)
        return Response(data=serializer.data)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer