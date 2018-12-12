#!/usr/bin/env python3
#
# An HTTP server that's a message board.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


memory = []

iframe='''<!DOCTYPE html>
  <title>Message Board</title>
<iframe
  id="myFrame"
  width="600"
  height="400"
  seamless
  frameBorder="0"
  scrolling="no"
  src='http://localhost:9999/superset/explore/?form_data=%7B%22datasource%22%3A%223__table%22%2C%22viz_type%22%3A%22pie%22%2C%22slice_id%22%3A55%2C%22url_params%22%3A%7B%7D%2C%22granularity_sqla%22%3A%22ds%22%2C%22time_grain_sqla%22%3A%22P1D%22%2C%22time_range%22%3A%22100+years+ago+%3A+now%22%2C%22metric%22%3A%22sum__num%22%2C%22adhoc_filters%22%3A%5B%5D%2C%22groupby%22%3A%5B%22gender%22%5D%2C%22row_limit%22%3A50000%2C%22pie_label_type%22%3A%22key%22%2C%22donut%22%3Afalse%2C%22show_legend%22%3Atrue%2C%22show_labels%22%3Atrue%2C%22labels_outside%22%3Atrue%2C%22color_scheme%22%3A%22bnbColors%22%7D&standalone=true&height=400'
>
</iframe>
<script>
function myFunction() {
    var x = document.getElementById("myFrame").src;
    document.getElementById("demo").innerHTML = x;
}
</script>
</html>'''

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <select>
  <option value="mesure">mesure</option>
  <option value="latitude">latitude</option>
  <option value="longitude">longitude</option>
  <option value="month">month</option>
  <option value="year">year</option>
  <option value="week">week</option>
</select>
<select>
  <option value="month">month</option>
  <option value="year">year</option>
  <option value="week">week</option>
</select>
<select>
<option value="min">min</option>
<option value="max">max</option>
<option value="moy">moy</option>
</select>
<label> Stations
<input type="text" name="stations"></label>
<button type="submit"> submit </button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):

 def do_GET(self):
    # First, send a 200 OK response.
    self.send_response(200)

    # Then send headers.
    self.send_header('Content-type', 'text/html; charset=utf-8')
    self.end_headers()

    # Send the form with the messages in it.
    self.wfile.write(form.encode())

 def do_POST(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html; charset=utf-8')
    self.end_headers()
    self.wfile.write(iframe.encode())

if __name__ == '__main__':
  server_address = ('', 8000)
  httpd = HTTPServer(server_address, MessageHandler)
  httpd.serve_forever()

