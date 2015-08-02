$(function() {

    $(".draggable-video").draggable({
        helper: "clone", connectToSortable: "#droppable",
        start: function (event, ui) {
            var clone = $(ui.helper);
            clone.addClass("xyi");
        },
        stop: function (event, ui) {
            var statesdemo = {
                state0: {
                    title: 'Video block',
                    html:'<label>Youtube link <input class="form-control" type="text" name="link" value=""></label><br />',
                    buttons: {OK: 1, Cancel:false },

                    submit:function(e,v,m,f){
                        var url=(f.link);
                        if(url) {
                            var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
                            var match = url.match(regExp);
                            if (match && match[2].length == 11) {
                                url = match[2];
                                $(ui.helper).empty();
                                $(ui.helper).append('<iframe width="560" height="315"  src="https://www.youtube.com/embed/' + url + '" frameborder="0" allowfullscreen></iframe>');
                                $(ui.helper).removeClass('btn-primary');
                                $(ui.helper).css('height', 'auto');
                                $(ui.helper).css('width', '100%');
                            } else {
                                $(ui.helper).remove();
                            }
                        }else{
                            $(ui.helper).remove();
                        }
                    },
                    close: function(e,v,m,f){$(ui.helper).remove()}
                }
            };
            $.prompt( statesdemo);
        }
    });

    $(".draggable-text").draggable({
        helper: "clone", connectToSortable: "#droppable",
        start: function (event, ui) {
            var clone = $(ui.helper);
            clone.addClass("xyi");
        },
        stop: function (event, ui) {
            $(ui.helper).empty();
            $(ui.helper).removeClass('btn-primary');
            $(ui.helper).removeClass('btn');
            $(ui.helper).css('height', 'auto');
            $(ui.helper).css('width', '100%');
            $(ui.helper).append('<textarea style="resize:vertical; width:95%" class="form-control markdown-field"></textarea>');
        }
    });

    $(".draggable-raiting").draggable({
        helper: "clone", connectToSortable: "#droppable",
        start: function (event, ui) {
            var clone = $(ui.helper);
            clone.addClass("xyi");
        },
        stop: function (event, ui) {
            $(ui.helper).empty();
            $(ui.helper).removeClass('btn-primary');
            $(ui.helper).removeClass('btn');
            $(ui.helper).css('height', '45px');
            $(ui.helper).css('width', '100%');
            $(ui.helper).append('    <div class="navbar-right  "><span class="btn glyphicon glyphicon-thumbs-up">'+
                '</span><text>0</text></div>');
            $.ajax({
                url: "/rating/",
                type:"GET",
                data:{"id_project_create_rating":$('h2').attr("id_project")},
                success:function(data){
                    if(data.response=='success'){
                         $(ui.helper).attr('id_rating', data.id_rating)
                    }
                }

            })
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
                if(ui.item.hasClass("draggable-raiting")){
                    $.ajax({
                        url: "/rating/",
                        type:"GET",
                        data:{"id_delete_rating":ui.item.attr('id_rating')},
                        success:function(data){
                        }

                    })
                }
                ui.item.remove()
            }
        }
    });
});