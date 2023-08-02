"""
URL configuration for loan_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from managers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showHomeView, name='home'),
    # USER
    path('register/', views.registerUser, name='register'),
    path('accounts/login/', views.loginView, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/edit/<int:pk>', views.editUser, name='edit-user'),
    path('users/delete/<int:pk>', views.deleteUser, name='delete-user'),
    path('users/<int:pk>', views.userDetailView, name='detail-view'),
    path('users/security/<int:pk>', views.editSecurity, name='security'),
    # ACCOUNT
    path('accounts/', views.accountListView, name='accounts'),
    path('accounts/<int:pk>', views.accountDetailView, name = 'detail-account'),
    path('accounts/create/', views.createAccount, name='create-account'),
    path('accounts/edit/<int:pk>', views.editAccount, name='edit-account'),
    path('accounts/delete/<int:pk>', views.deleteAccount, name='delete-account'),
    # CATEGORY
    path('categories/', views.categoryListView, name='categories'),
    path('categories/<int:pk>/', views.categoryDetailView, name='detail-category'),
    path('categories/create/', views.createCategory, name='create-category'),
    path('categories/edit/<int:pk>/', views.editCategory, name='edit-category'),
    path('categories/delete/<int:pk>/', views.deleteCategory, name='delete-category'),
    # BUDGET
    path('budgets/', views.budgetListView, name='budgets'),
    path('budgets/<int:pk>/', views.budgetDetailView, name='detail-budget'),
    path('budgets/create/', views.createBudget, name='create-budget'),
    path('budgets/edit/<int:pk>/', views.editBudget, name='edit-budget'),
    path('budgets/delete/<int:pk>/', views.deleteBudget, name='delete-budget'),
    # TRANSACTION
    path('transactions/', views.transactionListView, name='transactions'),
    path('transactions/<int:pk>/', views.transactionDetailView, name='detail-transaction'),
    path('transactions/create/', views.createTransaction, name='create-transaction'),
    path('transactions/edit/<int:pk>/', views.editTransaction, name='edit-transaction'),
    path('transactions/delete/<int:pk>/', views.deleteTransaction, name='delete-transaction'),
    # GOAL
    path('goals/', views.goalListView, name='goals'),
    path('goals/<int:pk>/', views.goalDetailView, name='detail-goal'),
    path('goals/create/', views.createGoal, name='create-goal'),
    path('goals/edit/<int:pk>/', views.editGoal, name='edit-goal'),
    path('goals/delete/<int:pk>/', views.deleteGoal, name='delete-goal'),

    # Reminder
    path('reminders/', views.reminderListView, name='reminders'),
    path('reminders/create/', views.createReminder, name='create-reminder'),
    path('reminders/edit/<int:pk>/', views.editReminder, name='edit-reminder'),
    path('reminders/delete/<int:pk>/', views.deleteReminder, name='delete-reminder'),
    path('reminders/<int:pk>/', views.reminderDetailView, name='detail-reminder'),

    # SavingsGoal
    path('savings-goals/', views.savingsGoalListView, name='savings-goals'),
    path('savings-goals/create/', views.createSavingsGoal, name='create-savings-goal'),
    path('savings-goals/edit/<int:pk>/', views.editSavingsGoal, name='edit-savings-goal'),
    path('savings-goals/delete/<int:pk>/', views.deleteSavingsGoal, name='delete-savings-goal'),
    path('savings-goals/<int:pk>/', views.savingsGoalDetailView, name='detail-savings-goal'),

    # Tax
    path('taxes/', views.taxListView, name='taxes'),
    path('taxes/create/', views.createTax, name='create-tax'),
    path('taxes/edit/<int:pk>/', views.editTax, name='edit-tax'),
    path('taxes/delete/<int:pk>/', views.deleteTax, name='delete-tax'),
    path('taxes/<int:pk>/', views.taxDetailView, name='detail-tax'),

    # Report
    path('reports/', views.reportListView, name='reports'),
    path('reports/create/', views.createReport, name='create-report'),
    path('reports/edit/<int:pk>/', views.editReport, name='edit-report'),
    path('reports/delete/<int:pk>/', views.deleteReport, name='delete-report'),
    path('reports/<int:pk>/', views.reportDetailView, name='detail-report'),
]
