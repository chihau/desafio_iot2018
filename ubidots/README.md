## Ejemplo para crear un dispositivo que envíe datos de temperatura de Ubidots

* Puedes ejecutar esta aplicación de prueba desde cualquier dispositivo que corre Linux y Python (Raspberry PI, Máquina Virtual, Instancia GCP, etc...)

* Primero debes crear una cuenta Educativa en [Ubidots](https://app.ubidots.com/accounts/signup/)

* Luego tienes iniciar sesión y ir a API Credentials y copiar el Default Token

* Instalar pip
```
sudo apt-get update && sudo apt-get install python-pip
```

* Instalar la biblioteca requests a través de pip
```
pip install requests
```

* Editar el código en el archivo ubidots_test.py, reemplazando TOKEN_AQUI por el Default Token que generó Ubidots

* Ejecutar la app de prueba
```
python ubidots_test.py
```
