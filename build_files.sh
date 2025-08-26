# build_files.sh

cd Equipment_accounting_system
pip install -r requirements.txt
python3.x manage.py collectstatic --no-input --clear