<template>
  <div class="create-right-side">
    <img :src="stepsImages[step].src" :alt="stepsImages[step].alt" />
  </div>
</template>

<script>
export default {
  name: 'CreateTFSRightSide',
  props: {
    step: {type: String, required: true},
  },
  created() {
    this.stepsImages = {
      step1: {
        src: require('@assets/twenty-four-seven/workspace-name.svg'),
        alt: 'Create the 24/7 workspace',
      },
      step2: {
        src: require('@assets/twenty-four-seven/project-name.svg'),
        alt: 'Create the 24/7 project',
      },
      step3: {
        src: require('@assets/twenty-four-seven/define-search.svg'),
        alt: 'Define the search',
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
