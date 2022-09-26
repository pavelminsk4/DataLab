<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
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

  min-height: fit-content;
  background: url(http://localhost:8080/img/img.1694ddef.svg) 50% 50% no-repeat;
  background-color: var(--primary-bg-color);
  background-size: 919px 100%;
}

:root {
  --primary-text-color: #ffffff;
  --secondary-text-color: #9198a7;

  --primary-button-color: #055ffc;
  --secondary-button-color: #222a36;

  --icon-bg-color: #1a1c1e;

  --input-border-color: #2d2d31;
  --modal-border-color: #404046;
  --modal-line-color: #2e2f34;

  --primary-bg-color: #1d1e1f;
  --secondary-bg-color: #242529;

  --box-shadow-color: #0b56d9;
  --progress-line: #34353b;

  --disabled-color: #3e4047;

  --tag-color: #30f47e;
  --key-word-color: #e7a747;

  --negative-status: #f94747;

  --dp-background-color: var(--input-border-color);
}
</style>
