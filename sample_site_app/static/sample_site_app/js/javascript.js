window.addEventListener("load", loaded);

function loaded() {
	// 検索ボタンの設定。
	const search_button = document.getElementById("button_id");
	search_button.addEventListener("click", function () { search() }, false);
}

// おまじない はじまり
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
// おまじない おわり

// 検索ボタン押下の処理。
function search() {
	alert('ボタン押されました。');

	// Ajax通信を開始
	$.ajax({
		url: 'result',
		method: 'POST',
		data: '', // 今のところ渡すデータは無い。
	})
		.done(function (data) {
			// 通信成功時の処理。
			alert('通信成功です。' + data);
		})
		.fail(function () {
			// 通信失敗時の処理。
			alert('エラーです。');
		});
}
