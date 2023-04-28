<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        title="Account Analysis"
        :back-page="{name: 'main page', routName: 'MainView'}"
      />

      <BaseButtonWithTooltip
        class="create-new-button"
        @click="$emit('create-workspace')"
      >
        <PlusIcon />
        <span>Create new workspace</span>
      </BaseButtonWithTooltip>
    </div>

    <div class="no-account-analysis-wrapper">
      <img
        src="@/assets/account-analysis/no-account-analysis-workspaces.svg"
        alt="No account analysis image"
      />
      <div>No workspaces created &#128542;</div>
    </div>
  </MainLayout>
</template>

<script>
// import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
// import {action, get} from '@store/constants'
// import {
//   action as actionAccountAnalysis,
//   get as getAccount,
// } from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip.vue'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock.vue'
import MainLayout from '@components/layout/MainLayout'
import PlusIcon from '@/components/icons/PlusIcon.vue'

export default {
  name: 'AccountAnalysisModuleScreen',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    BaseButtonWithTooltip,
    PlusIcon,
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}

.no-account-analysis-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
}
</style>
