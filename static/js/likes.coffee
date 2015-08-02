$ ->
  $('body').on 'click','.glyphicon',->
    numOfLike=$(this).parent().children('text')
    $.ajax
      url:"/like/"
      type:"GET"
      data:
        'id_rating':$(this).parent().parent().attr('id_rating')
      success: (data) ->
        numOfLike.text(data.response) if data.response != 'hui'
