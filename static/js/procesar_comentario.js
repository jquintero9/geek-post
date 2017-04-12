

	$form = $("form#comentario-form");

	$form.on('submit', function(event) {
		event.preventDefault();
		comentario = $form[0]['comentario'].value;
		usuario = $form[0]['usuario'].value;
		articulo = $form[0]['articulo'].value;
		csrfMiddleware = $form[0]['csrfmiddlewaretoken'].value;

		submitData = {
			"comentario": comentario,
			"usuario": usuario,
			"articulo": articulo 
		};

		console.log(usuario);
		console.log(articulo);

		console.log(submitData);

		$.ajax({
			data: JSON.stringify(submitData),
			type: "POST",
			dataType: "json",
			headers: {
				'X-CSRFToken': csrfMiddleware,
				"Content-Type": "application/json; charset=UTF-8"
			},
			url: "procesar_comentario",
			sucess: function(data) {
				console.log(data);
			}
		});
	});



