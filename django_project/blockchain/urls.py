from django.urls import path
from . import views
from .views import (
    # BLOCK
    BlocksListView,
    BlockDetailView,
    BlockCreateView,
    BlockUpdateView,
    BlockDeleteView,
    UserBlockListView,
    # TRANSACTION
    TransactionsListView,
    TransactionDetailView,
    TransactionCreateView,
    TransactionUpdateView,
    TransactionDeleteView,
    UserTransactionListView
)

urlpatterns = [
    # DEFAULT
    path('', BlocksListView.as_view(), name='blockchain-home'),
    path('', BlocksListView.as_view(), name='blockchain-blocks'),
    path('about/', views.about, name='blockchain-about'),
    # BLOCK
    path('blocks/', BlocksListView.as_view(), name='blockchain-blocks'),
    path('block/<int:pk>/', BlockDetailView.as_view(), name='blockchain-block-details'),
    path('block/user/<str:username>', UserBlockListView.as_view(), name='user-blocks'),
    path('block/<int:pk>/', BlockDetailView.as_view(), name='blockchian-block-detail'),
    path('block/new/', BlockCreateView.as_view(), name='blockchain-block-create'),
    path('block/<int:pk>/update/', BlockUpdateView.as_view(), name='blockchain-block-update'),
    path('block/<int:pk>/delete/', BlockDeleteView.as_view(), name='blockchain-block-delete'),
    # BLOCK SERIALIZER
    path('block/serializer/', views.block_list),
    path('block/serializer/<int:pk>/', views.block_detail),
    # TRANSACTION
    path('transactions/', TransactionsListView.as_view(), name='blockchain-transactions'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='blockchain-transaction-details'),
    path('transaction/user/<str:username>', UserTransactionListView.as_view(), name='user-transactions'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='blockchian-transaction-detail'),
    path('transaction/new/', TransactionCreateView.as_view(), name='blockchain-transaction-create'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='blockchain-transactoin-update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='blockchain-transaction-delete'),


]
