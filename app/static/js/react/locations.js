var LocationItem = React.createClass({
    render: function () {
        return (
            <a href = {"/Locations/" + this.props.id}>
                <div className = "col-sm-4" id = "locationItem">
                    <h1>{ this.props.name}</h1>
                    Restaurant Count: { this.props.numRest }<br />
                    Average Rating: { this.props.rating } <br />
                    Price Ranges: { this.props.Hprice + " - " + this.props.Lprice } <br />
                    Average Price: { this.props.avgPrice}/5

                </div>
            </a>
        );
    }
});

var LocationList = React.createClass({


    render: function () {
        var elements = this.props.elements.map(function (element, index) {
            return (
                <LocationItem
                    key={index}
                    name={element.zipcode}
                    rating={element.average_rating}
                    numRest={element.number_restaurants}
                    id={element.zipcode}
                    Lprice = {element.lowest_price}
                    Hprice = {element.highest_price}
                    avgPrice = {element.average_price}
                />
            );
        });

        var pageId = "";
        if (pages.length > 1) {
            pageId = "showPaginator";
        } else {
            pageId = "hidePaginator";
        }

        return (
            <div className = "row">
                <Paginator pageId = {pageId} location = "top"/>
                {elements}
                <Paginator pageId = {pageId} location = "bottom"/>
            </div>
        );
    }
});

var Paginator = React.createClass({
    render: function () {
        return (
            <div className={"col-sm-12 " + this.props.location} id = {this.props.pageId} >
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
var filters = {"avgPrice" : [], "avgRating": [], "FoodType": [], "Distance": ""};

function changePage (e) {
    //console.log(e);
    if (e == "First") {
        if (page != 0) {
            page = 0;
            ReactDOM.render(<LocationList elements={pages[0]} />, document.getElementById('locationGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Prev") {
        if (page != 0) {
            page -= 1;
            ReactDOM.render(<LocationList elements={pages[page]} />, document.getElementById('locationGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Next") {
        if (page < pages.length - 1) {
            page += 1;
            ReactDOM.render(<LocationList elements={pages[page]} />, document.getElementById('locationGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Last") {
        if (page < pages.length - 1) {
            page = pages.length - 1;
            ReactDOM.render(<LocationList elements={pages[page]} />, document.getElementById('locationGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    }
}


function loadLocationGrid() {
    //console.log(elements);
    ReactDOM.render(<h2>Loading...</h2>, document.getElementById('locationGrid'));
    getData();
}

function getData() {
    var url = "/API/Locations";
    //console.log("http://"+extractHostname(window.location.href)+"/API/Restaurants");
    $.getJSON( url, {
        tags: "locations",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            //console.log(data);
            elements = data;
            pages = [];

            // TODO: get the page number..

            var count = 0;
            for (var i = 0; i < elements.length; i += 45) {
                pages[count] = elements.slice(i, i + 45);
                count += 1;
            }
            //console.log(elements.length);
            //console.log("SIZE UP PAGES DOWN");
            //console.log(pages);

            // TODO: review if we need to keep this or remove above
            if (elements.length >0) {
                ReactDOM.render(<LocationList elements={pages[0]}/>, document.getElementById('locationGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('locationGrid'));
            }
        });

}

function sortGrid(e) {
    //getData();
    var sortBy = e.options[e.selectedIndex].value.split("-");
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Locations?sortby=" + sortBy[0].toLowerCase();
    if (filters["avgPrice"].length > 0) {
        url += "&avgprice=";
        filters["avgPrice"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    if (filters["avgRating"].length > 0) {
        url += "&avgrating=";
        filters["avgRating"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    if (filters["FoodType"].length > 0) {
        url += "&foodtype=";
        filters["FoodType"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    $.getJSON( url, {
        tags: "locations",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            console.log(data);
            elements = data;
            pages = [];
            page = 0;
            // TODO: get the page number..
            if (sortBy[1] == "H") {
                elements.reverse();
            }
            var count = 0;
            for (var i = 0; i < elements.length; i += 45) {
                pages[count] = elements.slice(i, i + 45);
                count += 1;
            }
            //console.log(elements.length);
            //console.log("SIZE UP PAGES DOWN");
            //console.log(pages);
            //console.log(sortBy[1]);
            // TODO: review if we need to keep this or remove above
            if (elements.length >0) {
                ReactDOM.render(<LocationList elements={pages[0]}/>, document.getElementById('locationGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('locationGrid'));
            }
        });
}

function getFilters() {
    var e = document.getElementById("sortOptions");
    var sortBy = e.options[e.selectedIndex].value.split("-");
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Locations?sortby=" + sortBy[0].toLowerCase();
    if (filters["avgPrice"].length > 0) {
        url += "&avgprice=";
        filters["avgPrice"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    if (filters["avgRating"].length > 0) {
        url += "&avgrating=";
        filters["avgRating"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    if (filters["FoodType"].length > 0) {
        url += "&foodtype=";
        filters["FoodType"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    console.log(url);
    $.getJSON( url, {
        tags: "locations",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            console.log(data);
            elements = data;
            pages = [];
            page = 0;
            // TODO: get the page number..
            if (sortBy[1] == "H") {
                elements.reverse();
            }
            var count = 0;
            for (var i = 0; i < elements.length; i += 45) {
                pages[count] = elements.slice(i, i + 45);
                count += 1;
            }
            //console.log(elements.length);
            //console.log("SIZE UP PAGES DOWN");
            //console.log(pages);
            //console.log(sortBy[1]);
            // TODO: review if we need to keep this or remove above
            if (elements.length >0) {
                ReactDOM.render(<LocationList elements={pages[0]}/>, document.getElementById('locationGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('locationGrid'));
            }
        });
}

function filterGrid() {
    getFilters();
}

function addFilter(e) {
    console.log(e);
    if (e[2]) {
        filters[e[0]].push(e[1]);
    } else {
        var i = filters[e[0]].indexOf(e[1]);
        filters[e[0]].splice(i, 1);
    }
    filters[e[0]].sort();
    console.log(filters);
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
loadLocationGrid();