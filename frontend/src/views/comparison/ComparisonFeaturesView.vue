<template>
  <MainLayout v-if="workspaces.length">
    <SideBar :nav-urls="navUrls" @open-tab="openTab" />

    <div class="features">
      <div class="features__header">
        <MainLayoutTitleBlock
          :title="currentProject.title"
          :description="currentProject.note"
          :back-page="{
            name: 'workspaces',
            routeName: `ComparisonWorkspaces`,
          }"
          :should-translate="false"
        />
      </div>
      <router-view
        :current-project="currentProject"
        :projects-module="projectsModule"
      ></router-view>
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import SideBar from '@components/navigation/SideBar'
import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapState} = createNamespacedHelpers('comparison')

export default {
  name: 'ComparisonFeatureView',
  components: {MainLayout, MainLayoutTitleBlock, SideBar},
  props: {
    workspaces: {type: Array, required: true},
  },
  computed: {
    ...mapState(['loading']),
    currentWorkspace() {
      const existingWorkspace = this.workspaces.find(
        (el) => el.id === +this.workspaceId
      )
      if (!existingWorkspace && !this.loading) return this.goToNotFoundPage()

      return existingWorkspace
    },
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentProject() {
      if (isAllFieldsEmpty(this.currentWorkspace)) return

      const existingProject =
        this.currentWorkspace?.cmpr_workspace_projects.find(
          (el) => el.id === +this.projectId
        )
      if (!existingProject && !this.loading) return this.goToNotFoundPage()

      return existingProject
    },
    projectsModule() {
      return this.currentProject.cmpr_items[0].module_type === 'Project'
        ? 'online'
        : 'social'
    },
  },
  created() {
    if (!this.workspaces?.length) this[action.GET_WORKSPACES]()
    this.navUrls = ['Summary', 'Sentiment', 'Demography', 'Influencers'].map(
      (item) => ({
        name: item,
        routeName: `Comparison${item}`,
      })
    )
  },
  unmounted() {
    this[action.CLEAR_WIDGETS_DATA]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.CLEAR_WIDGETS_DATA]),
    isAllFieldsEmpty,
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
