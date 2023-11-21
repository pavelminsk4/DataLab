<template>
  <MainLayout v-if="workspaces.length">
    <SideBar :nav-urls="navUrls" @open-tab="openTab" />

    <div class="project-wrapper">
      <router-view :current-project="currentProject"></router-view>
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import SideBar from '@/components/navigation/SideBar'
import MainLayout from '@/components/layout/MainLayout'

const {mapActions, mapState} = createNamespacedHelpers('online')

export default {
  name: 'OnlineProjectDashboardView',
  components: {
    SideBar,
    MainLayout,
  },
  computed: {
    ...mapState(['workspaces', 'loading']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      const existingWorkspace = this.workspaces.find(
        (el) => el.id === +this.workspaceId
      )
      if (!existingWorkspace && !this.loading) return this.goToNotFoundPage()

      return existingWorkspace
    },
    currentProject() {
      const existingProject = this.currentWorkspace?.projects.find(
        (el) => el.id === +this.projectId
      )
      if (!existingProject && !this.loading) return this.goToNotFoundPage()

      return existingProject
    },
  },
  async created() {
    this.navUrls = [
      'Analytics',
      'Search',
      'Summary',
      'Sentiment',
      'Demography',
      'Influencers',
    ].map((item) => ({
      name: item,
      routeName: `Online${item}`,
    }))

    await this[action.GET_AVAILABLE_WIDGETS](this.projectId)

    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.GET_AVAILABLE_WIDGETS]),
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
.project-wrapper {
  width: 100%;
  height: calc(100vh - 120px);
  padding-left: 70px;
}
</style>
