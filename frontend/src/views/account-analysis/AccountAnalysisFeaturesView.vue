<template>
  <MainLayout>
    <SideBar :nav-urls="navUrls" />

    <div class="features">
      <div class="features__header">
        <MainLayoutTitleBlock
          title="Account"
          :back-page="{
            name: 'main page',
            routName: `AccountAnalysisWorkspaces`,
          }"
        />
        <BaseTabs
          :main-settings="tabs"
          default-tab="Account Activity"
          class="tabs"
        />
        <BaseButton :is-not-background="true" class="btn-report">
          <ReportsUploadIcon /> Download Report
        </BaseButton>
      </div>
      <router-view :current-project="currentProject"></router-view>
    </div>
  </MainLayout>
</template>

<script>
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import SideBar from '@/components/navigation/SideBar'

import BaseTabs from '@/components/project/widgets/modals/BaseTabs'
import BaseButton from '@/components/common/BaseButton'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'

export default {
  name: 'AccountAnalysisFeaturesView',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    SideBar,
    BaseTabs,
    BaseButton,
    ReportsUploadIcon,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  created() {
    this.navUrls = ['Dashboard'].map((item) => ({
      name: item,
      routeName: `AccountAnalysis${item}`,
    }))
    this.tabs = ['Account Activity', 'Mentions']
  },
}
</script>

<style lang="scss" scoped>
.features {
  display: flex;
  flex-direction: column;
  gap: 30px;

  padding: 0px 0px 20px 70px;
}
.features__header {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  .btn-report {
    margin-top: 25px;
    align-self: flex-end;
  }
}
</style>
