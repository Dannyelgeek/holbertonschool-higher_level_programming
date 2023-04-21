// updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header.

$('div').click(function () {
  $('#red_header').css({ 'color': '#FF0000' });
});
