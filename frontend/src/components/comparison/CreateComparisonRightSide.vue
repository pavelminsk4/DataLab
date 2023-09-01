<template>
  <div class="create-right-side">
    <img :src="stepsImages[step].src" :alt="stepsImages[step].alt" />
  </div>
</template>

<script>
export default {
  name: 'CreateComparisonRightSide',
  props: {
    step: {type: String, required: true},
  },
  created() {
    this.stepsImages = {
      step1: {
        src: require('@/assets/comparison/workspace-name.svg'),
        alt: 'Create the Comparison workspace',
      },
      step2: {
        src: require('@/assets/comparison/project-name.svg'),
        alt: 'Create the Comparison project',
      },
      step3: {
        src: require('@/assets/comparison/search-name.svg'),
        alt: 'Define the comparison',
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.create-right-side {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 100%;
  height: 100%;
  padding-bottom: 100px;

  img {
    width: inherit;
  }
}
</style>
