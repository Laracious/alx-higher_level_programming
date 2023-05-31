/* 
 Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
 */
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', functiom (data) {
	$('DIV#character').text(data.name);
});
