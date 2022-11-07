import $ from "jquery";

$(function() {
    console.log( "ready!" );
    $(".menu__element").click(function () {
        $(".menu_screen").show()
    });

    $(".menu_screen__button").click(function () {
        $(".menu_screen").hide()
    });
})
