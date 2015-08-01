    $(function() {
        $(".draggable-video").draggable({
            helper: "clone", connectToSortable: "#droppable",
            start: function (event, ui) {
                var clone = $(ui.helper);
                clone.addClass("xyi");


            },
            stop: function (event, ui) {
                url=prompt('youtube.com link');
                if(url) {
                    console.log(url);
                    var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
                    var match = url.match(regExp);
                    if (match && match[2].length == 11) {
                        url = match[2];
                        $(ui.helper).empty()
                        $(ui.helper).append('<iframe width="560" height="315"  src="https://www.youtube.com/embed/' + url + '" frameborder="0" allowfullscreen></iframe>')
                        $(ui.helper).removeClass('btn-primary')
                        $(ui.helper).css('height', 'auto')
                        $(ui.helper).css('width', '100%')
                    } else {
                        $(ui.helper).remove();
                    }
                }else{
                    $(ui.helper).remove();
                }


            }
        });
        $("#droppable").sortable({
            over: function () {
                removeIntent = false
            },
            out: function () {
                removeIntent = true
            },
            beforeStop: function (event, ui) {
                if (removeIntent == true) {
                    ui.item.remove()
                }
            }
        });
    });