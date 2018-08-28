function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $("[name=csrfmiddlewaretoken]").val());
        }
    },
});

function open_contract(e) {
    $.ajax({
        type: "POST",
        url: "/view_contract",
        data: { contract_id: e.data('contract-id') },
        success: function () {
            setTooltip(e, 'Opened!');
        }
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
    setTimeout(function () {
        $(btn).tooltip('hide');
    }, 1000);
}

clipboard.on('success', function (e) {
    setTooltip(e.trigger, 'Copied!');
});

$(".btn-open-contract-esi").click(function() {
    open_contract($(this));
});
