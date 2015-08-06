$ ->
  $('body').on 'click', 'select', ->
    $('#select_lang_form').submit()
  $('body').on 'click', 'option', ->
    $('option').removeAttr('selected')
    $(this).attr('selected','selected')