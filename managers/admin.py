from django.contrib import admin
from .models import User, Account, Transaction, Category, Budget, Goal, Reminder, SavingsGoal, Tax, Report

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(Goal)
admin.site.register(Reminder)
admin.site.register(SavingsGoal)
admin.site.register(Tax)
admin.site.register(Report)
