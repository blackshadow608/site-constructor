window.onload = ->
  if $('.page-select').length
    $('.page-select:first').addClass('curr_page')
    load_page()

$('.btn').mousedown ->
  request()
$('body').on 'click', '.page-select', ->
  request()
  $('.page-select').removeClass('curr_page')
  $('.for-padding').children().remove()
  $(this).addClass('curr_page')
  load_page()

request = ->
  id_curr_pag = $('.curr_page').attr("id_page")
  conten = ""
  $.each $('.for-padding').children(), (index, val) ->
    conten += val.outerHTML
  $.ajax
    url: "/editor/"+$('h2').attr("id_project")+'/'
    type: "POST"
    data:
      'id_page':id_curr_pag
      'content': conten
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    async:false
    success:->
    error: ->
      alert 'gyjudvasf'

load_page = ->
  id = $('.curr_page').attr("id_page")
  $.ajax
    url:"/editor/"+$('h2').attr("id_project")+'/'
    type:"POST"
    data:
      'id_return_page':id
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    async:false
    success:(data)->
      $('.for-padding').append(data.page)
      sortab()

