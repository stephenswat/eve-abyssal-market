function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $("[name=csrfmiddlewaretoken]").val());
        }
    }
});

function open_contract(cid) {
    $.ajax({
        type: "POST",
        url: "/view_contract",
        data: { contract_id: cid }
    });
}

clipboard = new ClipboardJS('.btn-copy-contract-link');

$('.btn-open-contract').tooltip({
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
