from django.shortcuts import render
from .models import Account
# Create your views here.


def ContactBookHome(request):   
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        newContact = Account.objects.create(name=name,mobile=mobile,email=email,address=address)
        newContact.save()
        Accounts = Account.objects.all()
        return render(request,'ContactBook/ContactBookHome.html',{'Accounts':Accounts})
    Accounts = Account.objects.all()
    return render(request,'ContactBook/ContactBookHome.html',{'Accounts':Accounts})

def updateContactForm(request):
    if request.method == 'POST':
        id = request.POST['to_update']
        updateAccount = Account.objects.get(id=id)
        return render(request,'ContactBook/updateContactForm.html',{'updateAccount':updateAccount})
    
def updateContact(request):
    if request.method == 'POST':
        id = request.POST['id']  
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']
        Account.objects.filter(id=id).update(name=name,mobile=mobile,email=email,address=address)
        Accounts = Account.objects.all()
        return render(request,'ContactBook/ContactBookHome.html',{'Accounts':Accounts})  

def deleteContact(request):
    if request.method == 'POST':
        id = request.POST['to_delete']
        Account.objects.get(id=id).delete()
        Accounts = Account.objects.all()
        return render(request,'ContactBook/ContactBookHome.html',{'Accounts':Accounts})

def searchContact(request):
    if request.method == 'POST':
        searchingContact = request.POST['searching']
        if searchingContact.isalpha():
            try:
                outContact = Account.objects.get(name=searchingContact)
                return render(request,'ContactBook/searchContact.html',{'status':True,'outContact':outContact})
            except:
                return render(request,'ContactBook/searchContact.html',{'failed':True})
        else:
            searchingContact = str(searchingContact)
            if searchingContact.isnumeric():
                try:
                    outContact = Account.objects.get(mobile=int(searchingContact))
                    return render(request,'ContactBook/searchContact.html',{'status':True,'outContact':outContact})
                except:
                    return render(request,'ContactBook/searchContact.html',{'failed':True})
    return render(request,'ContactBook/searchContact.html')        