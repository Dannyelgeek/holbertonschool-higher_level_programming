/* fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello
 from that fetch in the HTML tag DIV#hello.*/

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
  { hello: '' }, function (data) {
    $('#hello').append(data.hello);
  });
