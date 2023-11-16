from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import cgi
import os
# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8090  # Порт для доступа по сети

with open('/home/geydarovr/Загрузки/errors_employees/progect/index.html', 'r') as file:
    data = file.read()


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        fileitem = form['f']
        if fileitem.filename:
            save_path = '/home/geydarovr/Загрузки/errors_employees/progect'
            fn = os.path.join(os.fsencode(save_path), os.fsencode(os.path.basename(fileitem.filename)))
            with open(fn, 'wb') as f:
                f.write(fileitem.file.read())

            self.send_response(200)
            self.end_headers()
            decoded_path = os.fsdecode(fn)

            self.wfile.write((f"File '{decoded_path}' файл загружен").encode('utf-8'))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("No file was uploaded".encode('utf-8'))

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        post = self._render_form()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(post, "utf-8"))  # Тело ответа

    def _render_form(self):
        return data


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")