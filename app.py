from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    total_income = 0
    total_expense = 0
    balance = 0

    if request.method == 'POST':
        # รับค่ารายรับจากฟอร์ม
        income_salary = float(request.form.get('income_salary', 0))
        income_pension = float(request.form.get('income_pension', 0))
        income_invest = float(request.form.get('income_invest', 0))
        income_other = float(request.form.get('income_other', 0))

        # รวมรายรับทั้งหมด
        total_income = income_salary + income_pension + income_invest + income_other

        # รับค่ารายจ่ายจากฟอร์ม
        house = float(request.form.get('house', 0))
        loan = float(request.form.get('loan', 0))
        utilities = float(request.form.get('utilities', 0))
        food = float(request.form.get('food', 0))
        travel = float(request.form.get('travel', 0))
        entertainment = float(request.form.get('entertainment', 0))
        health = float(request.form.get('health', 0))
        education = float(request.form.get('education', 0))
        others = float(request.form.get('others', 0))

        # รวมรายจ่ายทั้งหมด
        total_expense = house + loan + utilities + food + travel + entertainment + health + education + others

        # คงเหลือ
        balance = total_income - total_expense

    return render_template('index.html',
                           total_income=total_income,
                           total_expense=total_expense,
                           balance=balance)

if __name__ == '__main__':
    app.run(debug=True)
