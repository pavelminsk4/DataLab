<template>
  <router-view :workspaces="workspaces" @create-workspace="createWorkspace">
  </router-view>
</template>

<script>
import {createNamespacedHelpers, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

const {mapActions, mapState} = createNamespacedHelpers('comparison')

export default {
  name: 'ComparisonModuleView',
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
    ...mapState(['workspaces']),
  },
  created() {
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    createWorkspace() {
      this.$router.push({
        name: 'ComparisonWorkspaceStep1',
        params: {workspaceId: 'new'},
      })
    },
  },
}
</script>
