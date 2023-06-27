<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        v-if="workspace?.title"
        :title="workspace.title"
        :description="workspace.description"
        :back-page="{
          name: 'main page',
          routeName: 'TwentyFourSevenWorkspaces',
        }"
      >
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        @click="createProject"
      >
        <PlusIcon /> Create new project
      </BaseButtonWithTooltip>
    </div>

    <div class="projects-wrapper scroll">
      <TFSProjectsTable
        :values="filteredProjects"
        :members="workspace?.members"
        @go-to-project="goToProject"
      />
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import PlusIcon from '@/components/icons/PlusIcon'
import TFSProjectsTable from '@/components/twenty-four-seven/TFSProjectsTable'

const {mapState: mapTFSState} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSWorkspaceView',
  components: {
    BaseButtonWithTooltip,
    MainLayout,
    MainLayoutTitleBlock,
    PlusIcon,
    TFSProjectsTable,
  },
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapTFSState(['workspaces']),
    ...mapGetters({
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      return this.workspaces.find((el) => el.id === +this.workspaceId)
    },
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
    filteredProjects() {
      if (!this.search) return this.workspace?.projects
      return this.workspace?.projects.filter((project) =>
        project.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  created() {
    this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.CLEAR_STATE]),
    createProject() {
      this.$router.push({
        name: 'TFSWorkspaceStep2',
        params: {workspaceId: this.workspaceId},
      })
    },
    goToProject(projectId) {
      this.$router.push({
        name: 'TFSDashboard',
        params: {projectId, workspaceId: this.workspaceId},
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}
</style>
