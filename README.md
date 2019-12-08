# python-calc

```
$ pip install -r requirements.txt
```


Start app
```
$ python main.py
```

Run tests
```
$ python -m unittest test_calc.py -v
$ python -m unittest discover -v 
```

Code coverage
```
$ coverage run src/main.py
$ coverage run test_calc.py
$ coverage report
$ coverage html
$ open htmlcov/index.html
```

Docker2
```
$ docker build -t mario21ic/pycalc:v1.0 .
$ docker run -p 8080:8080 mario21ic/pycalc:v1.0
```

Docker Compose
```
$ docker-compose up
```

Nueva linea para ci automatico
