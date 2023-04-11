<template>
  <MainLayout
    :is-two-columns="currentStep !== 'step3'"
    class="create-report-wrapper"
  >
    <template #default>
      <MainLayoutTitleBlock
        title="Reports"
        :description="description"
        :back-page="{
          name: 'main page',
          routName: 'MainView',
        }"
      />

      <ReportProgressBar :step="currentStep" />

      <div class="step-content">
        <router-view></router-view>
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
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ReportProgressBar from '@/components/reports/ReportProgressBar'

export default {
  name: 'CreateReportView',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    ReportProgressBar,
  },
  computed: {
    ...mapGetters([get.CREATE_REPORTS_STEP]),
    currentStep() {
      return `step${this[get.CREATE_REPORTS_STEP]}`
    },
    description() {
      const descriptions = {
        step1: 'Set up and manage reports',
        step2: 'Set up sending time',
        step3: 'Choose projects',
        step4: 'Set up sending time',
        step5: 'Create Report',
      }
      return descriptions[this.currentStep]
    },
  },
}
</script>

<style lang="scss" scoped>
.create-report-wrapper {
  --width-second-column: 39%;
  --create-report-footer-height: 72px;
}

.step-content {
  position: relative;

  height: calc(100% + var(--create-report-footer-height));
  padding-bottom: var(--create-report-footer-height);
  margin-top: 40px;
}

.create-report-footer {
  position: absolute;
  left: 0;
  bottom: 0;

  width: calc(100% - var(--width-second-column));
  height: var(--create-report-footer-height);

  background-color: var(--background-primary-color);
  border-top: var(--border-primary);
}

.second-column {
  height: 100%;
  padding: 32px 32px 0 16px;
}
</style>

<style lang="scss">
.create-reports__footer {
  position: sticky;
  bottom: -24px;
  z-index: 10;

  display: flex;
  justify-content: flex-end;
  align-items: center;

  width: calc(100% + 2 * 32px);
  height: var(--create-report-footer-height);
  padding: 0 32px;
  margin-left: -32px;

  background-color: var(--background-primary-color);
}
</style>
