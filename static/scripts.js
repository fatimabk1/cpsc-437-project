$(function() {
    $("#director").typeahead({
        highlight: false,
        minLength: 3
    }, {
        async: true,
        display: function(suggestion) { return suggestion.name; },
        limit: 5,
        source: search,
        templates: {
            suggestion: function(data) {
                console.log(data);
                return "<div>" + data.name + "</div>";
            }
        }
    });
    $("#actor").typeahead({
        highlight: false,
        minLength: 3
    }, {
        async: true,
        display: function(suggestion) { return suggestion.name; },
        limit: 5,
        source: search,
        templates: {
            suggestion: function(data) {
                console.log(data);
                return "<div>" + data.name + "</div>";
            }
        }
    });
});

function search(query, callback, asyncCallback) {
    let parameters = {
        q: query
    }

    $.getJSON("/search", parameters, function(data) {
        asyncCallback(data);
    });
}