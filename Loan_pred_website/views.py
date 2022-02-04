from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import predict
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
        p = predict.Predector()
        form_data = request.POST
        # try:
        udata = [form_data['gender'], form_data['m_status'], float(form_data['dep']), form_data['edu_status'], form_data['self_emp'],
                float(form_data['income']), float(form_data['coincome']), float(form_data['l_amount']), float(form_data['l_term']), 
                float(form_data['c_history']), form_data['p_type']]
        # except Exception as e:
        #     return HttpResponse(f"<center> <H1> DATA ERROR <H1> <br> {e}</center>") #can be changed to return an error on the input page itself #only for debugging 
        
        pred = p.predetor(udata)
        print(pred)
        return render(request, 'Loan_pred_website/results.html', {'result' : pred})
    
    else:
        return redirect('LP-home')