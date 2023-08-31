<template>
  <div class="create-workspace-right-side">
    <img :src="stepsImages[step].src" :alt="stepsImages[step].alt" />
  </div>
</template>

<script>
export default {
  name: 'CreateWorkspaceRightSide',
  props: {
    step: {
      type: String,
      required: true,
    },
  },
  created() {
    this.stepsImages = {
      step1: {
        src: require('@/assets/workspace-name.svg'),
        alt: 'Create the workspace',
      },
      step2: {
        src: require('@/assets/project-name.svg'),
        alt: 'Create the project',
      },
      step3: {
        src: require('@/assets/search.svg'),
        alt: 'Define the search',
      },
      step3preview: {
        src: require('@/assets/empty-state.svg'),
        alt: 'No news for your request',
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.create-workspace-right-side {
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
