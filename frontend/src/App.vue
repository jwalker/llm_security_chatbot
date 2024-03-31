<template>
  <div id="app">
    <SideBar />
    <div class="content">
      <!-- Your main content here, such as SecurityChatBox -->
      <SecurityChatBox />
    </div>
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue';
import SecurityChatBox from './components/SecurityChatBox.vue';

export default {
  name: 'App',
  components: {
    SideBar,
    SecurityChatBox,
  },
};
</script>

<style>
.content {
  margin-left: 250px; /* Adjust according to the sidebar width */
}
</style>
