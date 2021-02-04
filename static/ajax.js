$( document ).ready(function(){
	        'use strict';

        var snd = new Audio('/static/asdqkqdkk.mp3');

        var Toast = function (element, config) {
            var
                _this = this,
                _element = element,
                _config = {
                    autohide: true,
                    delay: 5000
                };
            for (var prop in config) {
                _config[prop] = config[prop];
            }
            Object.defineProperty(this, 'element', {
                get: function () {
                    return _element;
                }
            });
            Object.defineProperty(this, 'config', {
                get: function () {
                    return _config;
                }
            });
            _element.addEventListener('click', function (e) {
                if (e.target.classList.contains('toast__close')) {
                    _this.hide();
                }
            });
        }

        Toast.prototype = {
            show: function () {
                var _this = this;
                this.element.classList.add('toast_show');
                if (this.config.autohide) {
                    setTimeout(function () {
                        _this.hide();
                    }, this.config.delay)
                }
            },
            hide: function () {
                this.element.classList.remove('toast_show');
            }
        };

        Toast.create = function (header, body, color) {
            var
                fragment = document.createDocumentFragment(),
                toast = document.createElement('div'),
                toastHeader = document.createElement('div'),
                toastClose = document.createElement('button'),
                toastBody = document.createElement('div');
            toast.classList.add('toast');
            toast.style.backgroundColor = 'rgba(' + parseInt(color.substr(1, 2), 16) + ',' + parseInt(color.substr(3, 2), 16) + ',' + parseInt(color.substr(5, 2), 16) + ',0.5)';
            toastHeader.classList.add('toast__header');
            toastHeader.textContent = header;
            toastClose.classList.add('toast__close');
            toastClose.setAttribute('type', 'button');
            toastClose.textContent = '×';
            toastBody.classList.add('toast__body');
            toastBody.textContent = body;
            toastBody.appendChild(toastClose);
            toast.appendChild(toastHeader);
            toast.appendChild(toastBody);
            fragment.appendChild(toast);
            return fragment;
        };

        Toast.add = function (params) {
            var config = {
                header: 'Название заголовка',
                body: 'Текст сообщения...',
                color: '#ffffff',
                autohide: true,
                delay: 5000
            };
            if (params !== undefined) {
                for (var item in params) {
                    config[item] = params[item];
                }
            }
            if (!document.querySelector('.toasts')) {
                var container = document.createElement('div');
                container.classList.add('toasts');
                container.style.cssText = 'position: fixed; top: 15px; right: 15px; width: 250px;';
                document.body.appendChild(container);
            }
            document.querySelector('.toasts').appendChild(Toast.create(config.header, config.body, config.color));
            var toasts = document.querySelectorAll('.toast');
            var toast = new Toast(toasts[toasts.length - 1], { autohide: config.autohide, delay: config.delay });
            toast.show();
            snd.currentTime = 0;
            snd.play();
            return toast;
        }

	function scroll() {
		message_chat1.scrollTop = message_chat1.scrollHeight;
	}
	$(document).on('click', '.btn', function() {
		let a = ''
		a = $(this).attr('id')
		a = a.replace(/[^+-\d]/g, '')

		if (a[0] == '+'){
			a = a.replace(/[^\d]/g, '')
			console.log(Number($('.' + a).text()))
			$('.' + a).text(Number($('.' + a).text())+1)
			$('.' + a + 'discount').text(Number($('.' + a + 'discount').text())+1)
		}

		if (a[0] == '-'){
			a = a.replace(/[^\d]/g, '')
			if (Number($('.' + a).text()) != 0){
			$('.' + a).text(Number($('.' + a).text())-1)
			$('.' + a + 'discount').text(Number($('.' + a + 'discount').text())-1)


		}
		}		
		$.ajax({
			url: 'http://aptekaopeka.ru/ajax/',
			type: 'get',
			data:{
				button_text: $(this).attr('id')
			},
			success: function(response){
				try{
					if (response.delete != 'NENADO'){
						try{
							document.getElementById(response.delete).remove();
						}
						catch{}
						try{
							document.getElementById('widjet_basket_' + response.delete).remove();
						}catch{}
					}
				}
				catch{}
				$(".summ").text(response.summ);
				$("#summ_count" + String(response.id_product)).text('Общая сумма: ' + response.summ_product + ' ₽')
				$("#basket").text(response.count_product_in_basket);
				$("#basketpage").text(response.count_product_in_basket);	
				$("#count").text(response.count);
				$(".widjet-basket-count-edit"+ String(response.id_product)).text(response.seconds);
				$(".widjet-basket-sumprice-edit"+ String(response.id_product)).text(response.summ_product + ' ₽');
				$(".order_inform_js").text('Вего выбрано товара ' + response.count_product_in_basket + ', на сумму ' + response.summ +' ₽  - ')
				Toast.add({
                header: 'Товар ' + String(response.status_object),
                body: 'Товар ' + String(response.status_object),
                color: 'white',
                autohide: true,
                delay: 5000,
           		 });
				}
		});
	});
	$(".send_back_call").on('click', function(){
		$.ajax({
			url: 'http://aptekaopeka.ru/send_back_call/',
			type: 'get',
			data:{
				fio: document.getElementById("back_call_elem_fio").value,
				phone: document.getElementById('back_call_phone').value,
				comment: document.getElementById('back_call_elem_comment').value,
			},
			success: function(response){
				Toast.add({
                header: '',
                body: 'Заявка на обратный звонок была отправлена',
                color: 'white',
                autohide: true,
                delay: 5000,
           		 });
				
		}
		});
	});
});
$(document).ready(function(){
	$(".btn-filter").on('click', function(){
		$.ajax({
			url: 'http://aptekaopeka.ru/ajax/filter',
			type: 'get',
			data:{
				button_filter: $(this).attr('id'),
				search: $(".gde_iskat").attr('id'),
				category: $(".search_product_in_category").attr('id'),
				in_stock: document.getElementById('checkbox1').checked,
				with_discount: document.getElementById('checkbox2').checked,
				prescription_only: document.getElementById('checkbox3').checked,
			},
			success: function(response){
			$(".content2").text('')

			for (let i in response){
				let g = ''
				let recipe = ''
				if (response[i].recipe){
					recipe = '<div class="only-recept"><h5>По рецепту</h5></div>'
				}
				if (response[i].discount != null){
					g =  '<h5 style="font-weight: normal;">Цена:</h5>  <div style="display: flex;align-items: center;"><h5 style="text-decoration:line-through;font-size: 90%;opacity: 0.5"> ' +response[i].price + ' ₽</h5> <h3> ' + response[i].discount + ' </h3><h4 style="font-weight: normal;margin-left:-3px; ">₽</h4></div>'
				}
				else{
					g = '<h5 style="font-weight: normal;">Цена:</h5>  <div style="display: flex;align-items: center;"><h3> ' + response[i].price +  '</3> <h4 style="font-weight: normal;margin-left:-3px; ">₽</h4></div>'
  
				}
				$(".content2").append('<div class="product-box">  ' + recipe + '   <div class="product">  <a href="/product/' + response[i].id +'">  <div class="link">    <div class="product_image">      <img style="height:170px;width:170px" src="/media/' +response[i].image + '" alt=""></div>    <h5 style="text-align: left;width: 100%;color: #1c257b;">' + response[i].name + '</h5> </div></a>  <h5 style="text-align: left;width: 100%;">'+ response[i].company +'</h5>   <div class="price">   ' + g + '</div> <div class="buy-options"><button style="padding:0" type="button" class="btn btn-buy btn-success btn-lg btn-block' + response[i].id + '" id="+:' + response[i].id + '"><h4>Купить</h4></button><button style="padding:0" type="button" class="btn btn-buy btn-success btn-lg btn-' + response[i].id + '" id="-:' + response[i].id + '"><h4>-1</h4></button><h4 style="text-align: center;"><div class="' + response[i].id + ' btn-' + response[i].id + '">1</div></h4> <button style="padding:0" type="button" class="btn btn-buy btn-success btn-lg btn-' + response[i].id + '" id="+:' + response[i].id + '"><h4>+1</h4></button><button style="padding:0" type="button" class="btn btn-buy btn-success btn-lg btn-' + response[i].id + '" id="+:' + response[i].id + '"><img src="{% static "order.png"%}" height="42px;" width="42px"></img></button></div></div></div><style type="text/css">  .btn-' + response[i].id + '{    display: none;  }  .btn-' + response[i].id + '-active{    display: block;    width: 50px;  }</style><script type="text/javascript">  $(".btn-block' + response[i].id + '").click(function(){  console.log("click");  $(".btn-block' + response[i].id + '").toggleClass("btn-block-active");  $(".btn-' + response[i].id + '").toggleClass("btn-' + response[i].id + '-active");});</script>')

			}
		}
		});
	});
});


$(document).ready(function(){
	$(".atctive_widjet").on('click', function(){
		$.ajax({
			url: 'http://aptekaopeka.ru/basket_ajax/',
			type: 'get',
			data:{
			},
			success: function(response){
			$(".basket_objects").text('')
			$(".basket_objects").append(response.message)
			$(".price_in_widjet_basket").text(response.summ)
			$(".count_in_widjet_basket").text(response.count)
			for (let i in response.objects){
				$(".basket_objects").append('<div class="basket_object" id="widjet_basket_' + response.objects[i]['id_product'] + '">			<div class="product_in_basket_widjet_1 dffw">				<img src="/media/' + response.objects[i]['product_thumb'] + '" height="80px;" width="90px" >				<a style="color: black;">' + response.objects[i]['name_product'] + '</a>			</div>			<div class="product_in_basket_widjet_2 ">				<div class="dffr tibw">					<div style="width: 100px;display: flex;justify-content: space-between;">						<h5><button type="button" class="btn btn-success btn-lg btn-cus" id="-:' + response.objects[i]['id_product'] + '">-</button></h5>						<h5><div class="widjet-basket-count-edit' + response.objects[i]['id_product'] + '">' + response.objects[i]['product_count'] + '</div></h5>								<h5><button type="button" class="btn btn-success btn-lg btn-cus" id="+:' + response.objects[i]['id_product'] + '">+</button></h5>					</div>					<h5>Количество: </h5>				</div>				<div class="dffr tibw">					<h5><div class="widjet-basket-sumprice-edit' + response.objects[i]['id_product'] + '"> ' + response.objects[i]['pruduct_count_sum'] + ' ₽</div></h5>					<h5></h5>				</div>			</div>		</div>')
			}
		}
		});
	});
});

$(document).ready(function(){
	$(".btn").on('click', function(){
		$.ajax({
			url: 'http://aptekaopeka.ru/basket_ajax/',
			type: 'get',
			data:{
			},
			success: function(response){
			$(".price_in_widjet_basket").text(response.summ)
			$(".count_in_widjet_basket").text(response.count)
			$(".basket_objects").text('')
			for (let i in response.objects){
				$(".basket_objects").append('<div class="basket_object" id="widjet_basket_' + response.objects[i]['id_product'] + '">			<div class="product_in_basket_widjet_1 dffw">				<img src="/media/' + response.objects[i]['product_thumb'] + '" height="80px;" width="90px" >				<a style="color: black;">' + response.objects[i]['name_product'] + '</a>			</div>			<div class="product_in_basket_widjet_2 ">				<div class="dffr tibw">					<div style="width: 100px;display: flex;justify-content: space-between;">						<h5><button type="button" class="btn btn-success btn-lg btn-cus" id="-:' + response.objects[i]['id_product'] + '">-</button></h5>						<h5><div class="widjet-basket-count-edit' + response.objects[i]['id_product'] + '">' + response.objects[i]['product_count'] + '</div></h5>								<h5><button type="button" class="btn btn-success btn-lg btn-cus" id="+:' + response.objects[i]['id_product'] + '">+</button></h5>					</div>					<h5>Количество: </h5>				</div>				<div class="dffr tibw">					<h5><div class="widjet-basket-sumprice-edit' + response.objects[i]['id_product'] + '"> ' + response.objects[i]['pruduct_count_sum'] + ' ₽</div></h5>					<h5></h5>				</div>			</div>		</div>')
			}
		}
		});
	});
});

