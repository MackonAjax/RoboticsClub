from rest_framework import serializers
from .models import Member, Project, BorrowedItem

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class BorrowedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedItem
        fields = ['item_name', 'borrower', 'return_date']