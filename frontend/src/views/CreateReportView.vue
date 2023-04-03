<template>
  <MainLayout :is-two-columns="true" width-second-columns="39%">
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

      <router-view></router-view>
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
.second-column {
  height: 100%;
  padding: 32px 32px 0 16px;
}
</style>
