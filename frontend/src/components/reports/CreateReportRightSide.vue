<template>
  <div class="create-report-right-side">
    <img :src="stepsImages[step].src" :alt="stepsImages[step].alt" />
  </div>
</template>

<script>
export default {
  name: 'CreateReportRightSide',
  props: {
    step: {type: String, required: true},
  },
  created() {
    this.stepsImages = {
      step1: {
        src: require('@/assets/reports/report-name.svg'),
        alt: 'Create the report',
      },
      step2: {
        src: require('@/assets/reports/report-set-time.svg'),
        alt: 'Set send time',
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.create-report-right-side {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 39vw;
  height: 100%;
  padding-bottom: 100px;

  img {
    width: inherit;
  }
}
</style>
