from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showHomeView(request):
    accounts = Account.objects.all()
    budgets = Budget.objects.all()
    categories = Category.objects.all()
    taxes = Tax.objects.all()
    reports = Report.objects.all()
    reminders = Reminder.objects.all()
    savings_goals = SavingsGoal.objects.all()
    goals = Goal.objects.all()
    transactions = Transaction.objects.all()

    account_serializer = AccountSerializer(accounts, many=True)
    budget_serializer = BudgetSerializer(budgets, many=True)
    category_serializer = CategorySerializer(categories, many=True)
    tax_serializer = TaxSerializer(taxes, many=True)
    report_serializer = ReportSerializer(reports, many=True)
    reminder_serializer = ReminderSerializer(reminders, many=True)
    savings_goal_serializer = SavingsGoalSerializer(savings_goals, many=True)
    goal_serializer = GoalSerializer(goals, many=True)
    transaction_serializer = TransactionSerializer(transactions, many=True)

    context = {
        'accounts': account_serializer.data,
        'budgets': budget_serializer.data,
        'categories': category_serializer.data,
        'taxes': tax_serializer.data,
        'reports': report_serializer.data,
        'reminders': reminder_serializer.data,
        'savings_goals': savings_goal_serializer.data,
        'goals': goal_serializer.data,
        'transactions': transaction_serializer.data,
    }

    return Response(context)

def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    form = UserRegistrationForm()
    return render(request, 'user_create.html', {'form': form})

def loginView(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('home')
        else:
            print("ERRORS: ", form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

@login_required
def userDetailView(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})        

@login_required
def editUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST": 
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'The user has been updated successfully!')
        return redirect('home')
    else:
        form = UserCreateForm(instance=user)
        return render(request,'user_edit.html', {'form': form})

@login_required
def editSecurity(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST": 
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'The security has been updated successfully!')
        return redirect('home')
    else:
        form = UserCreationForm(instance=user)
        return render(request,'user_edit.html', {'form': form})

@login_required
def deleteUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request,  'The user has been deleted successfully!')
    return redirect('home')

# ACCOUNT
@login_required
def createAccount(request):
    form = AccountCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            post.user_id = request.user
            post.save()
            messages.success(request,'The Account has been created successfully!')
            return redirect('accounts')
    else:
        form = AccountCreationForm()
    
    return render(request, 'account_create.html', {'form': form})

@login_required
def editAccount(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, instance=account)
        if form.is_valid():
            post = form.save()
            post.user_id = request.user
            messages.success(request,'The account has been updated successfully!')
            post.save()
            return redirect('accounts')
    else:
        form = AccountCreationForm(instance=account)
    
    return render(request, 'account_edit.html', {'form': form})

@login_required
def accountListView(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})

@login_required
def deleteAccount(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    messages.success(request,  'The user has been deleted successfully!')
    return redirect('accounts')

@login_required
def accountDetailView(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'account_detail.html', {'account': account})

# CATEGORY
@login_required
def createCategory(request):
    form = CategoryCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'The Category has been created successfully!')
            return redirect('categories')
    else:
        form = CategoryCreationForm()
    
    return render(request, 'category_create.html', {'form': form})

@login_required
def editCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'The category has been updated successfully!')
            return redirect('categories')
    else:
        form = CategoryCreationForm(instance=category)
    
    return render(request, 'category_edit.html', {'form': form})

@login_required
def categoryListView(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def deleteCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'The category has been deleted successfully!')
    return redirect('categories')

@login_required
def categoryDetailView(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

# BUDGET
@login_required
def createBudget(request):
    if request.method == 'POST':
        form = BudgetCreationForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'The budget has been created successfully!')
            return redirect('budgets')
    else:
        form = BudgetCreationForm()
    
    return render(request, 'budget_create.html', {'form': form})

@login_required
def editBudget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetCreationForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'The budget has been updated successfully!')
            return redirect('budgets')
    else:
        form = BudgetCreationForm(instance=budget)
    
    return render(request, 'budget_edit.html', {'form': form})

@login_required
def budgetListView(request):
    budgets = Budget.objects.all()
    return render(request, 'budget_list.html', {'budgets': budgets})

@login_required
def deleteBudget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    budget.delete()
    messages.success(request, 'The budget has been deleted successfully!')
    return redirect('budgets')

@login_required
def budgetDetailView(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    return render(request, 'budget_detail.html', {'budget': budget})

# TRANSACTION
@login_required
def transactionListView(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

@login_required
def createTransaction(request):
    form = TransactionCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save()
            messages.success(request, 'The transaction has been created successfully!')
            return redirect('transactions')
    else:
        form = TransactionCreationForm()
    
    return render(request, 'transaction_create.html', {'form': form})

@login_required
def editTransaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionCreationForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save()
            messages.success(request, 'The transaction has been updated successfully!')
            return redirect('transactions')
    else:
        form = TransactionCreationForm(instance=transaction)
    
    return render(request, 'transaction_edit.html', {'form': form})

@login_required
def deleteTransaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    messages.success(request, 'The transaction has been deleted successfully!')
    return redirect('transactions')

@login_required
def transactionDetailView(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

# GOAL
@login_required
def goalListView(request):
    goals = Goal.objects.all()
    return render(request, 'goal_list.html', {'goals': goals})

@login_required
def createGoal(request):
    form = GoalCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            goal = form.save()
            messages.success(request, 'The goal has been created successfully!')
            return redirect('goals')
    else:
        form = GoalCreationForm()
    
    return render(request, 'goal_create.html', {'form': form})

@login_required
def editGoal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'POST':
        form = GoalCreationForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save()
            messages.success(request, 'The goal has been updated successfully!')
            return redirect('goals')
    else:
        form = GoalCreationForm(instance=goal)
    
    return render(request, 'goal_edit.html', {'form': form})

@login_required
def deleteGoal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    messages.success(request, 'The goal has been deleted successfully!')
    return redirect('goals')

@login_required
def goalDetailView(request, pk):
    print('YES')
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'goal_detail.html', {'goal': goal})

# REMINDER
@login_required
def reminderListView(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder_list.html', {'reminders': reminders})

@login_required
def createReminder(request):
    form = ReminderCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            reminder = form.save()
            messages.success(request, 'The reminder has been created successfully!')
            return redirect('reminders')
    else:
        form = ReminderCreationForm()
    
    return render(request, 'reminder_create.html', {'form': form})

@login_required
def editReminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form = ReminderCreationForm(request.POST, instance=reminder)
        if form.is_valid():
            reminder = form.save()
            messages.success(request, 'The reminder has been updated successfully!')
            return redirect('reminders')
    else:
        form = ReminderCreationForm(instance=reminder)
    
    return render(request, 'reminder_edit.html', {'form': form})

@login_required
def deleteReminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    reminder.delete()
    messages.success(request, 'The reminder has been deleted successfully!')
    return redirect('reminders')

@login_required
def reminderDetailView(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    return render(request, 'reminder_detail.html', {'reminder': reminder})

# SAVINGGOALS
def savingsGoalListView(request):
    savings_goals = SavingsGoal.objects.all()
    return render(request, 'savings_goal_list.html', {'savings_goals': savings_goals})

@login_required
def createSavingsGoal(request):
    form = SavingsGoalCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            savings_goal = form.save()
            messages.success(request, 'The savings goal has been created successfully!')
            return redirect('savings-goals')
    else:
        form = SavingsGoalCreationForm()
    
    return render(request, 'savings_goal_create.html', {'form': form})

@login_required
def editSavingsGoal(request, pk):
    savings_goal = get_object_or_404(SavingsGoal, pk=pk)
    if request.method == 'POST':
        form = SavingsGoalCreationForm(request.POST, instance=savings_goal)
        if form.is_valid():
            savings_goal = form.save()
            messages.success(request, 'The savings goal has been updated successfully!')
            return redirect('savings-goals')
    else:
        form = SavingsGoalCreationForm(instance=savings_goal)
    
    return render(request, 'savings_goal_edit.html', {'form': form})

@login_required
def deleteSavingsGoal(request, pk):
    savings_goal = get_object_or_404(SavingsGoal, pk=pk)
    savings_goal.delete()
    messages.success(request, 'The savings goal has been deleted successfully!')
    return redirect('savings-goals')

@login_required
def savingsGoalDetailView(request, pk):
    savings_goal = get_object_or_404(SavingsGoal, pk=pk)
    return render(request, 'savings_goal_detail.html', {'savings_goal': savings_goal})

# TAX
@login_required
def taxListView(request):
    taxes = Tax.objects.all()
    return render(request, 'tax_list.html', {'taxes': taxes})

@login_required
def createTax(request):
    form = TaxCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            tax = form.save()
            messages.success(request, 'The tax has been created successfully!')
            return redirect('taxes')
    else:
        form = TaxCreationForm()
    
    return render(request, 'tax_create.html', {'form': form})

@login_required
def editTax(request, pk):
    tax = get_object_or_404(Tax, pk=pk)
    if request.method == 'POST':
        form = TaxCreationForm(request.POST, instance=tax)
        if form.is_valid():
            tax = form.save()
            messages.success(request, 'The tax has been updated successfully!')
            return redirect('taxes')
    else:
        form = TaxCreationForm(instance=tax)
    
    return render(request, 'tax_edit.html', {'form': form})

@login_required
def deleteTax(request, pk):
    tax = get_object_or_404(Tax, pk=pk)
    tax.delete()
    messages.success(request, 'The tax has been deleted successfully!')
    return redirect('taxes')

@login_required
def taxDetailView(request, pk):
    tax = get_object_or_404(Tax, pk=pk)
    return render(request, 'tax_detail.html', {'tax': tax})

# REPORT
@login_required
def reportListView(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

@login_required
def createReport(request):
    form = ReportCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            report = form.save()
            messages.success(request, 'The report has been created successfully!')
            return redirect('reports')
    else:
        form = ReportCreationForm()
    
    return render(request, 'report_create.html', {'form': form})

@login_required
def editReport(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportCreationForm(request.POST, instance=report)
        if form.is_valid():
            report = form.save()
            messages.success(request, 'The report has been updated successfully!')
            return redirect('reports')
    else:
        form = ReportCreationForm(instance=report)
    
    return render(request, 'report_edit.html', {'form': form})

@login_required
def deleteReport(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    messages.success(request, 'The report has been deleted successfully!')
    return redirect('reports')

@login_required
def reportDetailView(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report_detail.html', {'report': report})
