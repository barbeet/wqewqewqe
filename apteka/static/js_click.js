$('.search-options').click(function(){

  $('.unvisible-search').toggleClass('unvisible-search-active');
});

$('.ojidaiyt').click(function(){

  $('.ojidaiyt-box-element').toggleClass('ojidaiyt-box-element-active');
  try{
  document.getElementById('go-more1').style.transform = "rotate(-90deg)";
  document.getElementById('go-more1').id = "go-more11";
}catch{
  document.getElementById('go-more11').style.transform = "rotate(-0deg)";
  document.getElementById('go-more11').id = "go-more1";
}

});
$('.odobreno').click(function(){

  $('.odobreno-box-element').toggleClass('odobreno-box-element-active');
    try{
  document.getElementById('go-more2').style.transform = "rotate(-90deg)";
  document.getElementById('go-more2').id = "go-more22";
}catch{
  document.getElementById('go-more22').style.transform = "rotate(-0deg)";
  document.getElementById('go-more22').id = "go-more2";
}
});

$('.otozvano').click(function(){

  $('.otozvano-box-element').toggleClass('otozvano-box-element-active');
    try{
  document.getElementById('go-more3').style.transform = "rotate(-0deg)";
  document.getElementById('go-more3').id = "go-more33";
}catch{
  document.getElementById('go-more33').style.transform = "rotate(-90deg)";
  document.getElementById('go-more33').id = "go-more3";
}
});
$('.button-message').click(function(){

  $('.chat').toggleClass('chat-active');
    function scroll() {
    message_chat1.scrollTop = message_chat1.scrollHeight;
  }
    setTimeout(scroll, 100);
});
$('.close').click(function(){

  $('.chat-active').removeClass('chat-active');
});
$('.btn-filter-name').click(function(){

  try {
    document.getElementById('img-filter2').style.transform = "rotate(0deg)";
    document.getElementById('img-filter3').style.transform = "rotate(0deg)";
    document.getElementById('img-filter').style.transform = "rotate(0deg)";
    document.getElementById('oreder_by_name_+').id = "oreder_by_name_-";
	}
  catch {
    document.getElementById('img-filter').style.transform = "rotate(180deg)";
    document.getElementById('img-filter2').style.transform = "rotate(0deg)";
    document.getElementById('img-filter3').style.transform = "rotate(0deg)";
    document.getElementById('oreder_by_name_-').id = "oreder_by_name_+";
}

});
$('.btn-filter-price').click(function(){

  try {
    document.getElementById('img-filter3').style.transform = "rotate(0deg)";
    document.getElementById('img-filter').style.transform = "rotate(0deg)";
    document.getElementById('img-filter2').style.transform = "rotate(180deg)";
    document.getElementById('oreder_by_price_-').id = "oreder_by_price_+";
	}
  catch {
    document.getElementById('img-filter').style.transform = "rotate(0deg)";
    document.getElementById('img-filter2').style.transform = "rotate(0deg)";
    document.getElementById('img-filter3').style.transform = "rotate(0deg)";
    document.getElementById('oreder_by_price_+').id = "oreder_by_price_-";
}

});
$('.btn-filter-watches').click(function(){

  try {
    document.getElementById('img-filter2').style.transform = "rotate(0deg)";
    document.getElementById('img-filter').style.transform = "rotate(0deg)";    
    document.getElementById('img-filter3').style.transform = "rotate(180deg)";
    document.getElementById('oreder_by_watches_-').id = "oreder_by_watches_+";
  }
  catch {
    document.getElementById('img-filter').style.transform = "rotate(0deg)";
    document.getElementById('img-filter2').style.transform = "rotate(0deg)";
    document.getElementById('img-filter3').style.transform = "rotate(0deg)";
    document.getElementById('oreder_by_watches_+').id = "oreder_by_watches_-";
}

});

$('.search-options').click(function(){

  $('.unvisible-search').toggleClass('unvisible-search-active');
});

$('.odobreno1').click(function(){

  $('.odobreno-box-element1').toggleClass('odobreno-box-element1-active');
    try{
  document.getElementById('go-more2').style.transform = "rotate(-0deg)";
  document.getElementById('go-more2').id = "go-more22";
}catch{
  document.getElementById('go-more22').style.transform = "rotate(-90deg)";
  document.getElementById('go-more22').id = "go-more2";
}
});
$('.elenemt_catalog').click(function(){
  for (let i = 0; i < 50; i++) {
    $('.' + String(i) + '_category_id').css({'display': 'none'})
  }
  $('.' + String(this.id) + '_category_id').css({'display': 'block'})
});
