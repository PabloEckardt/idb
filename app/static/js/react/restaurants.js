var RestItem = React.createClass({
    render: function () {
        return (
            <a href = {"/Restaurants/" + this.props.id}>
                <div className = "col-sm-4" id = "restaurantGrid">
                    <img src = {this.props.img_url} />
                    <h1>{ this.props.name}</h1>
                    Address: { this.props.address }<br />
                    Rating: { this.props.rating } <br />
                    Food Type: { this.props.foodtype }

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
                    img_url={element.img_url}
                    id={element.id}
                    price = {element.price}
                />
            );
        });

        return (
            <div className = "row">
                {elements}
            </div>
        );
    }
});

// Could come from an API, LocalStorage, another component, etc...
var elements = [];

function loadRestGrid() {
    console.log(elements);
    getData();
    ReactDOM.render(<RestList elements={elements} />, document.getElementById('restGrid'));
}

function getData() {
    // $.ajax({
    //     type: 'GET',
    //     url: 'http://foodcloseto.me/API/Restaurants',
    //     data: data,
    //     async: false,
    //     beforeSend: function (xhr) {
    //         if (xhr && xhr.overrideMimeType) {
    //             xhr.overrideMimeType('application/json;charset=utf-8');
    //         }
    //     },
    //     error: function(jqXHR, textStatus, errorThrown) {
    //         alert(textStatus + ': ' + errorThrown);
    //     },
    //     dataType: 'json',
    //     success: function (data) {
    //         //Do stuff with the JSON data
    //     }
    // });
    // $.ajax({
    //     type: 'GET',
    //     url: 'http://localhost:5000/API/Restaurants',
    //     async: false,
    //     // data: data,
    //     // jsonpCallback: 'jsonCallback',
    //     // contentType: "application/json",
    //     dataType: 'json',
    //     success: function(data)
    //     {
    //         $('#jsonp-results').html(JSON.stringify(data));
    //         console.log(json);
    //     },
    //     error: function(e)
    //     {
    //         alert(e.message);
    //     }
    // });
    // $.ajax({
    //     dataType: "json",
    //     url: "http://foodcloseto.me/API/Restaurants",
    //     data: data,
    //     success: function (data) {
    //         console.log(data);
    //     }
    // });
    var url = "http://localhost:5000/API/Restaurants";
    $.getJSON( url, {
        tags: "restaurants",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            console.log(data);
            elements = data["restaurant_db"];
            // TODO: review if we need to keep this or remove above
            ReactDOM.render(<RestList elements={elements} />, document.getElementById('restGrid'));
        });

}

function sortGrid(e) {
    //getData();
    var sortBy = e.options[e.selectedIndex].value;
    console.log(e.options[e.selectedIndex].value);
    var url = "http://foodcloseto.me/API/Restaurants?sortby=" + sortBy.toLowerCase();
    $.getJSON( url, {
        tags: "restaurants",
        tagmode: "any",
        format: "json"
    })
        .done(function( data ) {
            console.log(data);
            elements = data;
            // TODO: review if we need to keep this or remove above
            ReactDOM.render(<RestList elements={elements} />, document.getElementById('restGrid'));
        });
}

function getFilters() {

}

function filterGrid() {

}


// start the display of elements
loadRestGrid();