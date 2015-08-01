$ ->
  $('#droppable').on('keyup','.markdown-field',->
      $(this).text $(this).val())

