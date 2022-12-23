<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600&display=swap');

* {
  margin: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  margin: 0;
  padding: 0;

  min-height: fit-content;
  background-color: var(--primary-bg-color);
  background-size: 919px 100%;
}

:root {
  --primary-text-color: #ffffff;
  --secondary-text-color: #9198a7;

  --primary-button-color: #055ffc;
  --secondary-button-color: #222a36;
  --hover-button-color: #29303d;

  --icon-bg-color: #1a1c1e;

  --border-color: #2d2d31;
  --input-border-color: var(--border-color);
  --modal-border-color: #404046;
  --sidebar-border-color: #2c2c2c;
  --modal-line-color: #2e2f34;

  --primary-bg-color: #1d1e1f;
  --secondary-bg-color: #242529;

  --box-shadow-color: #0b56d9;
  --progress-line: #34353b;

  --disabled-color: #3e4047;

  --tag-color: #30f47e;
  --key-word-color: #e7a747;

  --negative-status: #f94747;
  --neutral-status: #f6aa37;

  --dp-background-color: var(--input-border-color);

  --keyword: #f82a6c;

  --hover-circle-gradient: radial-gradient(
    circle at 2.5%,
    rgba(5, 95, 252, 0.8),
    #1f2022 6.5%
  );

  --animation-hover-gradient: hover-gradient 0.5s ease;
}

@keyframes hover-gradient {
  0% {
    background-position: 15% 0%;
  }
  100% {
    background-position: 0% 0%;
  }
}
</style>
