function open_contract(cid, csrf) {
    $.ajax({
        type: "POST",
        url: "/view_contract",
        data: { contract_id: cid, csrfmiddlewaretoken: csrf }
    });
}

clipboard = new ClipboardJS('.btn-copy-contract-link');

$('button').tooltip({
    trigger: 'click',
    placement: 'top'
});


function setTooltip(btn, message) {
    $(btn).tooltip('hide')
        .attr('data-original-title', message)
        .tooltip('show');
}

function hideTooltip(btn) {
    setTimeout(function () {
        $(btn).tooltip('hide');
    }, 1000);
}

clipboard.on('success', function (e) {
    setTooltip(e.trigger, 'Copied!');
    hideTooltip(e.trigger);
});
