from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.POST:
        return HttpResponse(request.POST['ms'])
    else:
        return render(request, 'Loan_pred_website/home.html')

def results(request):
    """
    the data is taken as follows in the post request dictionary 
    Gender : gender
    Marital status: m_status
    Dependents: dep
    Education complete: edu_status
    Self employed: self_emp
    Income: income
    Loan Amount: l_amount
    Loan Term: l_term
    credit_history: c_history
    Property_type: p_type
    """
    if request.POST:
        form_data = request.POST
        return render(request, 'Loan_pred_website/results.html', form_data)
    else:
        return redirect('LP-home')