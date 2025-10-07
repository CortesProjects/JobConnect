# JobConnect

Project title & short description
<h3>Title:</h3> Job Connect<br>
<h3>Description:</h3>
Our project focuses on helping people find companies where they can apply for jobs. While our main target audience is students, anyone can become an applicant and apply to a company. Employers are also able to create listings and manage applications to connect with potential candidates.
<h3>Setup & run instructions:</h3>
open cmd<br>
git clone<br>
cd jobconnect<br>
python backend\manage.py runserver<br>
or <br>
python jobconnect\backend\manage.py runserver<br>

"if login fails"<br>
python backend\manage.py migrate<br>
python backend\manage.py runserver<br>

"ModuleNotFoundError"<br>
cd jobconnect<br>
python -m venv env<br>
env\scripts\activate<br>
pip install django-allauth "django-allauth[providers]" requests "fastapi[all]" uvicorn supabase Django
python backend\manage.py runserver<br>


<h3>Team:</h3>
Isaac Raphael P. Cortes - Lead Developer
Richemmae V. Bigno - Full-Stack Developer
Ken Daniel E. Cortes - Full-Stack Developer

Paul Andrie E. Bibit - Project Owner
Justine Filip D. Custodio - Business Analyst
Van Andrae P. Bigtasin - Scrum Master

Deployed Link: NOT Yet Available
