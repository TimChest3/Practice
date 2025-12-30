from flask import Flask, render_template, request
import json


app = Flask(__name__)

def calculate_financial_path(tuition_fee, discounts, grants, installments):
    total_paid = tuition_fee - discounts - grants
    monthly_payment = total_paid / installments if installments > 0 else 0
    return {
        "tuition_fee": tuition_fee,
        "discounts": discounts,
        "grants": grants,
        "total_paid": total_paid,
        "installments": installments,
        "monthly_payment": round(monthly_payment, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        data = request.form
        tuition_fee = float(data.get('tuition_fee', 0))
        discounts = float(data.get('discounts', 0))
        grants = float(data.get('grants', 0))
        installments = int(data.get('installments', 1))
        
        result = calculate_financial_path(tuition_fee, discounts, grants, installments)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
