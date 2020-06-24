function preview_filler() {
    var title = $('input[name="title"]')[0];
    var an_title = $('.pushesContentTitleAndroid')[0];
    var ip_title = $('.pushesContentTitleIphone')[0];
    an_title.innerText = title.value;
    ip_title.innerText = title.value;

    $('input[name="title"]').keyup(function(){
        an_title.innerText = title.value;
        ip_title.innerText = title.value;
    });


    var text = $('textarea[name="text"]')[0];
    var an_text = $('.pushesContentTextAndroid')[0];
    var ip_text = $('.pushesContentTextIphone')[0];
    an_text.innerText = text.value;
    ip_text.innerText = text.value;

    $('textarea[name="text"]').keyup(function(){
        an_text.innerText = text.value;
        ip_text.innerText = text.value;
    });


}

function defer(method) {
    if (window.jQuery)
        method();
    else
        setTimeout(function() { defer(method) }, 50);
}

defer(preview_filler);