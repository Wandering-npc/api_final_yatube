# api_final
api final
# Как запустить проект
git clone git@github.com:Wandering-npc/api_final_yatube.git
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver