<template>
  <aside class="create-alert-right-side">
    <img :src="stepsImages[step].src" :alt="stepsImages[step].alt" />
  </aside>
</template>

<script>
export default {
  name: 'CreateAlertRightSide',
  props: {
    step: {type: String, required: true},
  },
  created() {
    this.stepsImages = {
      step1: {
        src: require('@/assets/alerts/alert-name.svg'),
        alt: 'Create the alert',
      },
      step2: {
        src: require('@/assets/alerts/alert-set-triggering.svg'),
        alt: 'Set alert triggering',
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.create-alert-right-side {
  display: flex;
  justify-content: center;
  align-items: center;

  height: 100%;
  width: 100%;
  padding-bottom: 100px;

  img {
    width: inherit;
  }
}
</style>
