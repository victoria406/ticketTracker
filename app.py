from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tickets = []


@app.route('/')
def index():
    return render_template('index.html', tickets=tickets)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['description']
        tickets.append({
            'id': len(tickets) + 1,
            'title': title,
            'description': description,
            'status': 'Open'
        })
        return redirect('/')
    return render_template('create.html')

@app.route('/update/<int:ticket_id>', methods=['POST'])
def update(ticket_id):
    new_status = request.form['status']
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket['status'] = new_statuss
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
