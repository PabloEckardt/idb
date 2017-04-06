var ReviewItem = React.createClass({
    render: function () {
        return (
            <a href = {"/Reviews/" + this.props.id}>
                <div className = "col-sm-4" id = "reviewGrid">
                    <div className="thumbnail_container">
                        <div className="thumbnail">
                            <img className="aboutPic" src = {this.props.img_url} />
                        </div>
                    </div>
                    <h1>{ this.props.name}</h1>

                </div>
            </a>
        );
    }
});

var ReviewList = React.createClass({


    render: function () {
        var elements = this.props.elements.map(function (element, index) {
            return (
                <ReviewItem
                    key={index}
                    name={element.username}
                    img_url={element.profile_picture_url}
                    restaurant = {element.restaurant_id}
                    rating = {element.rating}
                    date = {element.date}
                    id = {element.id}
                />
            );
        });

        var pageId = "";
        if (pages.length > 0) {
            pageId = "showPaginator";
        } else {
            pageId = "hidePaginator";
        }

        return (
            <div className = "row">
                <Paginator pageId = {pageId} />
                {elements}
                <Paginator pageId = {pageId} />
            </div>
        );
    }
});

var Paginator = React.createClass({
    render: function () {
        return (
            <div className="col-sm-12" id = {this.props.pageId} >
                <a href = "javascript:changePage('First')">&lt;&lt;First</a>&nbsp;&nbsp;
                <a href = "javascript:changePage('Prev')">&lt;&lt;Prev</a>
                &nbsp;&nbsp;Page: {page + 1} of {pages.length} &nbsp;&nbsp;
                <a href = "javascript:changePage('Next')">Next&gt;&gt;</a>&nbsp;&nbsp;
                <a href = "javascript:changePage('Last')">Last&gt;&gt;</a>
            </div>
        );
    }

});

// Could come from an API, LocalStorage, another component, etc...
var elements = [];
var pages = [];
var page = 0;

function changePage (e) {
    console.log(e);
    if (e == "First") {
        if (page != 0) {
            page = 0;
            ReactDOM.render(<ReviewList elements={pages[0]} />, document.getElementById('reviewGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Prev") {
        if (page != 0) {
            page -= 1;
            ReactDOM.render(<ReviewList elements={pages[page]} />, document.getElementById('reviewGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Next") {
        if (page < pages.length - 1) {
            page += 1;
            ReactDOM.render(<ReviewList elements={pages[page]} />, document.getElementById('reviewGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Last") {
        if (page < pages.length - 1) {
            page = pages.length - 1;
            ReactDOM.render(<ReviewList elements={pages[page]} />, document.getElementById('reviewGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    }
}


function loadReviewGrid() {
    console.log(elements);
    ReactDOM.render(<h2>Loading...</h2>, document.getElementById('reviewGrid'));
    getData();
}

function getData() {
    var url = "/API/Reviews";
    //console.log("http://"+extractHostname(window.location.href)+"/API/Restaurants");
    $.getJSON( url, {
        tags: "Reviews",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            console.log(data);
            elements = data;
            pages = [];

            // TODO: get the page number..

            var count = 0;
            for (var i = 0; i < elements.length; i += 45) {
                pages[count] = elements.slice(i, i + 45);
                count += 1;
            }
            console.log(elements.length);
            console.log("SIZE UP PAGES DOWN");
            console.log(pages);

            // TODO: review if we need to keep this or remove above
            ReactDOM.render(<ReviewList elements={pages[0]} />, document.getElementById('reviewGrid'));
        });

}

function sortGrid(e) {
    //getData();
    var sortBy = e.options[e.selectedIndex].value;
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Reviews?sortby=" + sortBy.toLowerCase();
    $.getJSON( url, {
        tags: "Reviews",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            console.log(data);
            elements = data;
            pages = [];
            page = 0;
            // TODO: get the page number..

            var count = 0;
            for (var i = 0; i < elements.length; i += 45) {
                pages[count] = elements.slice(i, i + 45);
                count += 1;
            }
            console.log(elements.length);
            console.log("SIZE UP PAGES DOWN");
            console.log(pages);
            // TODO: review if we need to keep this or remove above
            ReactDOM.render(<ReviewList elements={pages[0]} />, document.getElementById('reviewGrid'));
        });
}

function getFilters() {

}

function filterGrid() {

}

function extractHostname(url) {
    var hostname;
    //find & remove protocol (http, ftp, etc.) and get the hostname
    if (url.indexOf("://") > -1) {
        hostname = url.split('/')[2];
    }
    else {
        hostname = url.split('/')[0];
    }

    //find & remove port number
    // hostname = hostname.split(':')[0];

    return hostname;
}



// start the display of elements
loadReviewGrid();
