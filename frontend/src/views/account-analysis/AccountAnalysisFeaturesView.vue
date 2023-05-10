<template>
  <MainLayout>
    <SideBar :nav-urls="navUrls" @open-tab="openTab" />

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
export default {
  name: 'AccountAnalysisFeaturesView',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    SideBar,
    BaseTabs,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  created() {
    this.navUrls = ['Dashboard', 'Optimization'].map((item) => ({
      name: item,
      routeName: `AccountAnalysis${item}`,
    }))
    this.tabs = ['Account Activity', 'Mentions']
  },
  methods: {
    openTab(pathName) {
      this.$router.push({
        name: pathName,
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.features {
  display: flex;
  flex-direction: column;
  gap: 30px;

  padding: 0px 0px 20px 70px;
  &__header {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}
</style>
