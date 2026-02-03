from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.db.models import Q

def ContactBookHome(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            mobile = request.POST.get('phone', '').strip()
            email = request.POST.get('email', '').strip()
            address = request.POST.get('address', '').strip()

            if name and mobile:
                Account.objects.create(
                    name=name,
                    mobile=mobile,
                    email=email,
                    address=address
                )

            return redirect('home')

        except Exception as e:
            print("ERROR:", e)   # 👈 shows in Render logs
            return render(request, 'ContactBook/ContactBookHome.html', {
                'Accounts': Account.objects.all(),
                'error': 'Something went wrong'
            })

    return render(request, 'ContactBook/ContactBookHome.html', {
        'Accounts': Account.objects.all()
    })



def updateContactForm(request):
    if request.method == 'POST':
        contact_id = request.POST.get('to_update')
        updateAccount = get_object_or_404(Account, id=contact_id)

        return render(
            request,
            'ContactBook/updateContactForm.html',
            {'updateAccount': updateAccount}
        )

    return redirect('home')


def updateContact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('id')
        account = get_object_or_404(Account, id=contact_id)

        account.name = request.POST.get('name')
        account.mobile = request.POST.get('mobile')
        account.email = request.POST.get('email')
        account.address = request.POST.get('address')
        account.save()

        return redirect('home')

    return redirect('home')


def deleteContact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('to_delete')
        account = get_object_or_404(Account, id=contact_id)
        account.delete()

    return redirect('home')

def searchContact(request):
    if request.method == 'POST':
        searchingContact = request.POST.get('searching').strip()

        # Search by name (case-insensitive, supports spaces)
        contacts = Account.objects.filter(name__icontains=searchingContact)

        # If no name match, try mobile search
        if not contacts.exists() and searchingContact.isdigit():
            contacts = Account.objects.filter(mobile=searchingContact)

        if contacts.exists():
            return render(
                request,
                'ContactBook/searchContact.html',
                {'status': True, 'outContacts': contacts}
            )
        else:
            return render(
                request,
                'ContactBook/searchContact.html',
                {'failed': True}
            )

    return render(request, 'ContactBook/searchContact.html')











