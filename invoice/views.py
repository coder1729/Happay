from invoice.models import Invoice,Transaction
from rest_framework import viewsets
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer
from django.shortcuts import render_to_response

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Invoice.objects.all().order_by('date')
    serializer_class = InvoiceSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


