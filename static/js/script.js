function login()
{
	var url = window.location.href;

	var str = url.split("?")[1];

	if (str !== 'undefined') {
		var msg = str.split("=")[1];
		alert(msg.split('+').join(' '));
	}
}