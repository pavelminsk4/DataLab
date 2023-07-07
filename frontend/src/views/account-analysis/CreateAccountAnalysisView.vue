<template>
  <MainLayout :is-two-columns="true" class="create-report-wrapper">
    <template #default>
      <div class="create-report-step-content">
        <MainLayoutTitleBlock
          :title="accountAnalysisData.title"
          :description="accountAnalysisData.description"
          :back-page="{
            name: 'main page',
            routeName: 'MainView',
          }"
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
import ProgressBar from '@/components/account-analysis/AccountAnalysisProgressBar'

export default {
  name: 'CreateAccountAnalysisView',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    ProgressBar,
  },
  computed: {
    currentStep() {
      return `step${this.$route.name.toString().slice(-1)}`
    },
    accountAnalysisData() {
      const data = {
        step1: {
          title: 'The Workspaces',
          description: 'Create a new workspace on your Dashboard',
        },
        step2: {
          title: 'Account Analysis',
          description:
            'Monitor social media content created by your brand and influencers ',
        },
      }
      return data[this.currentStep]
    },
  },
}
</script>

<style lang="scss" scoped>
.create-report-wrapper {
  --create-report-footer-height: 72px;
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
