from django.urls import path
from . import views
from .views import (
    # BLOCK
    BlocksListView,
    BlockDetailView,

    # TRANSACTION
    TransactionsListView,
    TransactionDetailView,

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

    # BLOCK
    path('blocks/', BlocksListView.as_view(), name='blockchain-blocks'),
    path('block/<int:pk>/', BlockDetailView.as_view(), name='blockchain-block-details'),

    # TRANSACTION
    path('transactions/', TransactionsListView.as_view(), name='blockchain-transactions'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='blockchain-transaction-details'),

    # INPUTS
    path('inputs/', InputsListView.as_view(), name='blockchain-inputs'),
    path('input/<int:pk>/', InputDetailView.as_view(), name='blockchain-input-details'),

    # OUTPUTS
    path('outputs/', OutputsListView.as_view(), name='blockchain-outputs'),
    path('output/<int:pk>/', OutputDetailView.as_view(), name='blockchain-output-details'),
]




