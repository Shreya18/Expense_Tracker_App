from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64

def index(request):
    expenses = Expense.objects.all()
    return render(request, 'index.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        item = request.POST['item']
        cost = float(request.POST['cost'])
        currency = request.POST['currency']
        purchased_date = datetime.strptime(request.POST['purchased_date'], '%Y-%m-%d')
        completion_date = request.POST.get('completion_date')
        if completion_date:
            completion_date = datetime.strptime(completion_date, '%Y-%m-%d')
        else:
            completion_date = None

        Expense.objects.create(item=item, cost=cost, currency=currency,
                               purchased_date=purchased_date, completion_date=completion_date)
        return redirect('index')
    return render(request, 'add_expense.html')

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('index')

def dashboard(request):
    expenses = Expense.objects.all()
    data = {}
    for expense in expenses:
        month = expense.purchased_date.strftime('%Y-%m')
        if month not in data:
            data[month] = 0
        data[month] += expense.cost

    months = list(data.keys())
    costs = list(data.values())

    fig, ax = plt.subplots()
    ax.plot(months, costs, marker='o')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Expenses')
    ax.set_title('Monthly Expenses Analysis')

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render(request, 'dashboard.html', {'plot_url': plot_url})
