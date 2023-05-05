jQuery('.pq-section-title').each(function () {

    var high_text = jQuery(this).data('high_text');
    var text = jQuery(this).text().split(' ');
    var new_text = '';

    var main_text = jQuery(this).data('title_text');
    var regEx = new RegExp(high_text, "i");
    // console.log(high_text);
    // console.log(text);
    // console.log(main_text);

    result = main_text.match(regEx);
    console.log(result);

    result[0] = result[0].replace(/\s/g, '');
    // console.log(result[0]);
    text.forEach(function (val) {
        if (val == result[0]) {
            new_text += '<span class="last-word"> ' + val + ' </span>';
        }
        else {
            new_text += ' ' + val + ' ';
        }
    });
    jQuery(this).html(function () {
        return new_text;
    });

    //var last = text.pop();
    //console.log(text);

});
jQuery('pq-section-title').html(function () {
    var text = jQuery(this).text().split(' ');

    var last = text.pop();

    //console.log(' <span class="last-word">'+last+'</span>');

    //return text.join(" ") + (text.length > 0 ? ' <span class="last-word">'+last+'</span>' : last);  
});