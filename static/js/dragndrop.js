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
                                $(ui.helper).append('<iframe width="50%" height="auto"  src="https://www.youtube.com/embed/' + url + '" frameborder="0" allowfullscreen></iframe>');
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
            $(ui.helper).append('    <div class="navbar-right" style="font-size: 17px;"><span class="btn glyphicon glyphicon-thumbs-up"style="font-size: 20px;">'+
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

    $(".draggable-gallery").draggable({
        helper: "clone", connectToSortable: "#droppable",
        start: function (event, ui) {
            var clone = $(ui.helper);
            clone.addClass("xyi");
        },
        stop: function (event, ui) {
            $(ui.helper).empty();
            $(ui.helper).removeClass('btn-primary');
            $(ui.helper).removeClass('btn');
            $(ui.helper).addClass('container');
            //$(ui.helper).css('min-height', '200px');
            $(ui.helper).css('height', 'auto');
            $(ui.helper).css('padding-bottom', '20px');
            $(ui.helper).css('width', '100%');
            $(ui.helper).append('<div class="col-md-12 btn-group sortable-img well well-sm"></div>');

            $('.sortable-img').sortable({
                connectWith:'img',
                over: function () {
                    removeIntent = false
                },
                out: function () {
                    removeIntent = true;
                }

            });

        }
    });

    $(".draggable-img").draggable({
        helper: "clone", connectToSortable: ".sortable-img",
        start: function (event, ui) {
            var clone = $(ui.helper);
        },
        stop: function (event, ui) {
            //$(ui.helper).empty();


        }
    });

    $(".sortable-img").sortable({
            over: function () {
                removeIntent = false
            },
            out: function () {
                removeIntent = true
            },
            beforeStop: function (event, ui) {
                ui.item.remove()
            }
        }
    );
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
        },
    });
});