//init editor-like styling for code blocks
hljs.initHighlightingOnLoad();


(function($) {
  "use strict";
  var commentMgr = {
    addForm: function(_this){
      $('#reply-form input[name=parent_id]').val(_this.attr('rel'));
      $('#reply-form').insertAfter( _this.parent() );
      $('#reply-form').removeClass('hidden');
      $.fn.matchHeight._update();
      $.fn.matchHeight._throttle = 1;
      $.fn.matchHeight._maintainScroll = true;
    }
  };

  var helper = {

    // Set arrow to top (dropdown arrows)
    arrowUp: function(el){
      el.find('i.fa').removeClass('fa-chevron-down');
      el.find('i.fa').addClass('fa-chevron-up');
    },

    // Set arrow to down (dropdown arrows)
    arrowDown: function(el){
      el.find('i.fa').removeClass('fa-chevron-up');
      el.find('i.fa').addClass('fa-chevron-down');
    },

    windowScrollUp: function(){
      window.scrollTo(window.scrollX, window.scrollY - 500);
      console.log('yes');
    },
    truncate: function(target){
      $(target).dotdotdot({
        ellipsis	: '... ',
        watch		: true
      });
    }

  };

  /* Submit comment on enter */
  $(".commentButton").click(function(event) {
      event.preventDefault();
      $('.commentButton').attr('disabled','disabled');
      $(this).parents("form").submit();

  });

  /* Display reply form */
  $(".reply").click(function(event){
    event.preventDefault();
    commentMgr.addForm($(this));
  });

  /* Comments hide/show */
  $("#comments-control").on('click',function(event){
    event.preventDefault();
     var _this = $(this);
     var _commentswrap = $('#comments-wrap');
     if(_commentswrap.hasClass('in')){ // if comments displayed
       _commentswrap.removeClass('in');
       helper.arrowDown(_this);
     }else{ //if comments hidden
       _commentswrap.addClass('in');
       helper.arrowUp(_this);
     }
  });

  /* Download button */
  $('.download-source').on('click',function(){
    var entryId = $(this).attr('data-entry-id');
    $.get( "/_sections/downloads.increment.count/" + entryId , function() {
        console.log( "Load was performed." );
      });
  });

    $(document).ready(function () {
        var $textareas = jQuery('#comments-wrap textarea');

        // set init (default) state
        $textareas.data('x', $textareas.outerWidth());
        $textareas.data('y', $textareas.outerHeight());

        $textareas.mouseup(function () {

            var $this = jQuery(this);

            if ($this.outerWidth() != $this.data('x') || $this.outerHeight() != $this.data('y')) {
                $.fn.matchHeight._update();
                $.fn.matchHeight._throttle = 1;
                $.fn.matchHeight._maintainScroll = true;
            }

            // set new height/width
            $this.data('x', $this.outerWidth());
            $this.data('y', $this.outerHeight());
        });
    });

  $(window).load(function(){
    if(window.location.hash && location.hash == '#file') {
      /* anchor links need to go some pixels above where its linked to */
      window.scrollTo(window.scrollX, window.scrollY - 150);
    }
    helper.truncate('.truncated');
  });



})(jQuery);
