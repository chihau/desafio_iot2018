# Desafío IoT 2018 - 3iE

## Introducción al Big Data

### Herramientas para obtener y preparar datos en Linux

* Puedes ejecutar los siguientes comandos desde cualquier Linux o MacOS en una instancia de GCP, Máquina Virtual o Computador

* Instalar Git
```
sudo apt-get install git
```

* Descargar este repo de github
```
git clone https://github.com/chihau/desafio_iot2018.git
```

* Ir al directorio descargado
```
cd desafio_iot2018
```

* Ver las primeras 10 líneas de un archivo
```
head -10 players.csv
```

* Ver las últimas 10 líneas de un archivo
```
tail -10 players.csv
```

* Contar las líneas, palabras y caracteres
```
wc players.csv
```

* Contar las líneas
```
wc -l players.csv
```

* Mostrar las líneas que contienen la palabra "vidal"
```
grep -i "vidal" players.csv
```

* Mostrar la cantidad de jugadores chilenos
```
grep -i "chile" players.csv | wc -l
```

* Reemplazar las comas por tabs
```
grep -i "Chile" players.csv | tr ',' '\t'
```

* Mostrar sólo la primera columna (nombre del jugador)
```
grep -i "Chile" players.csv | cut -d ',' -f1
```

* Mostrar las 3 primeras columna (nombre del jugador, país y posición)
```
grep -i "Chile" players.csv | cut -d ',' -f1-3
```

* Mostrar la cantidad de jugadores chilenos, que jugaron algún partido según su posición
```
grep -i "Chile" players.csv | cut -d ',' -f3 | sort |uniq -c
```

### Hadoop con Dataproc

* Primero tenemos que crear un cluster Dataproc en GCP

* Luego nos conectamos vía ssh al nodo master

* Listamos los nodos
```
hdfs dfsadmin -report
```

* Descargar este repo de github
```
git clone https://github.com/chihau/desafio_iot2018.git
```

* Formateamos el texto
```
cat ~/desafio_iot2018/a_la_una_violeta_parra.txt | tr 'A-Z' 'a-z' | tr -d , | tr -d . > ~/violeta.txt
```

* Vamos al directorio
```
cd /usr/lib/hadoop-mapreduce/
```

* Listamos los ejemplos de hadoop con mapreduce
```
hadoop jar hadoop-mapreduce-examples.jar
```

* Listamos los archivos que contiene el HDFS
```
hdfs dfs -ls /
```

* Copiamos el archivo de texto 
```
hdfs dfs -put ~/violeta.txt /
```

* Ejecutamos el ejemplo WordCount
```
hadoop jar hadoop-mapreduce-examples.jar wordcount /violeta.txt /texto-out
```

* Chequeamos que WordCount generó un resultado
```
hdfs dfs -ls /texto-out
```

* Generamos un archivo con el resultado completo
```
hadoop fs -getmerge /texto-out/ ~/resultado.txt
```

* Vemos el resultado
```
cat ~/resultado.txt
```


