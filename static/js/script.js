document.getElementById('id_date').addEventListener('change', function() {
    let reservations = document.getElementsByClassName('reservation-info');
    for ( let reservation of reservations){
        reservation.style.display = "block";
        let tag = reservation.getAttribute('data-type');
        if (tag !== this.value)
            reservation.style.display = "none";
    }
    document.getElementById('date-selection').innerHTML = this.value;
  });
