<template>
  <div class="create-right-side">
    <img :src="stepsImages[step].src" :alt="stepsImages[step].alt" />
  </div>
</template>

<script>
export default {
  name: 'CreateAccountAnalysisRightSide',
  props: {
    step: {type: String, required: true},
  },
  created() {
    this.stepsImages = {
      step1: {
        src: require('@assets/account-analysis/workspace-name.svg'),
        alt: 'Create the account analysis workspace',
      },
      step2: {
        src: require('@assets/account-analysis/project-name.svg'),
        alt: 'Create the account analysis project',
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
