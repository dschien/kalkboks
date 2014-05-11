var globals = {
    urls: {
        cagr: 'api/cagr'
    }
}


function cagr(base, rate, years) {
    console.log('server calculates growth');
    var self = this;
    var posting = $.post(
        globals.urls.cagr,
        {"base": base, 'rate': rate, 'years': years}
    );
    posting.done(function (data) {
        $('#result').val(data.result);
        // create a clone of the array
        drawChart(data.series.slice(0))
        printValues(data.series)
    });
    posting.fail(function (data) {
        var reason = JSON.parse(data.responseText).result;
        console.log('failed to login:' + JSON.stringify(data));
        alert(reason);
    });
    return posting;
}

function drawChart(values) {

    values.unshift('series values')
    var chart = c3.generate({
        data: {
            columns: [
                values
            ],
            type: 'spline'
        }});

    $('h1.hidden').removeClass('hidden')
}


function printValues(values) {
    // transpose the array
    var dataSet = _.zip.apply(_, [d3.range(values.length), values ])

    $('#values').html('<table cellpadding="0" cellspacing="0" border="0" class="display" id="example"></table>');

    $('#example').dataTable({
        "data": dataSet,
        "columns": [
            { "title": "Year" },
            { "title": "Value" },
        ]
    });
}
// parsley
var validateFront = function () {
    if (true === $('#cagrForm').parsley().isValid()) {
//        $('.bs-callout-info').removeClass('hidden');
        $('.bs-callout-warning').addClass('hidden');
    } else {
//        $('.bs-callout-info').addClass('hidden');
        $('.bs-callout-warning').removeClass('hidden');
    }
};


$('#goBtn').click(function () {

    var cagrForm = $("#cagrForm");
    var isValid = cagrForm.parsley().validate();
    validateFront();
    if (isValid) {
        cagr($('#baseVal').val(), $('#rate').val(), $('#years').val())
    }
})

$(document).ready(function () {
    $.listen('parsley:field:validate', function () {
        validateFront();
    });
});