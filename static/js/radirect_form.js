/**
 * Created by evgen on 8.8.15.
 */
  $('form').submit(function(e) {
        this.submit();
        setTimeout(function() {
            window.location.href = '';
        }, 100);
        });