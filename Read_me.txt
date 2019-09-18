1. Create a virtual environment and install the requirements file
  -> pip install -r requirements.txt

2. Make the Django migrations(to set up the models in your system):
  (inside the json_api/jsonproject)
   -> python manage.py makemigrations
   -> python manage.py migrate

3. To save the data in the models(database):

 -> python manage.py shell
 A shell would come up :
 a) from jsonapp import views
 b) views.save_questions() #save the quetions in Quiz model(Model 1)
 c) views.save_answers() #save answers in Model 3
 d)  views.save_options() #save options in model 2

 PS. I Have created 3 models, one for questions, one for answers and one for options.
 All the linked to each other by the foreign kry save_questions

 4. To run the server:

 -> python manage.py runserver

 5. To view the data:
  link -> http://127.0.0.1:8000/data/save-questions/ #for questions
  http://127.0.0.1:8000/data/save-options/ #for options
  http://127.0.0.1:8000/data/save-answers/ #for answers

  You can also view by each question(id):
  the link is in jsonapp/urls.py files.

  THANK YOU!
