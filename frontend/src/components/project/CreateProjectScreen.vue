<template>
  <MainLayout>
    <component :is="projectSteps" @next-step="nextStep()" />
  </MainLayout>
</template>

<script>
import MainLayout from '@components/layout/MainLayout'
import CreateProjectFirstStep from '@components/project/CreateProjectFirstStep'
import CreateProjectSecondStep from '@components/project/CreateProjectSecondStep'

export default {
  name: 'CreateProjectScreen',
  components: {
    MainLayout,
    CreateProjectFirstStep,
    CreateProjectSecondStep,
  },
  data() {
    return {
      isNextStep: false,
    }
  },
  computed: {
    projectSteps() {
      return this.isNextStep
        ? 'CreateProjectSecondStep'
        : 'CreateProjectFirstStep'
    },
  },
  methods: {
    nextStep() {
      this.isNextStep = !this.isNextStep
    },
  },
}
</script>

<style lang="scss" scoped>
.back-button {
  cursor: pointer;

  color: var(--secondary-text-color);
}

.arrow-back {
  margin-right: 6px;
}

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--primary-text-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.next-button {
  width: 114px;
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}
</style>
