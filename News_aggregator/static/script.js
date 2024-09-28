$(document).ready(function() {
    $('#search').on('keyup', debounce(function() {
        var keyword = $(this).val().toLowerCase();
        var hasResults = false;

        $('.article-card').filter(function() {
            const match = $(this).text().toLowerCase().indexOf(keyword) > -1;
            $(this).toggle(match);
            if (match) hasResults = true;
        });

        if (!hasResults) {
            $('#no-results').show();
        } else {
            $('#no-results').hide();
        }
    }, 300));
});


function debounce(func, delay) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

$(document).ready(function() {
    $('#search').on('keyup', debounce(function() {
        var keyword = $(this).val().toLowerCase();
        $('.article-card').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(keyword) > -1);
        });
    }, 300)); // Adjust the delay as needed
});


