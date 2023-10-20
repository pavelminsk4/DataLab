<template>
  <FlashMessagesContainer />

  <router-view></router-view>
</template>

<script>
import FlashMessagesContainer from '@components/flash-messages/FlashMessagesContainer'

export default {
  name: 'App',
  components: {FlashMessagesContainer},
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');

:root {
  --primary-color: #e54985;
  --primary-hover-color: #bb3d6e;
  --primary-active-color: #fcedf3;
  --primary-disable-color: #fadae6;

  --background-primary-color: #f8f9fd;
  --background-secondary-color: #ffffff;
  --background-additional-color: #ebebf0;

  --typography-title-color: #29333d;
  --typography-primary-color: #484c52;
  --typography-secondary-color: #70767d;

  --button-primary-color: var(--primary-color);
  --button-primary-disabled-color: var(--primary-disable-color);
  --button-primary-hover-color: var(--primary-hover-color);
  --button-secondary-hover-color: #f4f2fe;
  --button-text-color: #ffffff;
  --button-text-disabled-color: #d2d5d9;

  --border-color: #dee0e3;
  --border-active-color: var(--primary-color);
  --border-primary: 1px solid var(--border-color);
  --border-radius: 8px;

  --neutral-primary-color: #516bee;
  --neutral-secondary-color: #e5e9fc;
  --positive-primary-color: #00b884;
  --positive-secondary-color: #d5f5ec;
  --negative-primary-color: #ed2549;
  --negative-secondary-color: #ffe3e8;

  --error-primary-color: var(--negative-primary-color);
  --error-secondary-color: var(--negative-secondary-color);

  --male-bg-color: #e5e9fc;
  --female-bg-color: #ffe3e8;

  --icon-primary-color: #797d80;
  --icon-hover-color: var(--primary-color);

  --chips-background-primary-color: var(--background-secondary-color);
  --chips-background-secondary-color: #eef1f3;
  --chips-background-female-color: var(--female-bg-color);
  --chips-background-male-color: var(--male-bg-color);

  --input-border-color: var(--border-color);
  --modal-border-color: #404046;
  --sidebar-border-color: #2c2c2c;
  --modal-line-color: #2e2f34;

  --primary-bg-color: #1d1e1f;
  --secondary-bg-color: #242529;

  --box-shadow-color: #0b56d9;
  --progress-line: #34353b;

  --warning-color: #cf0f04;

  --link-color: #0016dc;

  --disabled-color: #3e4047;

  --tag-color: #30f47e;
  --key-word-color: #e7a747;
  --hashtag-bg-color: #f5e8fe;

  --negative-status: #f94747;
  --neutral-status: #f6aa37;

  --dp-background-color: var(--input-border-color);

  --keyword: #f82a6c;

  --clipping-card: #242733;

  --picking-card-color: #effcfe;

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
  background-color: var(--background-primary-color);
  background-size: 919px 100%;

  font-size: 14px;
  color: var(--typography-primary-color);
}

h1,
h2,
h3,
h4 {
  color: var(--typography-title-color);
}

.scroll {
  overflow: auto;

  scroll-behavior: smooth;

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--background-secondary-color);
    border: 1px solid var(--border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--primary-color);
    border-radius: 10px;
  }
}

.disable {
  pointer-events: none;
  cursor: not-allowed;

  opacity: 50%;
}

.overflow-hidden {
  overflow: hidden;
}

svg {
  color: var(--icon-primary-color);
}

.icon-button {
  cursor: pointer;

  &:hover {
    color: var(--icon-hover-color);
  }
}

@keyframes hover-gradient {
  0% {
    background-position: 15% 0%;
  }
  100% {
    background-position: 0% 0%;
  }
}

.base-icon {
  padding: 2px;
  border-radius: 5px;
}
.online-icon {
  @extend .base-icon;
  background-color: #11afd1;
}

.social-icon {
  @extend .base-icon;
  background-color: #246fdf;
}

.twitter-icon {
  @extend .base-icon;
  background-color: #00a6de;
}

.calendar-icon {
  @extend .base-icon;
  background-color: #a0b8be;
}
</style>
