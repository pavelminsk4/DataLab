<template>
  <svg
    width="8"
    height="6"
    viewBox="0 0 8 6"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    :style="`transform: rotate(${rotate}deg)`"
  >
    <path
      d="M1 1.5L4 4.5L7 1.5"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>

<script>
export default {
  props: {
    direction: {type: String, default: 'down'},
  },
  computed: {
    rotate() {
      switch (this.direction) {
        case 'left':
          return 90
        case 'top':
          return 180
        case 'right':
          return 270
        default:
          return 0
      }
    },
  },
}
</script>
