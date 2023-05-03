(function(jQuery) {
  "use strict";

  jQuery.fn.isInViewport = function() {
    let elementTop = jQuery(this).offset().top;
    let elementBottom = elementTop + jQuery(this).outerHeight();

    let viewportTop = jQuery(window).scrollTop();
    let viewportBottom = viewportTop + jQuery(window).height();

    return elementBottom > viewportTop && elementTop < viewportBottom;
  };

  jQuery(document).ready(function(e) {





      if(jQuery('.pq-section-title').length > 0)
      {
      jQuery('.pq-section-title').each(function() {
        // console.log(jQuery(this).data('high_text'));
        if (jQuery(this).data('high_text').length > 0) {
          var a1, a2, color, id, type;


          const annotate = RoughNotation.annotate;
          const annotationGroup = RoughNotation.annotationGroup;
         const $ = (t) => document.querySelector(t);
          if (jQuery(this).data('rough_color') != '') {
            color = jQuery(this).data('rough_color');
          } else {
            color = '#fd4a18';
          }
          if (jQuery(this).data('rough_type') != '') {
            type = jQuery(this).data('rough_type');
          } else {
            type = 'underline';
          }

          id = jQuery(this).attr('id');
          // console.log(id);
          const config = {
            type: type,
            color: color,
            padding: [-15,0,-15,0]
          };
          a1 = annotate($('#' + id + ' .last-word'), config);
          a2 = annotate($('#' + id + ' .last-word'), config);


            // console.log(jQuery(id));
          jQuery(window).scroll(function() {
            if (jQuery('#' + id).isInViewport() && !jQuery('#' + id).hasClass('added')) {
              var svg = jQuery('svg');
              jQuery('#' + id).addClass('added');
              a1.hide();
              a2.hide();
              a1.show(3000);
              a2.show(3000);
            }
          });
        }
      });
      }


  });
})(jQuery);