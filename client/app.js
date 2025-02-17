function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBath");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
}
  
function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
}
  
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bath = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
    var area_type = document.getElementById("uiArea");
    console.log(area_type)
    var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        location: location.value,
        bhk: bhk,
        bath: bath,
        area_type: area_type.value
    },function(data, status) {
        console.log(data.estimate_price);
        estPrice.innerHTML = "<h2>" + data.estimate_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
        $.get(url,function(data, status) {
            console.log("got response for get_location_names request", data);
            if(data) {
                var locations = data.locations;
                var uiLocations = document.getElementById("uiLocations");
                $('#uiLocations').empty();
                for(var i in locations) {
                    var opt = new Option(locations[i]);
                    $('#uiLocations').append(opt);
                }
            }
        });
    
    // var url = "http://127.0.0.1:5000/get_area_types"; // Use this if you are NOT using nginx which is first 7 tutorials
        var url = "/api/get_area_types"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
            $.get(url,function(data, status) {
                console.log("got response for get_area_types request", data);
                if(data) {
                    var area_type = data.area_type;
                    var uiArea = document.getElementById("uiArea");
                    $('#uiArea').empty();
                    for(var i in area_type) {
                        var opt = new Option(area_type[i]);
                        $('#uiArea').append(opt);
                    }
                }
            });
}


window.onload = onPageLoad;