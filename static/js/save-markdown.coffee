
$ ->
  $('textarea').autoGrow()
  $('#droppable').on 'keyup','.markdown-field',->
    $(this).text $(this).val()
    $('textarea').autoGrow()

