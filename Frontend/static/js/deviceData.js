  function getDeviceData(x) {
 
    var token = localStorage.getItem("access_token");
                if(token == undefined){                  
                    //  window.location.href = "http://"+window.location.hostname+":5501"
                    window.location.href = "../../templates/Login.html";
                }else{   
  fetch("http://"+window.location.hostname+":8000/devicestream", {
    method:'GET',
    headers: {
    Accept: 'application/json',
    Authorization: 'Bearer ' + localStorage.getItem('access_token')}}).then(
  res => {
    res.json().then(
      data => {
        console.log(data);
        if (data.length > 0) {
          var temp = "";
          
          data.forEach((itemData) => {
            if (itemData.Device_Id ==  document.getElementById('deviceId').value){
              temp += "<tr>";
              temp += "<td>" + itemData.Battery_Level + "</td>";
              temp += "<td>" + itemData.Device_Id + "</td>";
              temp += "<td>" + itemData.First_Sensor_temperature + "</td>";
              temp += "<td>" + itemData.Route_From + "</td>";
              temp += "<td>" + itemData.Route_To + "</td></tr>";
         }});
          document.getElementById('data').innerHTML = temp;
        }
      }
    )
  }
)
}
  }
function logout(){
    localStorage.removeItem('access_token')
    window.location.href = "../../templates/Login.html"
    // window.location.href = "http://"+window.location.hostname+":5500/../../Frontend/templates/Login.html";
  }
