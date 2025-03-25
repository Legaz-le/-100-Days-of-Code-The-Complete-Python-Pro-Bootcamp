<script>
    document.getElementById('loginForm').addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission

      // Get form values
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      // Log form data (you can replace this with an API call)
      console.log({
        email,
        password,
      });

      alert('Login successful! (Mock)');
    });
</script>
// Initialize Leaflet Map
document.addEventListener('DOMContentLoaded', function () {
  // Initialize the map
  const map = L.map('map-container').setView([51.505, -0.09], 13); // London coordinates

  // Add OpenStreetMap tiles
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // Add markers for venues
  const venues = [
    { name: 'Cafe Cozy Corner', lat: 51.505, lng: -0.09 },
    { name: 'The Work Hub', lat: 51.51, lng: -0.1 },
    { name: 'Library Lounge', lat: 51.49, lng: -0.08 }
  ];

  venues.forEach(venue => {
    L.marker([venue.lat, venue.lng])
      .addTo(map)
      .bindPopup(venue.name);
  });
});