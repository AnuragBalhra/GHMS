$(window).load(function(){
	var href=window.location.href.split('#')[1].split('_')[0];
	console.log(href);

	if(href!=""){
		console.log($('#'+href).offset().top);
		scroll($('#'+href).offset().top);

	}	
});


$(document).ready(function(){

	$('.datepicker').pickadate({
	selectMonths: true, // Creates a dropdown to control month
	selectYears: 15, // Creates a dropdown of 15 years to control year
	format: 'yyyy-mm-dd',
	closeOnSelect: true,
	closeOnClear: true,
	});


	$('select').material_select();
    $('ul.tabs').tabs();
    $('.slider').slider();
    $('.parallax').parallax();
    $('.scrollspy').scrollSpy();


	$('.bookings_form').on('click',function(){
		$('#showBooking').fadeOut("slow");

		var bookingData=$(this).find( 'form' ).serialize();
		var url=$(this).find( 'form' ).attr("action");
		$.ajax({
           type: "POST",
           url: url,
           data: bookingData, // serializes the form's elements.
           success: function(data)
           {
        		$('#showBooking').html(data); // show response from the php script.
				$('#showBooking').fadeIn("slow");

           }
         });
		scroll( );
	});


	$('.users_form').on('click',function(){
		$('#showUser').fadeOut("slow");
		var userData=$(this).find( 'form' ).serialize();
		var url=$(this).find( 'form' ).attr("action");
		$.ajax({
           type: "POST",
           url: url,
           data: userData, // serializes the form's elements.
           success: function(data)
           {
               $('#showUser').html(data); // show response from the php script.
				$('#showUser').fadeIn("slow");
           }
         });
		scroll();

	});

	$('.rooms_form').on('click',function(){
		$('#showRoom').fadeOut("slow");
		var roomData=$(this).find( 'form' ).serialize();
		var url=$(this).find( 'form' ).attr("action");
		$.ajax({
           type: "POST",
           url: url,
           data: roomData, // serializes the form's elements.
           success: function(data)
           {
               $('#showRoom').html(data); // show response from the php script.
				$('#showRoom').fadeIn("slow");
           }
         });
		scroll( );

	});
	

	$('.scrollNav li a').on('click',function(event){
		event.preventDefault();
		gotoClass=$(this).attr('href');
		scroll($(gotoClass).offset().top);
		console.log($(gotoClass).offset().top);
			
	});



});



$('.err').on('click', function(){
	alert('asd');
});




// showRooms Page for User Functions

var roomId=0,checkIn=0,checkOut=0;
$('.date.True').on('click',function(){

	// alert("asd");
	var room=$(this).attr('id').split('_')[0];
	var date=$(this).attr('id').split('_')[1];
	console.log('date = ');
	console.log(date);

	// alert(date);
	if(room==roomId){
		if(checkIn==0){
			checkIn=date;
			checkOut=date;
			console.log('check date = '+date + 'checkOut = '+ checkOut+ " ---" );
		}
		else{
			console.log('check date = '+date + 'checkOut = '+ checkOut+ " ---" );

			if(date>=checkIn && date>checkOut){
				console.log($(this).attr('id').split('_')[1]);
				var startDate=checkIn;
				var error=0;
				$(this).siblings('td').each(function(){
					console.log($(this).attr('id').split('_')[1] + " != "+date);//.attr('id').split('_')[1]);

					if ($(this).attr('id').split('_')[1] >startDate){
						if($(this).attr('id').split('_')[1] > date){							
							return false;
						}
						else{
							if($(this).hasClass('False') ){
								alert('Invalid Dates Selected ');
								error=1;
								return false;
							}
							else{
								checkOut=$(this).attr('id').split('_')[1];
							}
						}
					}

				});
				if(error==0){
					checkOut=date;  // if no Invalid dates are found then checkOut = current date 
				}
			}
			else if(date>checkIn && date<=checkOut){
				checkOut=date;
			}
			else if(date<checkIn){
				console.log('test');
				var lowestPossibleDate=0;
				console.log($(this).attr('id').split('_')[1]);
				var startDate=checkIn;
				var error=0;
				$(this).siblings('td').each(function(){
					console.log($(this).attr('id').split('_')[1] + " != "+date);//.attr('id').split('_')[1]);

					if ($(this).attr('id').split('_')[1] <=startDate){
						if($(this).hasClass('False')!=true && lowestPossibleDate==0){
							lowestPossibleDate=$(this).attr('id').split('_')[1];
							console.log('lowestPossibleDate = ');
							console.log(lowestPossibleDate);
						}

						if($(this).attr('id').split('_')[1] >startDate){							
							return false;
						}
						else{
							if($(this).hasClass('False') && $(this).attr('id').split('_')[1] >=date){
								lowestPossibleDate=0;
								error=1;
								// return false;
							}

						}
					}

				});
				if(error==0){
					checkIn=date;  // if no Invalid dates are found then checkIn = current date 
				}
				else{
					alert('Invalid Dates Selected ');
					checkIn=lowestPossibleDate;
				}
			}
			else{
				var endDate=checkOut;
				var startDate=$(this);
				$(this).siblings('td').each(function(){
					if($(this).attr('id').split('_')[1] >= startDate && $(this).attr('id').split('_')[1] <= checkIn){
						if($(this).hasClass('False') ){
							alert('Invalid Dates Selected ')
							return false;
						}
					}
				});

				checkIn=date;
			}
		}
	}
	else{
		roomId=room;
		checkIn=date;
		checkOut=date;
			console.log('check date = '+date + 'checkOut = '+ checkOut+ " ---" );
	}
	activate();
	// $(this).addClass('active')

	$('.check').html("<th>Selected RoomId :</th> <td>"+roomId+"</td><th> Selected Check In Date :</th><td> "+checkIn+ " </td><th> Selected Check Out Date :</th><td> " + checkOut + " </td> " );
});

function activate(){
	var start, end;
	$('.date').each(function(){
		if($(this).attr('id').split('_')[1] == checkIn && $(this).attr('id').split('_')[0] == roomId){
			start=$(this);
		}
		if($(this).attr('id').split('_')[1] == checkOut && $(this).attr('id').split('_')[0] == roomId){
			end=$(this);
		}

	});
	$('.date').removeClass('active');

	start.siblings('td').each(function(){
		if($(this).attr('id').split('_')[1] > checkIn && $(this).attr('id').split('_')[1] < checkOut){
			$(this).addClass('active');
		}
	});
	// console.log(end);
	start.addClass('active');
	end.addClass('active');


	$('#checkIn').val(checkIn);
	$('#checkOut').val(checkOut);

	// alert($('#finalform').serialize());
}
function clear(){
	checkIn=0;
	checkOut=0;
	roomId=0;
	$('.date').removeClass('stop');
	$('.date').removeClass('active');
}

$('.clear').on('click',function(){
	clear();
	$('.check').html("<th>Selected RoomId :</th> <td>"+roomId+"</td><th> Selected Check In Date :</th><td> "+checkIn+ " </td><th> Selected Check Out Date :</th><td> " + checkOut + " </td> " );
});
$('.bookRoom').on('click',function(){
	bookRoom();
});
function bookRoom(){
	$("#finalform").submit();
    // $.post("process.php", $("#reg-form").serialize(), function(data) {
    //     alert(data);
    // });
}




function scroll(final_pos=0){
	var body = $("html, body");
	body.stop().animate({scrollTop:final_pos}, 1500, 'swing');

}

