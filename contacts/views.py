from django.contrib import messages
from django.shortcuts import render, redirect
from contacts.forms import NewContact, ContactEdit
from contacts.models import Contact


def contact_list(request):
    context = {}

    lists = Contact.objects.all().order_by('-created_at')
    context['lists'] = lists
    return render(request, 'contacts/lists.html', context)


def create(request):
    context = {}

    form = NewContact(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.info(request, 'New Contacts Created')
            return redirect('contacts:lists')

    context['form'] = form
    return render(request, 'contacts/create.html', context)


def edit(request, pk):
    context = {}

    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return redirect('contacts:lists')

    form = ContactEdit(request.POST or None, instance=contact)

    if request.method == 'POST':
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.info(request, 'Contact has been updated')
            return redirect('contacts:lists')

    context['form'] = form
    return render(request, 'contacts/edit.html', context)


def contact_delete(request, pk):

    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return redirect('contacts:lists')

    contact.delete()
    messages.info(request, 'Conatct Successfully Deleted')
    return redirect('contacts:lists')

