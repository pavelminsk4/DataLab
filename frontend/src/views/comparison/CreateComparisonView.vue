<template>
  <MainLayout :is-two-columns="true" class="create-comparison-wrapper">
    <template #default>
      <div class="create-comparison-step-content">
        <MainLayoutTitleBlock
          :title="stepsData.title"
          :description="stepsData.description"
          :back-page="{
            name: 'main page',
            routeName: 'MainView',
          }"
          :should-translate="false"
        />

        <ProgressBar :step="currentStep" />

        <div class="step-content">
          <router-view></router-view>
        </div>
      </div>
    </template>

    <template #second-column>
      <div class="second-column">
        <router-view name="secondColumn"></router-view>
      </div>
    </template>
  </MainLayout>
</template>

<script>
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProgressBar from '@/components/comparison/ComparisonProgressBar'

export default {
  name: 'CreateComparisonView',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    ProgressBar,
  },
  computed: {
    currentStep() {
      return `step${this.$route.name.toString().slice(-1)}`
    },
    stepsData() {
      const data = {
        step1: {
          title: 'The Workspaces',
          description: 'Create a new workspace on your Dashboard',
        },
        step2: {
          title: 'The Project',
          description: 'Name the project',
        },
        step3: {
          title: 'Define the comparison',
          description: 'Select 2 or 3 projects to compare',
        },
      }
      return data[this.currentStep]
    },
  },
}
</script>

<style lang="scss" scoped>
.create-comparison-wrapper {
  --create-comparison-footer-height: 72px;
}

.step-content {
  position: relative;

  margin-top: 40px;
}

.second-column {
  width: 45vw;
  height: 100%;
  padding: 32px 32px 0 16px;
}
</style>
