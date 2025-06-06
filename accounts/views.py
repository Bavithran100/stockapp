from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, StockItemForm
from .models import User, StockItem
from django.contrib import messages

def landing(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects(username=username).first():
                messages.error(request, 'Username already exists')
            else:
                user = User(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful. Please login.')
                return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects(username=username, password=password).first()
            if user:
                request.session['username'] = username
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'dashboard.html', {'username': username})

def add_stock_item(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            time = form.cleaned_data['time'].strftime('%H:%M')
            date = form.cleaned_data['date'].strftime('%d/%m/%Y')
            where_bought_from = form.cleaned_data['where_bought_from']
            quantity = form.cleaned_data['quantity']
            stock_item = StockItem(
                item_name=item_name,
                time=time,
                date=date,
                where_bought_from=where_bought_from,
                quantity=quantity
            )
            stock_item.save()
            messages.success(request, 'Stock item added successfully.')
            return redirect('dashboard')
    else:
        form = StockItemForm()
    return render(request, 'add_stock_item.html', {'form': form})

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('login')

def view_stock_items(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    query = request.GET.get('q', '')
    if query:
        stock_items = StockItem.objects(item_name__icontains=query)
    else:
        stock_items = StockItem.objects()

    return render(request, 'view_stock_items.html', {'stock_items': stock_items, 'query': query})

def low_stock_alerts(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    low_stock_items = StockItem.objects(quantity__lt=20)

    return render(request, 'low_stock_alerts.html', {'stock_items': low_stock_items})

def delete_stock_items(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    query = request.GET.get('q', '')
    if query:
        stock_items = StockItem.objects(item_name__icontains=query)
    else:
        stock_items = StockItem.objects()
    return render(request, 'delete_stock_items.html', {'stock_items': stock_items, 'query': query})

def edit_stock_item(request, item_id):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    stock_item = StockItem.objects(id=item_id).first()
    if not stock_item:
        messages.error(request, "Stock item not found.")
        return redirect('delete_stock_items')

    if request.method == 'POST':
        if 'delete' in request.POST:
            stock_item.delete()
            messages.success(request, "Stock item deleted successfully.")
            return redirect('delete_stock_items')

        item_name = request.POST.get('item_name')
        time = request.POST.get('time')
        date = request.POST.get('date')
        where_bought_from = request.POST.get('where_bought_from')
        quantity = request.POST.get('quantity')

        try:
            quantity = int(quantity)
            if quantity < 0:
                messages.error(request, "Quantity cannot be negative.")
                return render(request, 'edit_stock_item.html', {'stock_item': stock_item})
        except ValueError:
            messages.error(request, "Invalid quantity.")
            return render(request, 'edit_stock_item.html', {'stock_item': stock_item})

        stock_item.update(
            set__item_name=item_name,
            set__time=time,
            set__date=date,
            set__where_bought_from=where_bought_from,
            set__quantity=quantity
        )
        messages.success(request, "Stock item updated successfully.")
        return redirect('delete_stock_items')

    return render(request, 'edit_stock_item.html', {'stock_item': stock_item})
