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
        data: { 
            contract_id: e.data('contract-id'),
            character_id: localStorage.getItem('selected_character')
        },
        success: function () {
            setTooltip(e, 'Opened!');
        },
        error: function () {
            setTooltip(e, 'Error!');
        },
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
    if (attr == 105) {
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

    if (contract === null) {
        return "-";
    }

    if (contract.price.isk > 0 && contract.price.plex > 0) {
        base += `<span class="price-field">${price_humanize_verbose(contract.price.isk)}</span> + <span class="plex-field">${contract.price.plex}</span>`;
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

function action_format(mod, logged_in, ids, names) {
    if (mod.contract !== null) {
        return `<div class="btn-group" role="group" aria-label="Basic example">
                    <button ${logged_in ? "" : "disabled"} class="btn btn-std-size btn-primary btn-open-contract-esi btn-open-contract" data-contract-id="${mod.contract.id}">ESI</button>
                    <button class="btn btn-std-size btn-primary btn-copy btn-copy-contract-link btn-open-contract" data-clipboard-text="<url=contract:30000142//${mod.contract.id}>Contract ${mod.contract.id}</url>">Link</button>
                    <button class="btn btn-std-size btn-primary btn-copy" data-clipboard-text="${mod.pyfa}">Pyfa</button>
                    <!-- Similar Button -->
                    ` + generate_similar_button(mod, ids, names) + `
                </div>`
    } else {
        return `<div class="btn-group" role="group" aria-label="Basic example">
                    <button disabled class="btn btn-std-size btn-primary btn-open-contract-esi btn-open-contract" data-contract-id="">ESI</button>
                    <button disabled class="btn btn-std-size btn-primary btn-copy btn-copy-contract-link btn-open-contract" data-clipboard-text="">Link</button>
                    <button disabled class="btn btn-std-size btn-primary btn-copy" data-clipboard-text="">Pyfa</button>
                    <!-- Similar Button -->
                    ` + generate_similar_button(mod, ids, names) + `
                </div>`
    }

}

function action_format_non_contract(mod, ids, names) {
    return `<div class="btn-group" role="group" aria-label="Basic example">
                <button class="btn btn-std-size btn-primary btn-copy" data-clipboard-text="${mod.pyfa}">Pyfa</button>
                <!-- Similar Button -->
                ` + generate_similar_button(mod, ids, names) + `
                <!-- DEBUG -->
                <button class="btn btn-std-size btn-primary btn-sell">Sell</button>
            </div>`
}

function generate_similar_button(mod, ids, names) {
    // There's probably a better way to do this, but I'm too lazy to figure it out.
    output = `
    <div
        style="margin: 0; padding: 0;"
        class="btn btn-primary"
    >
        <button
            style="margin-right: 0; padding-right: 0;"
            class="btn btn-primary btn-similar-mods"
            data-id="${mod.id}"
        >
            Similar
        </button>
        <a
            style="margin-left: 0; padding-left: 0; background-color: transparent; border: transparent;"
            class="btn btn-primary"
            data-bs-toggle="dropdown"
            data-bs-auto-close="outside">
            <i class="fa fa-caret-down" aria-hidden="true"></i>
        </a>
        <div class="dropdown-menu" id="similar_form" style="padding: 15px; margin 15px; z-index: 100; position:relative;">
            <input id="${mod.id}_percent_range" type="number" min="0" max="100" value="15">
            <label for="${mod.id}_percent_range">&nbsp;Percent Range</label>`
    for (let i = 0; i < ids.length; i++)
    {
        let id = ids[i];
        let name = names[i];
        output += `
        <span>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="${mod.id}_${id}_check" checked>
                <label class="form-check-label" for="${mod.id}_${id}_check">
                <img src="/static/img/attributes/${id}.png" title="${name}">&nbsp;${name}
                </label>
            </div>
        </span>
        `
    }
    output +=
    `   <div>
            <button
                class="btn btn-primary btn-small mx-auto d-block btn-similar-mods"
                data-id="${mod.id}"
            >
                Submit
            </button>
        </div>
    </div>
    </div>`

    return output;
}

function attr_format(attr, data) {
    base = `<span class='attr-${attr} attr-cell'>${data.real_value.toFixed(get_precision(attr))}</span>`;

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
    } else if (attr_id == 204) {
        return 4;
    } else {
        return 1;
    }
}

function attribute_format(attrs) {
    var list = "";

    for (var a in attrs) {
        var rating = "";

        if (!attrs[a].display) {
            continue;
        }

        if (attrs[a].rating !== null && display_rating(a)) {
            if (attrs[a].rating > 0) {
                rating = ` <span class="module-rating text-success">+${attrs[a].rating}</span>`;
            } else if (attrs[a].rating == 0) {
                rating = ` <span class="module-rating text-warning">±${attrs[a].rating}</span>`;
            } else {
                rating = ` <span class="module-rating text-danger">${attrs[a].rating}</span>`;
            }
        }

        list += `<div class="col-12 col-md-4">
                    <img src="/static/img/attributes/${a}.png">
                    ${attrs[a].real_value.toFixed(get_precision(a))} ${attrs[a].unit} ${rating}
                 </div>`;
    }

    return `<div class="row">${list}</div>`
}

document.addEventListener('DOMContentLoaded', (event) => { update_mode(); });
