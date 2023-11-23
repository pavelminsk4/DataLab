<template>
  <BaseButtonSpinner v-if="isLoading" :widthSpinner="18" />
  <svg
    v-else-if="isClippingPost && !isLoading"
    width="15"
    height="19"
    viewBox="0 0 15 19"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    class="clipping-icon"
  >
    <path
      d="M0.5 1.33083V16.2929C0.5 17.1707 1.55002 17.6226 2.18746 17.0191L6.59032 12.8513C6.97594 12.4862 7.57962 12.4862 7.96524 12.8513L12.3681 17.0191C13.0055 17.6226 14.0556 17.1707 14.0556 16.2929V10.0618V1.33083C14.0556 0.778541 13.6078 0.330826 13.0556 0.330826H1.5C0.947715 0.330826 0.5 0.778541 0.5 1.33083Z"
      fill="#e54985"
    />
  </svg>

  <svg
    v-else
    width="18"
    height="20"
    viewBox="0 0 18 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    class="clipping-icon"
  >
    <path
      d="M15.0556 11.0618V17.2929C15.0556 18.1707 14.0055 18.6226 13.3681 18.0191L8.96524 13.8513C8.57962 13.4862 7.97594 13.4862 7.59032 13.8513L3.18746 18.0191C2.55002 18.6226 1.5 18.1707 1.5 17.2929V2.33083C1.5 1.77854 1.94772 1.33083 2.5 1.33083H11.6111"
      stroke="currentColor"
      stroke-width="1.75"
      stroke-linecap="round"
    />
    <path
      d="M14.7222 2.77444V4.91312M14.7222 7.0518V4.91312M14.7222 4.91312H16.9444M14.7222 4.91312H12.5"
      stroke="currentColor"
      stroke-width="1.75"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>

<script>
import BaseButtonSpinner from '@components/BaseButtonSpinner'

export default {
  name: 'ClippingIcon',
  components: {
    BaseButtonSpinner,
  },
  props: {
    isClippingPost: {
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

  color: var(--typography-secondary-color);

  &:hover {
    color: var(--primary-hover-color);
  }
}

.active-clipping-post {
  border: 1px solid var(--primary-hover-color);
  border-radius: 100px;
  background-color: var(--primary-hover-color);

  transform: rotate(30deg);
}
</style>
