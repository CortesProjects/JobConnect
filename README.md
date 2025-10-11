# JobConnect

Project title & short description
<h3>Title:</h3> Job Connect<br>

<h3>Description:</h3>
Our project focuses on <u>helping people find companies</u> where they can <u>apply for jobs</u>. While our main target audience is students, anyone can become an applicant and apply to a company. <u>Employers</u> are also able to <u>create listings and manage applications</u> to connect with potential candidates.

<h3>Setup & run instructions:</h3>
open cmd<br>
<span style="color:blue">git clone</span><br>
<span style="color:blue">cd jobconnect</span><br>
<span style="color:blue">python backend/manage.py runserver</span><br>
or <br>
<span style="color:blue">python jobconnect\backend\manage.py runserver</span><br>

<h5 style="color:red">"if login fails"</h5>
<span style="color:blue">python backend/manage.py migrate</span><br>
<span style="color:blue">python backend/manage.py runserver</span><br>

<h5 style="color:red">"ModuleNotFoundError: No module named 'request'"</h5>
<span style="color:blue">cd jobconnect</span><br>
<span style="color:blue">python -m <span style="color:purple">venv</span> env</span><br>
<span style="color:blue">env\scripts\activate</span><br>
<h5 style="color:red">"ModuleNotFoundError (but many module) do this"</h5>
<span style="color:red">pip install</span> <span style="color:purple">django-allauth</span> <span style="color:purple">"django-allauth[providers]"</span> <span style="color:purple">requests</span> <span style="color:purple">"fastapi[all]"</span> <span style="color:purple">uvicorn</span> <span style="color:purple">supabase</span> <span style="color:purple">Django</span><br>
<span style="color:blue">python backend/manage.py runserver</span><br>

<h3>Team:</h3>
Isaac Raphael P. Cortes - Lead Developer<br>
Richemmae V. Bigno - Full-Stack Developer<br>
Ken Daniel E. Cortes - Full-Stack Developer<br>
<br>
Paul Andrie E. Bibit - Project Owner<br>
Justine Filip D. Custodio - Business Analyst<br>
Van Andrae P. Bigtasin - Scrum Master<br>

<h3>Deployed Link:</h3> NOT Yet Available
