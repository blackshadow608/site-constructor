$('img').click ->
  src_img=$(this).attr('src')
  target=$(".img-click")
  target.empty()
  target.append('<img class="draggable-img" src="'+src_img+'"style="width:200px;height:150px" >')
  $(".draggable-img").draggable
    helper: "clone"
    connectToSortable: ".sortable-img"
