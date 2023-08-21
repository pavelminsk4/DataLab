<template>
  <MainLayout>
    <div class="features">
      <div class="features__header">
        <MainLayoutTitleBlock
          :title="currentProject?.title"
          :back-page="{
            name: 'main page',
            routeName: `TwentyFourSevenWorkspaces`,
          }"
          :should-translate="false"
        />
      </div>
      <router-view :current-project="currentProject"></router-view>
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

const {mapState, mapActions} = createNamespacedHelpers('twentyFourSeven')

import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'

export default {
  name: 'TFSDashboardView',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
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
      return this.currentWorkspace[0]?.projects.find(
        (el) => el.id === +this.projectId
      )
    },
  },
  async created() {
    this[action.CLEAR_TFS_ITEMS]()

    if (!this.workspaces?.length) {
      await this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.CLEAR_TFS_ITEMS]),
  },
}
</script>

<style lang="scss" scoped>
.features {
  display: flex;
  flex-direction: column;
  gap: 30px;

  padding: 0px 0px 20px 0px;
  &__header {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}
</style>
