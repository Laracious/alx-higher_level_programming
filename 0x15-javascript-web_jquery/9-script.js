/* Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello. */

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});