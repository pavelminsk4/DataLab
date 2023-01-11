<template>
  <BaseButtonSpinner v-if="isLoading" :widthSpinner="18" />
  <svg
    v-else
    width="18"
    height="18"
    viewBox="0 0 18 18"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    :class="['clipping-icon', isClippingElement && 'active-clipping-post']"
  >
    <path
      d="M10.1915 5.38281C10.3986 5.38281 10.5665 5.55071 10.5665 5.75781V8.45065C10.5665 9.0334 10.8806 9.50559 11.2189 9.8151C11.8395 10.3829 12.331 11.3715 12.5272 12.3704C12.5388 12.4294 12.5243 12.4775 12.4818 12.5228C12.4339 12.5741 12.3493 12.6181 12.2421 12.6181H5.75684C5.64967 12.6181 5.56505 12.5741 5.51712 12.5228C5.47472 12.4775 5.46029 12.4295 5.47187 12.3707C5.66968 11.3656 6.1674 10.3717 6.7957 9.8031C7.13797 9.49337 7.45602 9.01884 7.45602 8.43222V5.75781C7.45602 5.55071 7.62391 5.38281 7.83102 5.38281H10.1915Z"
      fill="white"
      stroke="white"
      stroke-width="1.25"
      stroke-linecap="round"
    />
    <path
      d="M5.46387 4.75781H12.5349"
      stroke="white"
      stroke-width="1.25"
      stroke-linecap="round"
    />
    <path
      d="M9 13V17"
      stroke="white"
      stroke-width="1.25"
      stroke-linecap="round"
    />
  </svg>
</template>

<script>
import BaseButtonSpinner from '@/components/BaseButtonSpinner'

export default {
  name: 'ClippingIcon',
  components: {
    BaseButtonSpinner,
  },
  props: {
    isClippingElement: {
      type: Boolean,
      default: false,
    },
    isLoading: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style lang="scss" scoped>
.clipping-icon {
  position: relative;

  cursor: pointer;

  &:hover {
    transform: rotate(30deg);
  }
}

.active-clipping-post {
  border: 1px solid var(--primary-text-color);
  border-radius: 100px;

  transform: rotate(30deg);
}
</style>
