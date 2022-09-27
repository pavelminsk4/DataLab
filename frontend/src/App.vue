<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style lang="scss">
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

  /* v-select */
  --vs-search-input-placeholder-color: var(--secondary-text-color);

  --vs-border-radius: 10px;

  --vs-dropdown-bg: var(--secondary-bg-color);
  --vs-dropdown-color: var(--primary-text-color);
  --vs-dropdown-box-shadow: 0 0 4px rgba(5, 95, 252, 0.49), 0;
  --vs-dropdown-option-padding: 11px 19px;

  --vs-dropdown-option--active-bg: var(--primary-button-color);
  --vs-dropdown-option--active-color: var(--primary-text-color);

  --vs-dropdown-option--deselect-bg: #fb5858;
  --vs-dropdown-option--deselect-color: #fff;
}

.v-select {
  .vs__dropdown-toggle {
    background-color: var(--secondary-bg-color);

    .vs__selected-options {
      padding-left: 19px;

      color: var(--primary-text-color);
    }
  }

  .vs__dropdown-menu {
    overflow-x: hidden;
    overflow-y: auto;

    border: 1px solid var(--primary-button-color);
    border-top: 0;

    &::-webkit-scrollbar {
      width: 5px;
    }

    &::-webkit-scrollbar-track {
      background: var(--secondary-bg-color);
      border: 1px solid var(--input-border-color);
      border-radius: 10px;
    }

    &::-webkit-scrollbar-thumb {
      height: 4px;

      background: var(--secondary-text-color);
      border-radius: 10px;
    }
  }
}
</style>
