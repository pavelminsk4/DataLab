<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
  >
    <path
      d="M5.68341 11.8201L9.61589 16.5391C9.81579 16.7789 10.1842 16.7789 10.3841 16.5391L14.3166 11.8201C14.588 11.4944 14.3564 11 13.9325 11H6.06752C5.6436 11 5.41202 11.4944 5.68341 11.8201Z"
      :fill="color.up"
    />
    <path
      d="M14.3166 8.17991L10.3841 3.46093C10.1842 3.22106 9.81579 3.22105 9.61589 3.46093L5.68341 8.17991C5.41202 8.50557 5.6436 9 6.06752 9L13.9325 9C14.3564 9 14.588 8.50557 14.3166 8.17991Z"
      :fill="color.down"
    />
  </svg>
</template>

<script>
import {SORT_BY} from '@lib/constants'

export default {
  props: {
    sortBy: {type: String, default: ''},
  },
  computed: {
    color() {
      const defaultColor = '#B0B5B8'
      const activeColor = '#797D80'
      return {
        up: this.sortBy === SORT_BY.ASCENDING ? activeColor : defaultColor,
        down: this.sortBy === SORT_BY.DESCENDING ? activeColor : defaultColor,
      }
    },
  },
}
</script>
