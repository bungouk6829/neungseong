$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }
  selector = '#content_menu > ul > a:nth-child(2) > li'
  change_color(selector);

});

//new_information_post <form> 유효성 검사
function validate() {
       var re1 = /^[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]{1,10}$/;
       var re2 = /^[a-zA-Z0-9]{4,20}$/;
       var re3 = /^[0-9]{10,21}$/;
       var re4 = /^.{1,100}$/;
       var re5 = /^.{1,5000}$/;

       var author = document.getElementById("author");
       var password = document.getElementById("password");
       var phone_number = document.getElementById("phone_number");
       var title = document.getElementById("title");
       var text = document.getElementById("text");
       var file_1 = document.getElementById("file_1");
       var file_2 = document.getElementById("file_2");
       var file_3 = document.getElementById("file_3");
       var file_4 = document.getElementById("file_4");
       var file_5 = document.getElementById("file_5");

       if(!check(re1,author,"작성자는 한글로 1~10 자로만 가능합니다.")) {
           return false;
       }
       if(!check(re2,password,"비밀번호는 영문과 숫자로 4~20자로만 가능합니다.")) {
           return false;
       }
       if(!check(re3,phone_number,"전화번호는 10자리~20자의 숫자로만 가능합니다.\n\n('-'기호는 입력하지 않습니다.)")) {
           return false;
       }
       if(!check(re4,title,"문의제목은 1~100 자로만 가능합니다.")) {
           return false;
       }
       if(!check(re5,text,"문의내용은 1~5000 자로만 가능합니다.")) {
           return false;
       }

       alret("문의글 작성이 완료되었습니다.");
   }

function check(re, what, message) {
    if(re.test(what.value)) {
        return true;
    }
    alert(message);
    what.value = "";
    what.focus();
}
