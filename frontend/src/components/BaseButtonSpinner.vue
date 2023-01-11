<template>
  <div class="lds-ring" :style="`--spinner-width: ${widthSpinner}px;`">
    <div></div>
    <div></div>
    <div></div>
    <div></div>
  </div>
</template>

<script>
export default {
  name: 'BaseButtonSpinner',
  props: {
    widthSpinner: {
      type: Number,
      default: 30,
    },
  },
}
</script>

<style lang="scss" scoped>
.lds-ring {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;

  width: var(--spinner-width);
  height: var(--spinner-width);
}
.lds-ring div {
  position: absolute;
  box-sizing: border-box;

  display: block;

  width: 100%;
  height: 100%;

  border: 4px solid var(--primary-text-color);
  border-radius: 50%;
  border-color: #fff transparent transparent transparent;

  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
