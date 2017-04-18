function updateHaystack(input, needle) {
    var found = false;
    var i = 0;
    for (;i < params.length; i++) {
        var reg = new RegExp('(^|)(' + params[i] + ')(|$)','ig');
        if (reg.test(input)) {
            found = true;
            input = input.replace(reg, '$1<span id = "highlightText">$2</span>$3');
        }

    }
    if (found)
        return input;
    return null;
}

var AllItem = React.createClass({
    render: function () {
        var htmlString = '';
        htmlString = "<div class ='text-right'>"+ this.props.type + "</div>";
        var name = updateHaystack(this.props.name, 'cafe');
        if (name != null)
            htmlString += '<h1>' + name + '</h1><br>';
        else
            htmlString += '<h1>' + this.props.name + '</h1><br>';
        var currElement = this.props.element;
        var keys = Object.keys(currElement);

        var j = 0;

        //console.log(params);
        for (; j < keys.length; j++) {
            var chString = String(currElement[keys[j]]);
            if (chString != null) {
                chString = updateHaystack(chString, 1431, params);
                if (chString != null) {
                    htmlString += keys[j] + ": " + chString + "<br />";
                }
            }

        }
        return (
            <a href = {this.props.url}>
                <div className = "col-sm-12" id = "allGridItem" dangerouslySetInnerHTML={{__html: htmlString}}>
                </div>
            </a>
        );
    }
});


var AllList = React.createClass({
    render: function () {
        var count = page * perPage;
        //console.log(this.props.elements)
        var elements = this.props.elements.map(function (element, index) {
            count++;
            if (count <= JSONsections[0])
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.name}
                        url={"/Restaurants/" + element.id}
                        type="Restaurant"
                    />
                );
            else if (count <= JSONsections[1])
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.zipcode}
                        url={"/Locations/" + element.zipcode}
                        type="Location"
                    />
                );
            else if (count <= JSONsections[2])
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.food_type_display_name}
                        url={"/Food_Type/" + element.food_type}
                        type="Food Type"
                    />
                );
            else if (count <= JSONsections[3]) {
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.username}
                        url={"/Reviews/" + element.id}
                        type="Review"
                    />
                );}
            else if (count <= JSONsections[4])
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.name}
                        url={"/Restaurants/" + element.id}
                        type="Restaurant"
                    />
                );
            else if (count <= JSONsections[5])
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.zipcode}
                        url={"/Locations/" + element.zipcode}
                        type="Location"
                    />
                );
            else if (count <= JSONsections[6])
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.food_type_display_name}
                        url={"/Food_Types/" + element.food_type}
                        type="Food Type"
                    />
                );
            else
                return (
                    <AllItem
                        element = {element}
                        key={index}
                        name={element.username}
                        url={"/Reviews/" + element.id}
                        type="Review"
                    />
                );

        });

        var pageId = "";
        if (pages.length > 1) {
            pageId = "showPaginator";
        } else {
            pageId = "hidePaginator";
        }
        var showRes = URLparam;
        return (
            <div className = "row">
                <h1> Results for: {showRes} </h1>
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
var JSONsections = [0,0,0,0,0,0,0,0,0,0,0,0];
var pages = [];
var page = 0;
var perPage = 45;
var filters = {"Price" : [], "Rating": [], "FoodType": [], "Distance": ""};
var URLparam = '';
var params = [];

function changePage (e) {
    //console.log(e);
    if (e == "First") {
        if (page != 0) {
            page = 0;
        }
    } else if (e == "Prev") {
        if (page != 0) {
            page -= 1;
        }
    } else if (e == "Next") {
        if (page < pages.length - 1) {
            page += 1;
        }
    } else if (e == "Last") {
        if (page < pages.length - 1) {
            page = pages.length - 1;

        }
    }
    ReactDOM.render(<AllList elements={pages[page]} />, document.getElementById('allGrid'));
    $('html, body').animate({ scrollTop: 0 }, 'fast');
}


function loadAllGrid() {
    //console.log(elements);
    ReactDOM.render(<h2>Loading...</h2>, document.getElementById('allGrid'));
    getData();

}

function getData() {
    var url = "/API/All?search=";
    URLparam = getParameterByName('search');
    url += URLparam;
    params = URLparam.split(" ");
    //console.log("http://"+extractHostname(window.location.href)+"/API/Restaurants");
    $.getJSON( url, {
        tags: "All",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            //console.log(data);
            elements = data;
            pages = [];
            var currpage = [];
            // TODO: get the page number..

            var pageCount = 0;
            var currCount = 0;
            //console.log(elements);
            var i = 0;
            for (; i < elements.length; i++) {
                if (i > 0)
                    JSONsections[i] = Object.keys(elements[i]).length  + JSONsections[i-1];
                else
                    JSONsections[i] = Object.keys(elements[i]).length;

                var keys = Object.keys(elements[i]);
                //console.log(keys);
                var j = 0;
                for (; j < keys.length; j++) {
                    currpage.push(elements[i][keys[j]]);
                    currCount++;
                    if (currCount == perPage) {
                        currCount = 0;
                        pages.push(currpage);
                        currpage = [];
                        pageCount++;
                    }
                }
            }
            console.log(JSONsections);
            console.log(pages);
            // for (var i = 0; i < elements.length; i += 45) {
            //     pages[count] = elements.slice(i, i + 45);
            //     count += 1;
            // }
            //console.log(elements.length);
            //console.log("SIZE UP PAGES DOWN");
            //console.log(pages);

            // TODO: review if we need to keep this or remove above
            ReactDOM.render(<AllList elements={pages[0]} />, document.getElementById('allGrid'));
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
            ReactDOM.render(<RestList elements={pages[0]} />, document.getElementById('restGrid'));
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
            if (elements.length >0) {
                ReactDOM.render(<AllList elements={pages[0]}/>, document.getElementById('allGrid'));
            } else {
                ReactDOM.render(<h1>None Found..</h1>, document.getElementById('allGrid'));
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

// get parameters from url

function getParameterByName(name, url) {
    if (!url) {
        url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}



// start the display of elements
loadAllGrid();