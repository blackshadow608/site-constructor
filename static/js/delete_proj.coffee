$('.glyphicon').click ->
  id = $(this).parent().children('.proj_id').val()
  parent = $(this).parent()
  $.ajax
    url: "/my_projects/"
    type: "POST"
    data:
      'proj_id': id
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    success:(data) ->
      parent.remove()
    error: ->
      alert 'in delete_proj'
