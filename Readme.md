Curso : https://www.udemy.com/course/sistema-de-compra-y-facturacion-con-python-usando-django/learn/lecture/14648928#overview


# Creamos el entorno virtual.
```
virtualenv env --python=python3
source env/bin/activate
```

# Aplicamos migraciones.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

# Guardamos las dependencias
```
pip freeze > requirements.txt
```


# Entramos a la sheel
```
 python3 manage.py dbshell
 \dt
 \q
 select * from auth_user;
```
