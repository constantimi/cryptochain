from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

"""SERIALIZER & JSON IMPORTS"""
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (ListView, CreateView, UpdateView, DetailView, DeleteView)
from rest_framework.parsers import JSONParser

from .models import Block, Transaction
from .serializers import BlockSerializer


"""DEFAULT VIEWS"""


def home(request):

    return render(request, 'blockchain/home.html')


def about(request):
    return render(request, 'blockchain/about.html', {'title': 'About'})


"""BLOCKS VIEWS"""


class BlocksListView(ListView):
    model = Block
    template_name = 'blockchain/block/block-list.html'
    context_object_name = 'blocks'
    ordering = ['-date_posted']
    paginate_by = 5


class UserBlockListView(ListView):
    model = Block
    template_name = 'blockchain/user-blocks.html'
    context_object_name = 'blocks'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Block.objects.filter(author=user).order_by('-date_posted')


class BlockDetailView(DetailView):
    model = Block
    template_name = 'blockchain/block/block-details.html'


class BlockCreateView(LoginRequiredMixin, CreateView):
    model = Block
    template_name = 'blockchain/block/block-form.html'
    fields = [
        'title',
        'hash',
        'previous_block',
        'merkle_root',
        'time',
        'bits',
        'fee',
        'nonce',
        'n_tx',
        'size',
        'block_index',
        'height',
        'received_time'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlockUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Block
    template_name = 'blockchain/block/block-update.html'
    fields = [
        'title',
        'hash',
        'previous_block',
        'merkle_root',
        'time',
        'bits',
        'fee',
        'nonce',
        'n_tx',
        'size',
        'block_index',
        'height',
        'received_time'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        block = self.get_object()
        if self.request.user == block.author:
            return True
        else:
            return False


class BlockDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Block
    template_name = 'blockchain/block/block-confirm-delete.html'
    success_url = '/'

    def test_func(self):
        block = self.get_object()
        if self.request.user == block.author:
            return True
        return False


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


class TransactionsListView(ListView):
    model = Transaction
    template_name = 'blockchain/transaction/transaction-list.html'
    context_object_name = 'transactions'
    ordering = ['-date_posted']
    paginate_by = 5


class UserTransactionListView(ListView):
    model = Transaction
    template_name = 'blockchain/transaction/user-transaction.html'
    context_object_name = 'transactions'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Transaction.objects.filter(author=user).order_by('-date_posted')


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'blockchain/transaction/transaction-details.html'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = 'blockchain/transaction/transaction-form.html'
    fields = [
        'title',
        'double_spend',
        'block_height',
        'time',
        'relayed_by',
        'hash',
        'tx_index',
        'version',
        'size',
        'inputs',
        'outputs'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transaction
    template_name = 'blockchain/transaction/transaction-update.html'
    fields = [
        'title',
        'double_spend',
        'block_height',
        'time',
        'relayed_by',
        'hash',
        'tx_index',
        'version',
        'size',
        'inputs',
        'outputs'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.author:
            return True
        else:
            return False


class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    template_name = 'blockchain/transaction/transaction-confirm-delete.html'
    success_url = '/'

    def test_func(self):
        transaction = self.get_object()
        if self.request.user == transaction.author:
            return True
        return False
