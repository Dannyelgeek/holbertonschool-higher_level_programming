// fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json.

$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
  var titles = data.results.map(function(movie) {
    return movie.title;
  });
  var $list = $('#list_movies');
  $.each(titles, function(i, title) {
    $("<li>").text(title).appendTo($list);
  });
});
