<template>
  <MainLayout v-if="currentProject" :is-project-extra-settings="true">
    <SideBar @open-tab="openTab" />

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
  name: 'ProjectReports',
  components: {
    SideBar,
    MainLayout,
  },
  created() {
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
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
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    openTab(pathName) {
      this.$router.push({
        name: pathName,
      })
    },
    goToDashboard() {
      this.$router.push({
        name: 'Home',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.project-dashboard-wrapper {
  width: 100%;
  height: 100%;
  padding-left: 70px;
}
</style>
