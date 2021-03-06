var ReviewItem = React.createClass({
    render: function () {
        return (
            <a href = {"/Reviews/" + this.props.id}>
                <div className = "col-sm-4" id = "reviewItem">
                    <div className="review_pic">
                            <img className="aboutPic img-responsive" src = {this.props.img_url} />
                    </div>
                    <h1>{ this.props.name}</h1>
                    Date of Review: {this.props.date} <br />
                    Restaurant: {this.props.restaurant} <br />
                    Rating Given: {this.props.rating} <br />
                    Food Type Reviewed: {this.props.foodtype}

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
                    restaurant = {element.restaurant_name}
                    rating = {element.rating}
                    date = {element.date}
                    id = {element.id}
                    foodtype = {element.food_type_disp}
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
var filters = {"Img" : [], "Rating": [], "FoodType": [], "Distance": ""};

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
            if (elements.length >0) {
                ReactDOM.render(<ReviewList elements={pages[0]}/>, document.getElementById('reviewGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('reviewGrid'));
            }
        });

}

function sortGrid(e) {
    //getData();
    var sortBy = e.options[e.selectedIndex].value.split("-");
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Reviews?sortby=" + sortBy[0].toLowerCase();
    if (filters["Img"].length > 0) {
        url += "&hasimg=";
        filters["Img"].forEach(function(element) {
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
            if (elements.length >0) {
                ReactDOM.render(<ReviewList elements={pages[0]}/>, document.getElementById('reviewGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('reviewGrid'));
            }
        });
}


function getFilters() {
    var e = document.getElementById("sortOptions");
    var sortBy = e.options[e.selectedIndex].value.split("-");
    console.log(e.options[e.selectedIndex].value);
    var url = "/API/Reviews?sortby=" + sortBy[0].toLowerCase();
    if (filters["Img"].length > 0) {
        url += "&hasimg=";
        filters["Img"].forEach(function(element) {
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
        tags: "reviews",
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
                ReactDOM.render(<ReviewList elements={pages[0]}/>, document.getElementById('reviewGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('reviewGrid'));
            }
        });
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



function filterGrid() {
    getFilters();
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
