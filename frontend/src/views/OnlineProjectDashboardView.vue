<template>
  <MainLayout v-if="currentProject">
    <SideBar :nav-urls="navUrls" @open-tab="openTab" />

    <div class="project-wrapper">
      <router-view :current-project="currentProject"></router-view>
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import SideBar from '@components/navigation/SideBar'
import MainLayout from '@components/layout/MainLayout'

const {mapActions, mapState, mapGetters} = createNamespacedHelpers('online')

export default {
  name: 'OnlineProjectDashboardView',
  components: {
    SideBar,
    MainLayout,
  },
  computed: {
    ...mapState(['workspaces', 'loading']),
    ...mapGetters({project: get.CURRENT_PROJECT}),
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

      const workspaceExists = existingWorkspace || this.project || this.loading

      if (!workspaceExists) return this.goToNotFoundPage()

      return existingWorkspace
    },
    currentProject() {
      const existingProject = this.currentWorkspace?.projects.find(
        (el) => el.id === +this.projectId
      )

      const projectExists = existingProject || this.project || this.loading

      if (!projectExists) return this.goToNotFoundPage()

      return existingProject || this.project
    },
  },
  async created() {
    if (this.projectId && !this.workspaces.length) {
      this[action.GET_PROJECT](this.projectId)
    }

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
  },
  methods: {
    ...mapActions([action.GET_PROJECT, action.GET_AVAILABLE_WIDGETS]),
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
