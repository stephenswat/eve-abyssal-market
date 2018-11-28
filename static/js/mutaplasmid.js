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
        url: "/view_contract/",
        data: { contract_id: e.data('contract-id') },
        success: function () {
            setTooltip(e, 'Opened!');
        }
    });
}

clipboard = new ClipboardJS('.btn-copy');

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

function display_rating(attr) {
    if (attr == 1255) {
        return false;
    } else if (attr == 105) {
        return false;
    } else {
        return true;
    }
}

function initializeEsiButtons() {
    $(".btn-open-contract-esi").click(function() {
        open_contract($(this));
    });
}

function price_format(contract) {
    base = ""

    if (contract.price.isk > 0 && contract.price.plex > 0) {
        base += `<span class="price-field">${price_humanize_verbose(contract.price.isk)}</span> + <span class="plex-field">${price.plex}</span>`;
    } else if (contract.price.plex > 0) {
        base += `<span class="plex-field">${contract.price.plex}</span>`;
    } else {
        base += `<span class="price-field">${price_humanize_verbose(contract.price.isk)}</span>`;
    }

    if (contract.multi_item) {
        base += `<span class="annotation-multi-item text-muted" title="This contract includes other items."></span>`
    }

    if (contract.auction) {
        base += `<span class="annotation-auction text-muted" title="This is an auction."></span>`
    }

    return base;
}

function open_format(mod, logged_in) {
    return `<div class="btn-group" role="group" aria-label="Basic example">
                <button ${logged_in ? "" : "disabled"} class="btn btn-std-size btn-primary btn-open-contract-esi btn-open-contract" data-contract-id="${mod.contract.id}">ESI</button>
                <button class="btn btn-std-size btn-primary btn-copy btn-copy-contract-link btn-open-contract" data-clipboard-text="<url=contract:30000142//${mod.contract.id}>Contract ${mod.contract.id}</url>">Link</button>
                <button class="btn btn-std-size btn-primary btn-copy" data-clipboard-text="${mod.pyfa}">Pyfa</button>
            </div>`
}

function attr_format(attr, data) {
    base = `<span class='attr-${attr}'>${data.real_value.toFixed(get_precision(attr))}</span>`;

    if (data.rating != null && display_rating(attr)) {
        if (data.rating > 0) {
            base += ` <span class="module-rating text-success">+${data.rating}</span>`;
        } else if (data.rating == 0) {
            base += ` <span class="module-rating text-warning">±${data.rating}</span>`;
        } else {
            base += ` <span class="module-rating text-danger">${data.rating}</span>`;
        }
    }

    return base;
}

function price_humanize_verbose(price) {
    if (price >= 1000000000) {
        return (price / 1000000000).toFixed(1) + " billion"
    } else {
        return (price / 1000000).toFixed(1) + " million"
    }
}

function get_precision(attr_id) {
    if (attr_id == 64) {
        return 3;
    } else if (attr_id == "price") {
        return 0;
    } else if (attr_id == 105) {
        return 0;
    } else if (attr_id == 54) {
        return 0;
    } else {
        return 1;
    }
}
