var RestItem = React.createClass({
    render: function () {
        return (
            <a href = {"/Restaurants/" + this.props.id}>
                <div className = "col-sm-4" id = "restaurantGrid">
                    <img src = {this.props.img_url} className="img-responsive"/>
                    <h1>{ this.props.name}</h1>
                    Address: { this.props.address }<br />
                    Rating: { this.props.rating } <br />
                    Food Type: { this.props.foodtypeD } <br />
                    Price: { this.props.price }

                </div>
            </a>
        );
    }
});

var RestList = React.createClass({


    render: function () {
        var elements = this.props.elements.map(function (element, index) {
            return (
                <RestItem
                    key={index}
                    name={element.name}
                    rating={element.rating}
                    address={element.address}
                    foodtype={element.food_type}
                    foodtypeD = {element.food_type_disp}
                    img_url={element.img_url}
                    id={element.id}
                    price = {element.price}
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
var filters = {"Price" : [], "Rating": [], "FoodType": [], "Distance": ""};

function changePage (e) {
    //console.log(e);
    if (e == "First") {
        if (page != 0) {
            page = 0;
            ReactDOM.render(<RestList elements={pages[0]} />, document.getElementById('restGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Prev") {
        if (page != 0) {
            page -= 1;
            ReactDOM.render(<RestList elements={pages[page]} />, document.getElementById('restGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Next") {
        if (page < pages.length - 1) {
            page += 1;
            ReactDOM.render(<RestList elements={pages[page]} />, document.getElementById('restGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    } else if (e == "Last") {
        if (page < pages.length - 1) {
            page = pages.length - 1;
            ReactDOM.render(<RestList elements={pages[page]} />, document.getElementById('restGrid'));
            $('html, body').animate({ scrollTop: 0 }, 'fast');
        }
    }
}


function loadRestGrid() {
    //console.log(elements);
    ReactDOM.render(<h2>Loading...</h2>, document.getElementById('restGrid'));
    getData();
}

function getData() {
    var url = "/API/Restaurants";
    //console.log("http://"+extractHostname(window.location.href)+"/API/Restaurants");
    $.getJSON( url, {
        tags: "restaurants",
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
            // console.log(pages);

            // TODO: review if we need to keep this or remove above
            if (elements.length > 0) {
                ReactDOM.render(<RestList elements={pages[0]}/>, document.getElementById('restGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('restGrid'));
            }
        });

}

function sortGrid(e) {
    //getData();
    var sortBy = e.options[e.selectedIndex].value.split("-");
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Restaurants?sortby=" + sortBy[0].toLowerCase();
    if (filters["Price"].length > 0) {
        url += "&price=";
        filters["Price"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    if (filters["Rating"].length > 0) {
        url += "&rating=";
        filters["Rating"].forEach(function(element) {
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
        tags: "restaurants",
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
            if (elements.length > 0) {
                ReactDOM.render(<RestList elements={pages[0]}/>, document.getElementById('restGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('restGrid'));
            }
        });
}

function getFilters() {
    var e = document.getElementById("sortOptions");
    var sortBy = e.options[e.selectedIndex].value.split("-");
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Restaurants?sortby=" + sortBy[0].toLowerCase();
    if (filters["Price"].length > 0) {
        url += "&price=";
        filters["Price"].forEach(function(element) {
            url += element + ",";
        });
        url = url.substring(0, url.length-1);
    }
    if (filters["Rating"].length > 0) {
        url += "&rating=";
        filters["Rating"].forEach(function(element) {
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
        tags: "restaurants",
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
            if (elements.length > 0) {
                ReactDOM.render(<RestList elements={pages[0]}/>, document.getElementById('restGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('restGrid'));
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
loadRestGrid();