<template>
  <MainLayout>
    <SideBar :nav-urls="navUrls" @open-tab="openTab" />

    <div class="features">
      <div class="features__header">
        <MainLayoutTitleBlock
          :title="currentProject.title"
          :desription="currentProject.description"
          :back-page="{
            name: 'workspaces',
            routeName: `AccountAnalysisWorkspaces`,
          }"
        />
        <BaseTabs
          :main-settings="tabs"
          default-tab="Account Activity"
          class="tabs"
          @update-setting-panel="updateSettingPanel"
        />
      </div>
      <router-view
        :current-project="currentProject"
        :current-tab="currentTab"
      ></router-view>
    </div>
  </MainLayout>
</template>

<script>
import {action} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'

import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import SideBar from '@/components/navigation/SideBar'
import BaseTabs from '@/components/project/widgets/modals/BaseTabs'
import {stringToPascalCase} from '@/lib/utilities'

const {mapActions} = createNamespacedHelpers('accountAnalysis/widgets')

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
  data() {
    return {
      currentTab: 'AccountActivity',
    }
  },
  created() {
    this[action.CLEAR_WIDGETS_DATA]()
    this.navUrls = [
      'Dashboard',
      'Optimization',
      'Posts',
      //'Followers'
    ].map((item) => ({
      name: item,
      routeName: `AccountAnalysis${item}`,
    }))

    this.tabs = ['Account Activity', 'Mentions']
  },
  methods: {
    ...mapActions([action.CLEAR_WIDGETS_DATA]),
    stringToPascalCase,
    openTab(pathName) {
      this.$router.push({
        name: pathName,
      })
    },
    updateSettingPanel(val) {
      this.currentTab = stringToPascalCase(val)
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
