# FlaskGetCities

Querystring'de gelen country_code parametresine göre MongoDb'ye bağlanarak ilgili country_code'a ait kayıtları listeler.


Yüklemek için:
Python 3.6 kurulu olmalı.

Aşağıdaki komutları powershell'de sırasıyla çalıştırın.

git clone https://github.com/Caneryy/FlaskGetCities.git
cd .\FlaskGetCities\
.\env\Scripts\activate
flask run

Uygulama ayağa kalktığında tarayıcıdan ya da postman ile http://127.0.0.1:5000/?country_code=us adresine get istek atarak json response'a ulaşabilirsiniz.
