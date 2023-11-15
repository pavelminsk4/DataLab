<template>
  <TFSModuleScreen
    :workspaces="workspaces"
    :is-project-creation-available="isProjectCreationAvailable"
    @create-workspace="createWorkspace"
    @open-workspace="openWorkspace"
    @add-new-project="addNewProject"
  />
</template>

<script>
import {createNamespacedHelpers, mapGetters} from 'vuex'
import {get} from '@store/constants'

import TFSModuleScreen from '@components/twenty-four-seven/screens/TFSModuleScreen'

const {mapState: mapTFS} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSWorkspacesView',
  components: {
    TFSModuleScreen,
  },
  computed: {
    ...mapTFS(['workspaces']),
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_account_analysis_projects >=
        this.department?.max_projects_account_analysis
      )
    },
  },
  methods: {
    createWorkspace() {
      this.$router.push({
        name: 'TFSWorkspaceStep1',
        params: {workspaceId: 'new'},
      })
    },
    openWorkspace(workspaceId) {
      this.$router.push({
        name: 'TFSWorkspace',
        params: {workspaceId},
      })
    },
    addNewProject(workspaceId) {
      this.$router.push({
        name: 'TFSWorkspaceStep2',
        params: {workspaceId},
      })
    },
  },
}
</script>
