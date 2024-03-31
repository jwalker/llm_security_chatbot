<template>
    <div class="sidebar">
      <div class="logo-container">
        <img src="@/assets/chatbot.jpg" alt="Chatbot Logo" class="chatbot-logo" />
      </div>
      <ul class="sidebar-menu">
        <li><a href="#">Home</a></li>
        <li><a href="#">Settings</a></li>
        <li><a href="#">Integrations</a></li>
        <li><a href="#">Help</a></li>
        <!-- Add more tool options or links as needed -->
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SideBar',
  };
  </script>
  
  <style>
  .sidebar {
    width: 250px; /* Adjust the width as needed */
    background-color: #f4f4f4; /* Light background color */
    height: 100vh; /* Full height */
    position: fixed; /* Fixed Sidebar (stay in place on scroll) */
    left: 0;
    overflow-x: hidden; /* Disable horizontal scroll */
    padding-top: 20px;
  }
  
  .logo-container {
    display: flex;
    justify-content: center; /* Center logo horizontally */
    margin-bottom: 20px;
  }
  
  .chatbot-logo {
    width: 100px; /* Adjust logo size as needed */
    height: auto;
  }
  
  .sidebar-menu {
    list-style-type: none; /* Remove bullets */
    padding: 0;
  }
  
  .sidebar-menu li a {
    padding: 10px 15px;
    text-decoration: none; /* No underline */
    font-size: 18px;
    color: #333; /* Dark text color */
    display: block; /* Make the links fill the container */
  }
  
  .sidebar-menu li a:hover {
    background-color: #ddd; /* Light grey background on hover */
  }
  </style>
  