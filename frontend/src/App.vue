<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600&display=swap');

:root {
  //TODO: fix colors ---------------------------------------------
  --general-background-color: #ffffff;
  --general-text-color: #29333d;
  --secondary-text-color: #5c6e80;
  --hover-text-color: #664dff;

  --border-color: #e3e5e8;

  --primary-chips-backgroud-color: #e9f0f3;

  --neutral-sentiment-color: #516bee;
  --positive-sentiment-color: #00b884;
  --negative-sentiment-color: #ed2549;
  --neutral-sentiment-background: rgba(81, 107, 238, 0.15);
  --positive-sentiment-background: #d5f5ec;
  --negative-sentiment-background: #ffe3e8;

  --primary-text-color: #ffffff;
  //end ------------------------------------------------------------

  --primary-color: #715de7;
  --primary-hover-color: #664dff;
  --primary-active-color: #e7e2fe;
  --primary-disable-color: #d3d0e7;

  --background-primary-color: #f8fafd;
  --background-secondary-color: #ffffff;

  --typography-title-color: #29333d;
  --typography-primary-color: #484c52;
  --typography-secondary-color: #70767d;

  --button-primary-color: var(--primary-color);
  --button-primary-disabled-color: var(--primary-disable-color);
  --button-primary-hover-color: var(--primary-hover-color);
  --button-secondary-hover-color: #f4f2fe;
  --button-text-color: #ffffff;
  --button-text-disabled-color: #d2d5d9;

  --positive-primary-color: #00b884;
  --positive-secondary-color: #d5f5ec;
  --negative-primary-color: #ed2549;
  --negative-secondary-color: #ffe3e8;

  // TODO: Delete --------------------------------
  --secondary-button-color: #222a36;
  // end -----------------------------------------

  --icon-bg-color: #1a1c1e;

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

  --clipping-card: #242733;

  --header-height: 52px;

  --hover-circle-gradient: radial-gradient(
    circle at 2.5%,
    rgba(5, 95, 252, 0.8),
    #1f2022 6.5%
  );

  --animation-hover-gradient: hover-gradient 0.5s ease;
}

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

  color: var(--typography-primary-color);
}

h1,
h2,
h3,
h4 {
  color: var(--typography-title-color);
}

.scroll {
  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}

.overflow-hidden {
  overflow: hidden;
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
