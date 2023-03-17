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
import {action} from '@store/constants'

import SideBar from '@/components/navigation/SideBar'
import MainLayout from '@/components/layout/MainLayout'

const {mapActions, mapState} = createNamespacedHelpers('social')

export default {
  name: 'SocialProjectDashboardView',
  components: {
    SideBar,
    MainLayout,
  },
  computed: {
    ...mapState(['workspaces']),
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
  created() {
    this.navUrls = ['Dashboard', 'Search'].map((item) => ({
      name: item,
      routeName: `Social${item}`,
    }))
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    openTab(pathName) {
      this.$router.push({
        name: pathName,
      })
    },
    goToDashboard() {
      this.$router.push({
        name: 'SocialHome',
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
