from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Transaction, ObjectifFinancier
from .serializers import TransactionSerializer, ObjectifFinancierSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ObjectifFinancierViewSet(viewsets.ModelViewSet):
    queryset = ObjectifFinancier.objects.all()
    serializer_class = ObjectifFinancierSerializer