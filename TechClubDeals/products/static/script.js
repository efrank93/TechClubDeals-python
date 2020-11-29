function enterSite() {
    $("#landing").css("transform", "translate(-200vw)");
    $("#dimmed-bg").css("visibility", "visible");
    $("#dimmed-bg").css("transform", "translate(0)");
    $("#above-fold").css("opacity", "1");
    $("#full-site").css("visibility", "visible");
    $("#full-site").css("overflow", "visible");
    $("#full-site").css("max-height", "auto");
}


$("#visible-section").mouseenter(function() { openForm(); });
$("#empty-section").mouseenter(function() { closeForm(); });
$("#form-section").mouseleave(function() { closeForm(); });