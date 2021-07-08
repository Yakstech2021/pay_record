# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from .forms import PaymentForm
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa



def home(request):
    return render(request, "home.html")

def Registration(request):
    return render(request, "Registration.html")

def create_payment(request, ):
    if request.method == 'POST':
        payment_name = request.POST['ptname']
        cash_from_bank = request.POST['cash4b']
        cash_to_bank = request.POST['cash2b']
        revenue_from_counter = request.POST['revenue']
        remittance_from_counter = request.POST['remittance']
        deposit_from_counter = request.POST['deposit']
        revenue = request.POST['rev']
        remittance = request.POST['remit']
        deposit = request.POST['dep']

      
        payment = Payment.objects.create(payment_name=payment_name,
                                         cash_from_bank=cash_from_bank,
                                         cash_to_bank=cash_to_bank,
                                         revenue_from_counter=revenue_from_counter,
                                         remittance_from_counter=remittance_from_counter,
                                         deposit_from_counter=deposit_from_counter,
                                         revenue=revenue,
                                         remittance=remittance,
                                         deposit=deposit,
                                         
                                         
                                         )
                                    
    
        return redirect('payment:pdf_preview', payment.id)
    else:
        return render(request, "payment.html")


def pdf_preview(request, *args, **kwargs):
    pk = kwargs.get('pk')
    payment = get_object_or_404(Payment, pk=pk)
    context = {
        'payment': payment
    }
    template = get_template('pdf_preview.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename= payment_for_{payment.payment_name}.pdf'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

