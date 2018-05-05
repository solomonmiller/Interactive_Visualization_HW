    var name_url = "/names";
    Plotly.d3.json(name_url, function(error, data) {
        if (error) return console.warn(error);
        names = Object.values(data);
        for (var n = 0; n < names.length; n++) {
            var $option = document.createElement("option");
            var $selection = document.querySelector("#selDataset")
            $option.value = names[n];
            $option.innerHTML = names[n];
            $selection.appendChild($option);
        };
    })

    Plotly.d3.json('/samples/BB_940', function(error, data){
        if (error) return console.warn(error);
        var layout = {
            height: 400,
            width: 500};
        
        var PIE = document.getElementById('pie');
        Plotly.plot(PIE, data, layout);
    })