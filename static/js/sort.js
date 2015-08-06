/**
 * Created by evgen on 6.8.15.
 */
 function sortab() {
    $(".sortable-img").sortable({
            over: function () {
                removeIntent = false
            },
            out: function () {
                removeIntent = true
            }
        }
    );
}