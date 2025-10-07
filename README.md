# JobConnect

Project title & short description
Title: Job Connect<br>
# JobConnect
Our project focuses on helping people find companies where they can apply for jobs. While our main target audience is students, anyone can become an applicant and apply to a company. Employers are also able to create listings and manage applications to connect with potential candidates.
Setup & run instructions:
open cmd
git clone 
cd jobconnect
python backend\manage.py runserver
or 
python jobconnect\backend\manage.py runserver

"if login fails"
python backend\manage.py migrate
python backend\manage.py runserver

"ModuleNotFoundError"
cd jobconnect
python -m venv env
env\scripts\activate
pip install django-allauth "django-allauth[providers]" requests "fastapi[all]" uvicorn supabase Django
python backend\manage.py runserver


Team:
Isaac Raphael P. Cortes - Lead Developer
Richemmae V. Bigno - Full-Stack Developer
Ken Daniel E. Cortes - Full-Stack Developer

Paul Andrie E. Bibit - Project Owner
Justine Filip D. Custodio - Business Analyst
Van Andrae P. Bigtasin - Scrum Master

Deployed Link: NOT Yet Available
