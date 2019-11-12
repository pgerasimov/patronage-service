$(document).ready(function () {
	if(jQuery.fn.datepicker) {
		$('input.date').datepicker();
	}

	$('a[data-toggle="modal"]').on('click', function(e) {
		var href = e.currentTarget.getAttribute('href');
		if (!href || href.indexOf('#') === 0) { return; }

		var target_modal = $(e.currentTarget).data('target');
		var remote_content = e.currentTarget.href;

		var modal = $(target_modal);
		var modalBody = $(target_modal + ' .modal-body');

		modal.off('show.bs.modal');
		modal.on('show.bs.modal', function () {
			modalBody.load(remote_content);
		}).modal();

		return false;
	});
	
	$('a.toggle-form').on('click', function(e) {
		e.preventDefault();
		$('.tohide').slideToggle();
		$(this).find('span').toggleClass('icon-double_up icon-double_down');
	});
	if(($('#patronazh-list').outerHeight() - 200) < ($('#filter-form').outerHeight()/2)){
		$('a.toggle-form').trigger( "click" );
	}

	var o = $("#map");
	if (o) {
		try {
			ymaps.ready(function () {
				var myMap = new ymaps.Map(o.attr("id"), {
					center: o.data("place"),
					zoom: o.data("zoom")? o.data("zoom") : 14,
					controls: ['smallMapDefaultSet']
				});
				
				myMap.geoObjects.add(new ymaps.Placemark(o.data("place"), {
						balloonContent: o.data("name")
				}, {
						preset: 'islands#icon',
						iconColor: '#FE7C4A'
				}));
				
				//myMap.behaviors.disable(['scrollZoom']);
				//myMap.setBounds(myMap.geoObjects.getBounds());
				
			});
		} catch(err) {
			console.log(err);
		}
	}
});