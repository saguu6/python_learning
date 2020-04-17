# python_learning

Note : you can download annaconda or miniconda pacakge both will work for python.

download anacoda for python with pre-installed packages
https://www.anaconda.com/distribution/

download miniconda with only conda anda python .
https://conda.io/en/latest/miniconda.html

to install package type in terminal -- >
bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh

// ~/Downloads is the path of the anacoda.sh file

#Django

For documentation on Django go to this link
https://docs.djangoproject.com/

To know which pyhton version supports , which django version go to below link
https://docs.djangoproject.com/en/3.0/faq/install/#faq-python-version-support


Creating virtual environment:

(Note : Since python pacakges get updated its better to create a virtual environment so that it doesn't effect our web app. You can create virtual env of newer version packages)

Annaconda makes it easier to create virtual environment since it has virtual environment handler.


To use virtual environment in terminal type

conda create --name myEnv django  

This command will create a environamnet with latest version of django
myEnv - is the name of the virtual environment

To activate this environment
activate myEnv

To deactivate this environment
deactivate myEnv

To know more about creating conda environment go to below link
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

After activating the env also you can install the packages that are required

conda install django

for normal python distributions
pip install django

To create project in django
django-admin startproject first_project   

first_project is projectroot folder

To run the project
python manage.py runserver
