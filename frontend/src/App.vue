<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

  * {
    margin: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }

  body {
    margin: 0;
    padding: 0;
  }

  :root {
    --primary-text-color: #FFFFFF;
    --secondary-text-color: #9198A7;

    --primary-button-color: #055FFC;
    --secondary-button-color: #222A36;
    --icon-bg-color: #1A1C1E;

    --primary-bg-color: #1D1E1F;
    --secondary-bg-color: #242529;
  }
</style>
