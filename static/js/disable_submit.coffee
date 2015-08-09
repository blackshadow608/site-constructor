$('form').submit ->
  $('[type="submit"]', $(this)).attr('disabled', 'disabled');
