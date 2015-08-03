
$ ->
  if $('.dark').attr('is_check')
    alert 'asd'
  $('input').click ->
    $('input').removeAttr('is_check')
    $(this).attr('is_check','')
    site = $('.for-padding')
    if $(this).hasClass('dark')
      site.addClass('dark')

    else
      site.removeClass('dark')