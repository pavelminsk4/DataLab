<template>
  <MainLayout v-if="currentProject" :is-project-extra-settings="true">
    <SideBar :nav-urls="navUrls" @open-tab="openTab" />

    <div class="project-dashboard-wrapper">
      <router-view :current-project="currentProject"></router-view>
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import SideBar from '@/components/navigation/SideBar'
import MainLayout from '@/components/layout/MainLayout'

export default {
  name: 'OnlineProjectDashboardView',
  components: {
    SideBar,
    MainLayout,
  },
  computed: {
    ...mapState(['workspaces', 'availableWidgets']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      return this.workspaces.filter((el) => el.id === +this.workspaceId)
    },
    currentProject() {
      return this.currentWorkspace[0]?.projects.filter(
        (el) => el.id === +this.projectId
      )[0]
    },
  },
  async created() {
    this.navUrls = [
      'Analytics',
      'Search',
      'Summary',
      'Sentiment',
      // 'Demography',
      // 'Influencers',
    ].map((item) => ({
      name: item,
      routeName: `Online${item}`,
    }))

    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }

    await this[action.GET_AVAILABLE_WIDGETS](this.projectId)

    await this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
      projectId: this.projectId,
      widgetId: this.availableWidgets.clipping_feed_content_widget.id,
    })
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.GET_AVAILABLE_WIDGETS,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    openTab(pathName) {
      this.$router.push({
        name: pathName,
      })
    },
    goToDashboard() {
      this.$router.push({
        name: 'OnlineHome',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.project-dashboard-wrapper {
  width: 100%;
  height: calc(100vh - 120px);
  padding-left: 70px;
}
</style>
