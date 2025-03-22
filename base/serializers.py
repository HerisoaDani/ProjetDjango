from rest_framework import serializers
from .models import Transaction, ObjectifFinancier

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ObjectifFinancierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectifFinancier
        fields = '__all__'
