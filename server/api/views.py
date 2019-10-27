"""SERIALIZER & JSON IMPORTS"""
from rest_framework import generics
from . import models
from . import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .models import Block, Transaction, Input, Output
from .serializers import BlockSerializer, TransactionSerializer, InputSerializer, OutputSerializer

"""DEFAULT VIEWS"""


def home(request):
    return render(request, 'api/home.html')


"""BLOCKS VIEWS"""


class BlocksListView(generics.ListCreateAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer

    model = Block


class BlockDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Block.objects.all()
    serializer_class = serializers.BlockSerializer

    model = Block


"""SERIALIZER BLOCK VIEWS"""


@csrf_exempt
def block_list(request):
    if request.method == 'GET':
        blocks = Block.objects.all()
        serializer = BlockSerializer(blocks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def block_detail(request, pk):
    try:
        block = Block.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlockSerializer(block)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlockSerializer(block, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        block.delete()
        return HttpResponse(status=204)


"""TRANSACTIONS VIEW"""


class TransactionsListView(generics.ListCreateAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    model = Transaction


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    model = Transaction


"""SERIALIZER TRANSACTION VIEWS"""


@csrf_exempt
def transaction_list(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def transaction_detail(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TransactionSerializer(transaction, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        transaction.delete()
        return HttpResponse(status=204)


"""INPUT VIEWS"""


class InputsListView(generics.ListCreateAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Input.objects.all()
    serializer_class = serializers.InputSerializer

    model = Input


class InputDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Input.objects.all()
    serializer_class = serializers.InputSerializer

    model = Input


"""SERIALIZER INPUT VIEWS"""


@csrf_exempt
def input_list(request):
    if request.method == 'GET':
        inputs = Input.objects.all()
        serializer = InputSerializer(inputs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def input_detail(request, pk):
    try:
        input = Input.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InputSerializer(input)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InputSerializer(input, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        input.delete()
        return HttpResponse(status=204)


"""OUTPUT VIEWS"""


class OutputsListView(generics.ListCreateAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Output.objects.all()
    serializer_class = serializers.OutputSerializer

    model = Output


class OutputDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
     A view that returns the count of active users in JSON.
    """
    queryset = models.Output.objects.all()
    serializer_class = serializers.OutputSerializer

    model = Output


"""SERIALIZER OUTPUT VIEWS"""


@csrf_exempt
def output_list(request):
    if request.method == 'GET':
        outputs = Output.objects.all()
        serializer = OutputSerializer(outputs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OutputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def output_detail(request, pk):
    try:
        output = Output.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OutputSerializer(output)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OutputSerializer(output, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        output.delete()
        return HttpResponse(status=204)
