function open_contract(cid, csrf) {
    $.ajax({
        type: "POST",
        url: "/view_contract",
        data: { contract_id: cid, csrfmiddlewaretoken: csrf }
    });
}
