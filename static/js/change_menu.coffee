$ ->
  $('input.view_menu[type=radio]').click ->
    id= $('h2').attr("id_project")
    if $(this).hasClass('horizontal')
      request(id,'True')
    else
      request(id,'False')

request = (id, is_horizontal)->
  $.ajax
    url: "/menu/"
    type: "GET"
    data:
      'proj_id': id
      'is_horizontal': is_horizontal
    success:(data) ->
    error: ->
      alert 'gyjudvasf'
