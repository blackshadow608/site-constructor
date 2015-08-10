/**
 * Created by evgen on 8.8.15.
 */
  $('.myform').submit(function(e) {
        this.submit();
        setTimeout(function() {
            window.location.href = '';
        }, 100);
        });
