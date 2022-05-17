#!/bin/sh

python dinamic_formset/manage.py migrate
python dinamic_formset/manage.py runserver 0.0.0.0:5000