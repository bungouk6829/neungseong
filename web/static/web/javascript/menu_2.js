$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

 href = window.location.href.replace("http://www.neungseong.com/","");

  if (href == "business"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }

  else if (href == "demolition"){
    selector = '#content_menu > ul > a:nth-child(2) > li'
    change_color(selector);
  }

  else if (href == "asbestos"){
    selector = '#content_menu > ul > a:nth-child(3) > li'
    change_color(selector);
  }

   else if (href == "waste"){
    selector = '#content_menu > ul > a:nth-child(4) > li'
    change_color(selector);
  }

   else if (href == "civil"){
    selector = '#content_menu > ul > a:nth-child(5) > li'
    change_color(selector);
  }

  else if (href == "major"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }



  $('.mg-link').magnificPopup({
       type: 'image',
       closeOnContentClick: true,
       closeBtnInside: true,
       fixedContentPos: true,
       image: {    verticalFit: true,
                   titleSrc: 'title',
                   titleSrc: function(item) {
                     return '<h3>' + item.el.find('img').attr('alt') + '</h3>' + item.el.attr('title');
                   }
              },
       gallery: {   enabled: true    }, // 좌우로 사진 돌려보기 생성
       zoom: {    enabled: true,   duration: 400    }
    });
});
