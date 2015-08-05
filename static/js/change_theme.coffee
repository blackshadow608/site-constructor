$ ->
  if $('.dark').hasClass('is_check')
    $('.for-padding').addClass('dark')
  $('input.view_theme[type=radio]').click ->
    $('input.view_theme[type=radio]').removeClass('is_check')
    $(this).addClass('is_check')
    site = $('.for-padding')
    id= $('h2').attr("id_project")
    if $(this).hasClass('dark')
      site.addClass('dark')
      request(id,'True')
    else
      site.removeClass('dark')
      request(id,'False')

request = (id, is_dark)->
  $.ajax
    url: "/theme/"
    type: "GET"
    data:
      'proj_id': id
      'is_dark': is_dark
    success:(data) ->
    error: ->
      alert 'gyjudvasf'
