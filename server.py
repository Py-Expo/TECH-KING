from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

job_postings=[]
job_applications=[]
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       # Perform login validation here (e.g., check username and password against a database)
       # For demonstration purposes, let's assume the login is successful
       if username == 'admin' and password == 'password':
        return redirect(url_for('index'))
       else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        job_title = request.form['job_title']
        company_name = request.form['company_name']
        job_description = request.form['job_description']
        
        # Store the job posting (in real application, save to database)
        job_postings.append({'title': job_title, 'company': company_name, 'description': job_description})
        
        return "Job posted successfully."
    else:
        return render_template('post.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        resume = request.files['resume']
        job = request.form.get('job')

        # Save the job application (in real application, save to database)
        job_applications.append({'name': name, 'email': email, 'resume': resume.filename, 'job': job})
        
        # Process the form data (e.g., save to database, send email, etc.)
        # Here, you can add code to save the resume file to a specific location
        
        return f"<h2>Application Submitted Successfully</h2><p>Name: {name}</p><p>Email: {email}</p><p>Job: {job}</p>"
    
    return render_template('apply.html')

@app.route('/market-trends')
def market_trends():
    # Logic to display current market trends
    return render_template('market_trends.html')

0
@app.route('/certifications')
def certifications():
    # Logic to display international certifications
    return render_template('certifications.html')

if __name__ == '__main__':
    app.run(debug=True)




