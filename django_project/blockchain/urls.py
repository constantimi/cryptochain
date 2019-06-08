from django.urls import path
from . import views
from .views import (
    # BLOCK
    BlocksListView,
    BlockDetailView,
    BlockUpdateView,
    BlockDeleteView,
    UserBlockListView,
    # TRANSACTION
    TransactionsListView,
    TransactionDetailView,
    TransactionUpdateView,
    TransactionDeleteView,
    UserTransactionListView,
    # INPUTS
    InputsListView,
    InputDetailView,
    # OUTPUTS
    OutputsListView,
    OutputDetailView
)

urlpatterns = [
    # DEFAULT
    path('', views.home, name='blockchain-home'),
    path('about/', views.about, name='blockchain-about'),

    # BLOCK
    path('blocks/', BlocksListView.as_view(), name='blockchain-blocks'),
    path('block/<int:pk>/', BlockDetailView.as_view(), name='blockchain-block-details'),

    path('block/user/<str:username>', UserBlockListView.as_view(), name='user-blocks'),
    path('block/<int:pk>/update/', BlockUpdateView.as_view(), name='blockchain-block-update'),
    path('block/<int:pk>/delete/', BlockDeleteView.as_view(), name='blockchain-block-delete'),

    # TRANSACTION
    path('transactions/', TransactionsListView.as_view(), name='blockchain-transactions'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='blockchain-transaction-details'),

    path('transaction/user/<str:username>', UserTransactionListView.as_view(), name='user-transactions'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='blockchain-transactoin-update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='blockchain-transaction-delete'),

    # INPUTS
    path('inputs/', InputsListView.as_view(), name='blockchain-inputs'),
    path('input/<int:pk>/', InputDetailView.as_view(), name='blockchain-input-details'),

    # OUTPUTS
    path('outputs/', OutputsListView.as_view(), name='blockchain-outputs'),
    path('output/<int:pk>/', OutputDetailView.as_view(), name='blockchain-output-details'),
]




