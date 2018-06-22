# Desafío IoT 2018 - 3iE

## Introducción al Big Data

### Herramientas para obtener y preparar datos en Linux

* Ver las primeras 10 líneas de un archivo
```
head -10 Players.csv
```

* Ver las últimas 10 líneas de un archivo
```
head -10 Players.csv
```

* Contar los caracteres, palabras y líneas
```
wc Players.csv
```

* Contar las líneas
```
wc -l Players.csv
```

* Mostrar las líneas que contienen la palabra "vidal"
```
grep -i "vidal" Players.csv
```

* Mostrar la cantidad de jugadores chilenos
```
grep -i “chile” Players.csv | wc -l
```

* Reemplazar las comas por tabs
```
grep -i "Chile" Players.csv | tr ',' '\t'
```

* Mostrar sólo la primera columna (nombre del jugador)
```
grep -i "Chile" Players.csv | cut -d ',' -f1
```

* Mostrar las 3 primeras columna (nombre del jugador, país y posición)
```
grep -i "Chile" Players.csv | cut -d ',' -f1-3
```

* Mostrar la cantidad de jugadores chilenos, que jugaron algún partido según su posición
```
grep -i "Chile" Players.csv | cut -d ',' -f3 | sort |uniq -c
```


